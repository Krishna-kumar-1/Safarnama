from dataclasses import dataclass, field


@dataclass
class Station:
    code: str
    name: str
    state: str
    # Stations imported from a timetable listing arrive without coordinates --
    # the source publishes none. They still route fine (the graph only needs
    # codes); they are simply skipped when snapping an arbitrary lat/lon to a
    # nearest station. None is used rather than 0.0 because 0,0 is a real
    # place in the Atlantic and would win "nearest" lookups from anywhere.
    lat: float | None = None
    lon: float | None = None

    @property
    def has_coords(self) -> bool:
        return self.lat is not None and self.lon is not None


@dataclass
class RouteLeg:
    source: str
    destination: str
    mode: str  # train / bus / cab / walk
    duration_min: int
    cost_inr: float
    train_number: str = ""
    train_name: str = ""
    available: bool = True
    date: str = ""  # YYYY-MM-DD, blank for road-based legs
    dep_time: str = ""  # HH:MM local departure clock time, blank for road-based legs
    arr_time: str = ""  # HH:MM local arrival clock time, blank for road-based legs
    # Seasonal/special trains only run inside a published window. Stored as
    # MM-DD (the source publishes no year) and compared cyclically, so a
    # window like 12-06 -> 08-29 correctly spans the new year. Blank on both
    # means the train runs year-round.
    valid_from: str = ""
    valid_to: str = ""
    # Weekdays the train runs, as "mon,wed,sat". Only the RailRadar import
    # supplies this; the scraped listings lose it in copy-paste. Blank means
    # unknown, which is treated as "runs" -- never as "never runs", or a
    # station would silently vanish from the network.
    run_days: str = ""


@dataclass
class Itinerary:
    legs: list[RouteLeg] = field(default_factory=list)

    @property
    def total_duration_min(self) -> int:
        return sum(leg.duration_min for leg in self.legs)

    @property
    def total_cost_inr(self) -> float:
        return sum(leg.cost_inr for leg in self.legs)

    @property
    def has_sold_out_leg(self) -> bool:
        return any(not leg.available for leg in self.legs)

    @property
    def num_legs(self) -> int:
        return len(self.legs)
