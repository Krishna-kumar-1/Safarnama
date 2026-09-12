from datetime import date as date_cls, datetime, timedelta
from itertools import islice

import networkx as nx

from .data_loader import EXTRA_SUFFIXES, load_routes, load_stations
from .last_mile import last_mile_leg, nearest_station
from .models import Itinerary, RouteLeg

NEARBY_DAY_OFFSETS = [-2, -1, 1, 2]

# Added to every train edge's graph weight when optimizing for "fastest",
# never to the leg's own duration_min. Without this, shortest_path treats a
# transfer as free, so a chain of many short MEMU hops (each summing to a few
# minutes) can beat one direct long-distance train whose real board time
# includes waiting for its own scheduled departure -- a route no one would
# actually take. This is a graph-search bias, not a real travel time.
TRANSFER_PENALTY_MIN = 90


def estimate_class_fares(distance_km: float | None, base_cost: float = 0.0) -> dict[str, int]:
    """Calculate realistic Indian Railways dynamic class fares for a given distance."""
    if not distance_km or distance_km <= 0:
        d = max(50.0, base_cost / 1.1 if base_cost else 100.0)
    else:
        d = float(distance_km)

    return {
        "2S": max(45, round((d * 0.38 + 35) / 5) * 5),
        "SL": max(145, round((d * 0.62 + 60) / 5) * 5),
        "CC": max(260, round((d * 1.35 + 90) / 5) * 5),
        "3E": max(465, round((d * 1.52 + 110) / 5) * 5),
        "3A": max(510, round((d * 1.72 + 125) / 5) * 5),
        "2A": max(760, round((d * 2.45 + 160) / 5) * 5),
        "1A": max(1280, round((d * 4.10 + 220) / 5) * 5),
    }



# date.weekday() is 0 for Monday, matching this order.
WEEKDAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")


def runs_on(leg, travel_date) -> bool:
    """Does this train operate on the given date?

    Two independent gates, both of which must pass:

    * Weekday. RailRadar publishes the days a train runs ("mon,fri"); a
      Friday-only train must not appear in a Monday search.
    * Seasonal window. Stored as MM-DD because the timetable source publishes
      no year, and compared cyclically, so 12-06 -> 08-29 correctly spans the
      new year.

    A blank value on either means *unknown*, which is treated as "runs".
    Treating unknown as "never runs" would silently delete most of the
    network, since the scraped listings carry no running days at all.
    """
    if travel_date is None:
        return True
    if isinstance(travel_date, str):
        travel_date = date_cls.fromisoformat(travel_date)

    days = (getattr(leg, "run_days", "") or "").strip()
    if days:
        running = {d.strip().lower()[:3] for d in days.split(",") if d.strip()}
        if running and WEEKDAYS[travel_date.weekday()] not in running:
            return False

    if not leg.valid_from and not leg.valid_to:
        return True

    today = travel_date.strftime("%m-%d")
    start = leg.valid_from or leg.valid_to
    end = leg.valid_to or leg.valid_from
    if start <= end:
        return start <= today <= end
    # window wraps past 31 Dec
    return today >= start or today <= end


