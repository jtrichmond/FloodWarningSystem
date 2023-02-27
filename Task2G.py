from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    list_of_towns_severe = []
    list_of_towns_high = []
    list_of_towns_mod = []
    list_of_towns_low = []

    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > 1.2:
                list_of_towns_severe.append(station.town)
            if 1 < station.relative_water_level() < 1.2:
                list_of_towns_high.append(station.town)
            if 0.7 < station.relative_water_level() < 1:
                list_of_towns_mod.append(station.town)
            if station.relative_water_level() < 0.7:
                list_of_towns_low.append(station.town)

    print(f"Towns at severe flood risk: {list_of_towns_severe}")
    print(f"Towns at high flood risk: {list_of_towns_high}")
    print(f"Towns at moderate flood risk: {list_of_towns_mod}")


if __name__ == "__main__":
    run()