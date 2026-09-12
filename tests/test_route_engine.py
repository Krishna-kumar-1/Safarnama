import time
import unittest

import networkx as nx

from src.data_loader import DATA_DIR, load_routes
from src.models import RouteLeg
from src.route_engine import RouteEngine, runs_on


class TestRouteEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RouteEngine()

    def test_direct_route(self):
        result = self.engine.find_routes("TATA", "SMVB")
        self.assertIsNotNone(result["fastest"])
        self.assertEqual(result["fastest"].num_legs, 1)
        self.assertEqual(result["fastest"].legs[0].train_number, "12889")

    def test_no_direct_route_returns_multi_leg(self):
        result = self.engine.find_routes("GKP", "TATA")
        self.assertIsNotNone(result["fastest"])
        self.assertGreater(result["fastest"].num_legs, 1)
        self.assertEqual(result["fastest"].legs[0].source, "GKP")
        self.assertEqual(result["fastest"].legs[-1].destination, "TATA")

    def test_cheapest_is_not_more_expensive_than_fastest(self):
        result = self.engine.find_routes("JSME", "DHN")
        self.assertLessEqual(result["cheapest"].total_cost_inr, result["fastest"].total_cost_inr)

    def test_top_alternatives_returned(self):
        result = self.engine.find_routes("JSME", "RNC")
        self.assertGreaterEqual(len(result["alternatives"]), 1)
        self.assertLessEqual(len(result["alternatives"]), 3)

    def test_unknown_station_raises(self):
        with self.assertRaises(ValueError):
            self.engine.find_routes("XXXX", "RNC")

    def test_last_mile_walk_for_short_distance(self):
        # ~0.7km north of Siliguri Jn, inside the walkable threshold
        result = self.engine.find_routes_to_coordinates("TATA", 26.7301, 88.4137, dest_label="Near SGUJ")
        last_leg = result["fastest"].legs[-1]
        self.assertEqual(last_leg.mode, "walk")
        self.assertEqual(last_leg.cost_inr, 0.0)

    def test_last_mile_bus_for_long_distance(self):
        # ~29.5km from Darjeeling station, well past the 15km cab threshold
        result = self.engine.find_routes_to_coordinates("TATA", 27.2, 88.5, dest_label="Far Town")
        last_leg = result["fastest"].legs[-1]
        self.assertEqual(last_leg.mode, "bus")

    def test_schedule_waits_same_day_when_departure_still_ahead(self):
        # Train 12889 TATA->SMVB departs 17:45; leaving ready at 10:00 waits same-day.
        itinerary = self.engine.find_routes("TATA", "SMVB")["fastest"]
        schedule = self.engine.schedule_itinerary(itinerary, "2026-08-20", "10:00")
        leg = schedule["legs"][0]
        self.assertEqual(leg["dep_date"], "2026-08-20")
        self.assertEqual(leg["dep_time"], "17:45")
        self.assertEqual(leg["wait_min"], 465)  # 10:00 -> 17:45
        self.assertEqual(schedule["total_elapsed_min"], leg["wait_min"] + itinerary.total_duration_min)

    def test_schedule_rolls_to_next_day_when_departure_already_passed(self):
        # Same train, but 20:00 start is past today's 17:45 departure.
        itinerary = self.engine.find_routes("TATA", "SMVB")["fastest"]
        schedule = self.engine.schedule_itinerary(itinerary, "2026-08-20", "20:00")
        leg = schedule["legs"][0]
        self.assertEqual(leg["dep_date"], "2026-08-21")
        self.assertEqual(leg["wait_min"], 1305)  # 20:00 -> next day 17:45

    def test_plan_journey_picks_minimum_real_elapsed_time(self):
        planned = self.engine.plan_journey("JSME", "RNC", "2026-08-20", "09:00")
        self.assertIsNotNone(planned)
        best_elapsed = planned["best"]["schedule"]["total_elapsed_min"]
        for alt in planned["alternatives"]:
            self.assertLessEqual(best_elapsed, alt["schedule"]["total_elapsed_min"])
        # real elapsed time must include any layover waits, so it can't be
        # shorter than the itinerary's raw summed travel duration
        self.assertGreaterEqual(best_elapsed, planned["best"]["itinerary"].total_duration_min)

    def test_plan_journey_unknown_station_raises(self):
        with self.assertRaises(ValueError):
            self.engine.plan_journey("XXXX", "RNC", "2026-08-20", "09:00")

    def test_every_route_references_a_known_station(self):
        unknown = {
            code
            for leg in self.engine.legs
            for code in (leg.source, leg.destination)
            if code not in self.engine.stations
        }
        self.assertEqual(unknown, set())

    def test_core_network_is_fully_connected(self):
        # The hand-curated network must stay fully round-trippable: every
        # station reachable from every other. Bulk imports are excluded here
        # because a listing often contains a train one way and not its return.
        legs = load_routes(DATA_DIR / "routes.csv", extras=("specials",))
        graph = nx.DiGraph()
        for leg in legs:
            graph.add_edge(leg.source, leg.destination)
        self.assertTrue(
            nx.is_strongly_connected(graph),
            "curated network split into "
            f"{nx.number_strongly_connected_components(graph)} pieces",
        )

    def test_network_is_not_fragmented(self):
        # A bulk import can leave a small island behind -- a train whose
        # connecting services are in a listing nobody has collected yet. That
        # is a data-completeness gap, so a couple of stray stations must not
        # fail the build. What must fail is the network actually shattering,
        # or a station appearing with no trains at all.
        graph = self.engine._build_graph(None, "duration_min")
        biggest = max(nx.weakly_connected_components(graph), key=len)
        share = len(biggest) / graph.number_of_nodes()
        self.assertGreaterEqual(
            share, 0.95,
            f"only {share:.0%} of stations are in the main network; "
            f"{nx.number_weakly_connected_components(graph)} islands",
        )
        stranded = [n for n in graph if graph.degree(n) == 0]
        self.assertEqual(stranded, [], f"stations with no trains: {stranded}")

    def test_cross_country_route_completes_quickly(self):
        # guards against re-introducing list(shortest_simple_paths(...)), which
        # enumerates every simple path and hangs on a densely connected graph
        start = time.monotonic()
        result = self.engine.find_routes("JSME", "TVC")
        elapsed = time.monotonic() - start
        self.assertIsNotNone(result["fastest"])
        self.assertLess(elapsed, 10.0)

    def test_runs_on_within_and_outside_window(self):
        leg = RouteLeg("A", "B", "train", 60, 100, valid_from="08-14", valid_to="09-04")
        self.assertTrue(runs_on(leg, "2026-08-20"))
        self.assertTrue(runs_on(leg, "2026-08-14"))  # inclusive start
        self.assertTrue(runs_on(leg, "2026-09-04"))  # inclusive end
        self.assertFalse(runs_on(leg, "2026-08-13"))
        self.assertFalse(runs_on(leg, "2026-09-05"))

    def test_runs_on_window_wrapping_new_year(self):
        # 09-28 -> 08-16 spans past 31 Dec (train 04716 Shirdi->Bikaner)
        leg = RouteLeg("A", "B", "train", 60, 100, valid_from="09-28", valid_to="08-16")
        self.assertTrue(runs_on(leg, "2026-12-25"))
        self.assertTrue(runs_on(leg, "2026-01-10"))
        self.assertTrue(runs_on(leg, "2026-08-16"))
        self.assertFalse(runs_on(leg, "2026-09-01"))

    def test_run_days_excludes_wrong_weekday(self):
        # 2026-08-21 is a Friday, 2026-08-24 a Monday.
        leg = RouteLeg("A", "B", "train", 60, 100, run_days="fri")
        self.assertTrue(runs_on(leg, "2026-08-21"))
        self.assertFalse(runs_on(leg, "2026-08-24"))

    def test_run_days_blank_means_unknown_not_never(self):
        # Scraped listings carry no running days. Treating blank as "never"
        # would delete most of the network.
        leg = RouteLeg("A", "B", "train", 60, 100, run_days="")
        for day in ("2026-08-21", "2026-08-22", "2026-08-24"):
            self.assertTrue(runs_on(leg, day))

    def test_run_days_and_season_window_both_apply(self):
        # Friday-only AND only inside an August window: needs both to pass.
        leg = RouteLeg("A", "B", "train", 60, 100,
                       valid_from="08-01", valid_to="08-31", run_days="fri")
        self.assertTrue(runs_on(leg, "2026-08-21"))    # Friday, in window
        self.assertFalse(runs_on(leg, "2026-08-24"))   # Monday, in window
        self.assertFalse(runs_on(leg, "2026-09-04"))   # Friday, out of window

    def test_run_days_respected_when_building_the_graph(self):
        # Real legs from the RailRadar import carry running days, so a dated
        # search must drop the trains that do not run that day. Which weekday
        # is busier depends on the data, so assert the shape rather than a
        # direction: every dated graph is a subset of the undated one, and two
        # different weekdays do not produce the same graph.
        everything = self.engine._build_graph(None, "duration_min")
        friday = self.engine._build_graph("2026-08-21", "duration_min")
        monday = self.engine._build_graph("2026-08-24", "duration_min")

        self.assertLess(friday.number_of_edges(), everything.number_of_edges())
        self.assertLess(monday.number_of_edges(), everything.number_of_edges())
        self.assertNotEqual(
            set(friday.edges()), set(monday.edges()),
            "weekday filtering had no effect on the graph",
        )

    def test_friday_only_train_is_absent_on_monday(self):
        # 22306 is Friday-only in the API data and ASN->DGR is one of its
        # mid-route halt legs. Other trains also run that pair, so the edge
        # itself survives Monday -- what must not survive is this train.
        def trains(day):
            return {leg.train_number
                    for leg in self.engine._candidate_legs("ASN", "DGR", day)}

        self.assertIn("22306", trains("2026-08-21"))
        self.assertNotIn("22306", trains("2026-08-24"))

    def test_runs_on_year_round_train_always_runs(self):
        leg = RouteLeg("A", "B", "train", 60, 100)
        self.assertTrue(runs_on(leg, "2026-01-01"))
        self.assertTrue(runs_on(leg, "2026-07-04"))

    def test_seasonal_train_excluded_from_out_of_window_graph(self):
        # Ganpati specials run in September only, so SWV is served then and
        # stranded in January. Total edge counts are not compared: other
        # seasonal windows (the summer mela specials) close before September,
        # so neither month is reliably the busier one.
        specials_engine = RouteEngine(extras=("specials",))
        september = specials_engine._build_graph("2026-09-15", "duration_min")
        january = specials_engine._build_graph("2026-01-15", "duration_min")
        self.assertGreater(september.out_degree("SWV") + september.in_degree("SWV"), 0)
        self.assertEqual(january.out_degree("SWV") + january.in_degree("SWV"), 0)

    def test_plan_journey_flags_legs_outside_their_window(self):
        planned = self.engine.plan_journey("DHN", "RNC", "2026-08-20", "09:00")
        self.assertIsNotNone(planned)
        schedule = planned["best"]["schedule"]
        self.assertIn("all_legs_run_on_date", schedule)
        for leg in schedule["legs"]:
            self.assertIn("runs_on_date", leg)

    def test_plan_journey_completes_quickly(self):
        start = time.monotonic()
        planned = self.engine.plan_journey("DHN", "MAS", "2026-08-20", "09:00")
        elapsed = time.monotonic() - start
        self.assertIsNotNone(planned)
        self.assertLess(elapsed, 10.0)


if __name__ == "__main__":
    unittest.main()
