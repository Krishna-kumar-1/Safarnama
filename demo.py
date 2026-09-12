from src.route_engine import RouteEngine


def print_itinerary(label: str, engine: RouteEngine, itinerary):
    if itinerary is None:
        print(f"\n{label}: no route found")
        return
    print(f"\n{label}  ({itinerary.num_legs} legs, {itinerary.total_duration_min} min, Rs.{itinerary.total_cost_inr:.0f})")
    for leg in itinerary.legs:
        src_name = engine.stations[leg.source].name
        dst_name = engine.stations[leg.destination].name
        flag = " [SOLD OUT]" if not leg.available else ""
        train = f" ({leg.train_number})" if leg.train_number else ""
        print(f"  {src_name} -> {dst_name}  [{leg.mode}]{train}  {leg.duration_min}min  Rs.{leg.cost_inr:.0f}{flag}")


def run(source, destination, date=None):
    engine = RouteEngine()
    print("=" * 70)
    print(f"{engine.stations[source].name} -> {engine.stations[destination].name}" + (f"  on {date}" if date else ""))
    print("=" * 70)

    result = engine.find_routes(source, destination, date=date)

    print_itinerary("FASTEST", engine, result["fastest"])
    print_itinerary("CHEAPEST", engine, result["cheapest"])
    print_itinerary("RECOMMENDED (balanced)", engine, result["recommended"])

    if result["warnings"]:
        print("\nDATE AVAILABILITY WARNINGS:")
        for w in result["warnings"]:
            print(f"  Train {w['train_number']} on {w['leg']} is SOLD OUT for {w['requested_date']}.")
            if w["alt_dates_available"]:
                print(f"    Try instead: {', '.join(w['alt_dates_available'])}")
            else:
                print("    No nearby dates available either.")

    print(f"\nTOP {len(result['alternatives'])} ALTERNATIVE ROUTES:")
    for i, alt in enumerate(result["alternatives"], 1):
        print_itinerary(f"  Option {i}", engine, alt)


if __name__ == "__main__":
    run("TATA", "SMVB")
    run("JSME", "DHN")
    run("JSME", "RNC")