class RouteEngine:
    def __init__(self, stations_path=None, routes_path=None, extras=EXTRA_SUFFIXES):
        self.stations = load_stations(stations_path) if stations_path else load_stations()
        self.legs = load_routes(routes_path, extras=extras) if routes_path else load_routes(extras=extras)
        # (source, destination) -> legs between them. _build_graph asks for
        # every unique pair, once per criterion (fastest/cheapest/simplest);
        # without this index each call re-scans the entire leg list, which
        # is fine at hundreds of legs but scales badly past a few thousand.
        self._legs_by_pair: dict[tuple[str, str], list[RouteLeg]] = {}
        self._legs_by_train: dict[str, list[RouteLeg]] = {}
        for leg in self.legs:
            self._legs_by_pair.setdefault((leg.source, leg.destination), []).append(leg)
            if leg.train_number:
                self._legs_by_train.setdefault(leg.train_number, []).append(leg)

    def get_leg_path_stations(self, source: str, destination: str, train_number: str = "") -> list[str]:
        """Return ordered list of station codes representing the railway line halts."""
        if source == destination:
            return [source]

        if train_number and train_number in self._legs_by_train:
            t_legs = self._legs_by_train[train_number]
            # 1. Direct pairs starting from source
            from_src = [l for l in t_legs if l.source == source]
            matching_dest = [l for l in from_src if l.destination == destination]
            if matching_dest:
                max_dur = matching_dest[0].duration_min
                halts_legs = [l for l in from_src if 0 < l.duration_min <= max_dur]
                halts_legs.sort(key=lambda l: l.duration_min)
                if halts_legs and halts_legs[-1].destination == destination:
                    return [source] + [l.destination for l in halts_legs]

            # 2. Directed graph of all halts for this train number
            tg = nx.DiGraph()
            for l in t_legs:
                tg.add_edge(l.source, l.destination, weight=l.duration_min)
            if source in tg and destination in tg and nx.has_path(tg, source, destination):
                try:
                    return nx.shortest_path(tg, source, destination, weight="weight")
                except Exception:
                    pass

        return [source, destination]

    # ---- edge selection -------------------------------------------------

    def _candidate_legs(self, source: str, destination: str, date: str | None):
        """All raw legs between two stations, optionally filtered to a travel date.

        Road-based legs (cab/bus/walk) have no date and always match.
        """
        out = self._legs_by_pair.get((source, destination), [])
        if date is None:
            return out
        # drop seasonal trains that don't run on this date, then apply any
        # per-date row filter
        out = [leg for leg in out if runs_on(leg, date)]
        return [leg for leg in out if leg.date == "" or leg.date == date]

    def _best_leg(self, source: str, destination: str, date: str | None, criterion: str) -> RouteLeg | None:
        candidates = [leg for leg in self._candidate_legs(source, destination, date) if leg.available]
        if not candidates:
            return None
        key = (lambda l: l.duration_min) if criterion == "duration_min" else (lambda l: l.cost_inr)
        return min(candidates, key=key)

    def _sold_out_leg(self, source: str, destination: str, date: str) -> RouteLeg | None:
        """Return a leg that exists for this date but is sold out (for flagging + suggestions)."""
        for leg in self._candidate_legs(source, destination, date):
            if not leg.available:
                return leg
        return None

    def suggest_alt_dates(self, source: str, destination: str, train_number: str, date: str) -> list[str]:
        base = datetime.strptime(date, "%Y-%m-%d").date()
        found = []
        for offset in NEARBY_DAY_OFFSETS:
            candidate_date = (base + timedelta(days=offset)).isoformat()
            for leg in self.legs:
                if (
                    leg.source == source
                    and leg.destination == destination
                    and leg.train_number == train_number
                    and leg.date == candidate_date
                    and leg.available
                ):
                    found.append(candidate_date)
                    break
        return sorted(found)

    # ---- graph construction ----------------------------------------------

    def _build_graph(self, date: str | None, criterion: str) -> nx.DiGraph:
        weight_attr = "duration_min" if criterion == "duration_min" else "cost_inr"
        graph = nx.DiGraph()
        graph.add_nodes_from(self.stations.keys())
        pairs = {(leg.source, leg.destination) for leg in self.legs}
        for source, destination in pairs:
            # "hops" picks the fewest-transfer route: every edge costs the same
            # (1), so shortest_path minimizes leg count instead of time/fare.
            # duration_min still breaks ties between parallel trains on the
            # same station pair, so we don't pick an arbitrarily slow one.
            best = self._best_leg(source, destination, date, "duration_min" if criterion == "hops" else criterion)
            if best is not None:
                if criterion == "hops":
                    weight = 1
                else:
                    weight = getattr(best, weight_attr)
                    if criterion == "duration_min":
                        weight += TRANSFER_PENALTY_MIN
                graph.add_edge(source, destination, weight=weight, leg=best)
        return graph

    def _path_to_itinerary(self, graph: nx.DiGraph, path: list[str]) -> Itinerary:
        legs = [graph[u][v]["leg"] for u, v in zip(path, path[1:])]
        return Itinerary(legs=legs)

    # ---- public API --------------------------------------------------------

    def find_routes(self, source: str, destination: str, date: str | None = None, top_n: int = 3):
        """Return fastest, cheapest, recommended (balanced) itineraries plus alternatives.

        Also returns per-leg sold-out flags and nearby-date suggestions when the
        requested date has no available seat on a leg the traveller would need.
        """
        if source not in self.stations or destination not in self.stations:
            raise ValueError(f"Unknown station: {source} or {destination}")

        fastest_graph = self._build_graph(date, "duration_min")
        cheapest_graph = self._build_graph(date, "cost_inr")
        simplest_graph = self._build_graph(date, "hops")

        result = {"fastest": None, "cheapest": None, "recommended": None, "simplest": None, "alternatives": [], "warnings": []}

        if nx.has_path(fastest_graph, source, destination):
            fastest_path = nx.shortest_path(fastest_graph, source, destination, weight="weight")
            # If a direct 1-leg train exists between source and destination, prioritize it if its duration is competitive
            direct_leg = self._best_leg(source, destination, date, "duration_min")
            if direct_leg and len(fastest_path) > 2:
                fastest_itin = self._path_to_itinerary(fastest_graph, fastest_path)
                if direct_leg.duration_min <= fastest_itin.total_duration_min + 300:
                    fastest_path = [source, destination]
            result["fastest"] = self._path_to_itinerary(fastest_graph, fastest_path)

        if nx.has_path(cheapest_graph, source, destination):
            cheapest_path = nx.shortest_path(cheapest_graph, source, destination, weight="weight")
            result["cheapest"] = self._path_to_itinerary(cheapest_graph, cheapest_path)

        if nx.has_path(simplest_graph, source, destination):
            simplest_path = nx.shortest_path(simplest_graph, source, destination, weight="weight")
            result["simplest"] = self._path_to_itinerary(simplest_graph, simplest_path)

        if result["fastest"] and result["cheapest"]:
            result["recommended"] = self._pick_balanced(result["fastest"], result["cheapest"], fastest_graph, cheapest_graph, source, destination)

        # top-N alternatives on the fastest-graph topology
        if nx.has_path(fastest_graph, source, destination):
            simple_graph = fastest_graph.to_undirected(as_view=False)
            try:
                paths = list(islice(nx.shortest_simple_paths(fastest_graph, source, destination, weight="weight"), top_n))
            except nx.NetworkXNoPath:
                paths = []
            result["alternatives"] = [self._path_to_itinerary(fastest_graph, p) for p in paths]

        # date-based sold-out detection + suggestions, checked against the fastest itinerary's legs
        if date and result["fastest"]:
            for leg in result["fastest"].legs:
                if leg.mode != "train":
                    continue
                sold_out = self._sold_out_leg(leg.source, leg.destination, date)
                if sold_out and sold_out.train_number:
                    alt_dates = self.suggest_alt_dates(leg.source, leg.destination, sold_out.train_number, date)
                    result["warnings"].append(
                        {
                            "leg": f"{leg.source}->{leg.destination}",
                            "train_number": sold_out.train_number,
                            "requested_date": date,
                            "sold_out": True,
                            "alt_dates_available": alt_dates,
                        }
                    )

        return result

    def find_routes_to_coordinates(self, source: str, dest_lat: float, dest_lon: float, dest_label: str = "destination", date: str | None = None, top_n: int = 3):
        """Route to an arbitrary point (e.g. a street address) via its nearest station.

        Appends a walk/cab/bus last-mile leg from the nearest station to the
        given coordinates, chosen by distance threshold.
        """
        station, distance_km = nearest_station(self.stations, dest_lat, dest_lon)
        result = self.find_routes(source, station.code, date=date, top_n=top_n)

        last_leg = last_mile_leg(station.code, dest_label, distance_km)
        for key in ("fastest", "cheapest", "recommended", "simplest"):
            if result[key] is not None:
                result[key] = Itinerary(legs=result[key].legs + [last_leg])
        result["alternatives"] = [Itinerary(legs=alt.legs + [last_leg]) for alt in result["alternatives"]]
        result["nearest_station"] = station
        result["last_mile_distance_km"] = round(distance_km, 2)
        return result

    # ---- schedule-aware planning (real dep/arr clock times, layover waits) ----

    def schedule_itinerary(self, itinerary: Itinerary, start_date: str, start_time: str = "00:00") -> dict:
        """Walk an itinerary leg by leg against real departure clock times.

        Road-based legs (walk/cab/bus) are treated as departing immediately
        (no fixed timetable) once the traveller is ready. Train legs wait
        for the next occurrence of their daily departure clock time, which
        may push departure to the next calendar day if it's already passed.
        Returns per-leg schedule plus total wait and total door-to-door
        elapsed time (which can exceed the sum of leg durations).
        """
        current = datetime.combine(date_cls.fromisoformat(start_date), datetime.strptime(start_time, "%H:%M").time())
        start = current
        legs_out = []
        total_wait_min = 0

        for leg in itinerary.legs:
            if leg.dep_time:
                dep_clock = datetime.strptime(leg.dep_time, "%H:%M").time()
                departure = datetime.combine(current.date(), dep_clock)
                if departure < current:
                    departure += timedelta(days=1)
            else:
                departure = current

            wait_min = round((departure - current).total_seconds() / 60)
            arrival = departure + timedelta(minutes=leg.duration_min)
            total_wait_min += wait_min

            legs_out.append(
                {
                    "source": leg.source,
                    "destination": leg.destination,
                    "mode": leg.mode,
                    "train_number": leg.train_number,
                    "train_name": leg.train_name,
                    "dep_date": departure.date().isoformat(),
                    "dep_time": departure.strftime("%H:%M"),
                    "arr_date": arrival.date().isoformat(),
                    "arr_time": arrival.strftime("%H:%M"),
                    "wait_min": wait_min,
                    "duration_min": leg.duration_min,
                    # a long journey can reach a later leg after its seasonal
                    # window has closed, so re-check on the real boarding date
                    "runs_on_date": runs_on(leg, departure.date()),
                    "valid_from": leg.valid_from,
                    "valid_to": leg.valid_to,
                }
            )
            current = arrival

        total_elapsed_min = round((current - start).total_seconds() / 60)
        return {
            "legs": legs_out,
            "all_legs_run_on_date": all(l["runs_on_date"] for l in legs_out),
            "start_date": start.date().isoformat(),
            "start_time": start.strftime("%H:%M"),
            "arrival_date": current.date().isoformat(),
            "arrival_time": current.strftime("%H:%M"),
            "total_elapsed_min": total_elapsed_min,
            "total_wait_min": total_wait_min,
            "total_days": (current.date() - start.date()).days + 1,
        }

    def plan_journey(self, source: str, destination: str, start_date: str, start_time: str = "00:00", top_n: int = 5):
        """Pick the itinerary with the least real door-to-door time for an actual departure.

        Candidate routes come from the duration-weighted graph's top_n simple
        paths; each is simulated against real departure clock times so a
        route with a long layover can lose to a nominally "slower" one with
        a better-timed connection.
        """
        if source not in self.stations or destination not in self.stations:
            raise ValueError(f"Unknown station: {source} or {destination}")

        # only consider trains actually running on the departure date
        graph = self._build_graph(start_date, "duration_min")
        if source not in graph or destination not in graph:
            return None
        if not nx.has_path(graph, source, destination):
            return None

        try:
            paths = list(islice(nx.shortest_simple_paths(graph, source, destination, weight="weight"), top_n))
        except nx.NetworkXNoPath:
            return None

        # Also try the fewest-transfer path. A single long-haul train can lose
        # on the duration-graph's flat weighting (it doesn't know about real
        # departure times) while still being the actual best real-world
        # option once simulated -- so it needs to be in the candidate pool,
        # not just assumed to lose.
        simplest_graph = self._build_graph(start_date, "hops")
        if source in simplest_graph and destination in simplest_graph and nx.has_path(simplest_graph, source, destination):
            simplest_path = nx.shortest_path(simplest_graph, source, destination, weight="weight")
            if simplest_path not in paths:
                paths.append(simplest_path)

        candidates = []
        for path in paths:
            itinerary = self._path_to_itinerary(graph, path)
            schedule = self.schedule_itinerary(itinerary, start_date, start_time)
            candidates.append({"itinerary": itinerary, "schedule": schedule})

        # prefer itineraries whose every leg still runs on its boarding date,
        # then by shortest real door-to-door time,
        # then prioritize single-leg (direct) routes / fewest legs
        best = min(
            candidates,
            key=lambda c: (
                not c["schedule"]["all_legs_run_on_date"],
                c["schedule"]["total_elapsed_min"],
                c["itinerary"].num_legs,
            ),
        )
        return {
            "best": best,
            "alternatives": [c for c in candidates if c is not best],
        }

    def plan_journey_flexible(self, source: str, destination: str, start_date: str, start_time: str = "00:00", days_range: int = 3):
        """Search for routes across nearby dates (+-days_range) and recommend direct/fewer-leg routes."""
        base_date = date_cls.fromisoformat(start_date)
        exact_plan = self.plan_journey(source, destination, start_date, start_time)

        # Offsets to check in order of closeness: +1, -1, +2, -2, +3, -3...
        offsets = []
        for d in range(1, days_range + 1):
            offsets.extend([d, -d])

        flexible_options = []
        direct_legs = [l for l in self._legs_by_pair.get((source, destination), []) if l.available and l.mode == "train"]
        direct_dates_seen = set()

        # 1. Quick Direct (1-leg) train scan across candidate dates
        for offset in offsets:
            cand_date = base_date + timedelta(days=offset)
            cand_date_str = cand_date.isoformat()
            matching_direct = [l for l in direct_legs if runs_on(l, cand_date_str)]
            for d_leg in matching_direct:
                itin = Itinerary(legs=[d_leg])
                sched = self.schedule_itinerary(itin, cand_date_str, start_time)
                if sched["all_legs_run_on_date"] and cand_date_str not in direct_dates_seen:
                    direct_dates_seen.add(cand_date_str)
                    offset_sign = "+" if offset > 0 else ""
                    day_word = "day" if abs(offset) == 1 else "days"
                    flexible_options.append({
                        "date": cand_date_str,
                        "offset_days": offset,
                        "is_direct": True,
                        "num_legs": 1,
                        "advantage": f"Direct 1-Leg train available on {cand_date.strftime('%d %b %Y')} ({offset_sign}{offset} {day_word})",
                        "candidate": {"itinerary": itin, "schedule": sched}
                    })

        # 2. General plan_journey search on nearby dates
        for offset in offsets:
            cand_date = base_date + timedelta(days=offset)
            cand_date_str = cand_date.isoformat()
            if cand_date_str in direct_dates_seen:
                continue
            try:
                plan = self.plan_journey(source, destination, cand_date_str, start_time)
                if plan and plan.get("best"):
                    best_c = plan["best"]
                    legs_count = best_c["itinerary"].num_legs
                    exact_legs_count = exact_plan["best"]["itinerary"].num_legs if (exact_plan and exact_plan.get("best")) else 99

                    # If nearby date has fewer legs than exact date or offers a clean direct/2-leg connection
                    if legs_count < exact_legs_count or (legs_count <= 2 and exact_legs_count > 1):
                        offset_sign = "+" if offset > 0 else ""
                        day_word = "day" if abs(offset) == 1 else "days"
                        leg_word = "1-Leg Direct train" if legs_count == 1 else f"{legs_count}-Leg route"
                        flexible_options.append({
                            "date": cand_date_str,
                            "offset_days": offset,
                            "is_direct": (legs_count == 1),
                            "num_legs": legs_count,
                            "advantage": f"{leg_word} available on {cand_date.strftime('%d %b %Y')} ({offset_sign}{offset} {day_word})",
                            "candidate": best_c
                        })
            except Exception:
                pass

        # Sort flexible options by: (num_legs, abs(offset_days), total_elapsed_min)
        flexible_options.sort(key=lambda x: (
            x["num_legs"],
            abs(x["offset_days"]),
            x["candidate"]["schedule"]["total_elapsed_min"]
        ))

        return {
            "exact_plan": exact_plan,
            "flexible_options": flexible_options[:6]
        }

    def _pick_balanced(self, fastest: Itinerary, cheapest: Itinerary, fastest_graph, cheapest_graph, source, destination) -> Itinerary:
        if fastest.legs == cheapest.legs:
            return fastest

        candidates = [fastest, cheapest]
        try:
            for path in islice(nx.shortest_simple_paths(fastest_graph, source, destination, weight="weight"), 5):
                candidates.append(self._path_to_itinerary(fastest_graph, path))
        except nx.NetworkXNoPath:
            pass

        durations = [c.total_duration_min for c in candidates]
        costs = [c.total_cost_inr for c in candidates]
        d_min, d_max = min(durations), max(durations)
        c_min, c_max = min(costs), max(costs)

        def norm(value, lo, hi):
            return 0.0 if hi == lo else (value - lo) / (hi - lo)

        best, best_score = None, float("inf")
        for candidate in candidates:
            score = 0.5 * norm(candidate.total_duration_min, d_min, d_max) + 0.5 * norm(candidate.total_cost_inr, c_min, c_max)
            if score < best_score:
                best, best_score = candidate, score
        return best
