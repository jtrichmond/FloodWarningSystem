def run():
    from floodsystem.geo import rivers_with_station
    from floodsystem.geo import stations_by_river
    from floodsystem.geo import stations_on_given_river
    from floodsystem.stationdata import build_station_list

    stations = build_station_list()

    print(str(len(rivers_with_station(stations))) + " stations. First 10 - " 
    + str(sorted(rivers_with_station(stations))[:10]))


    print(stations_by_river(stations)["River Aire"])
    print(stations_by_river(stations)["River Cam"])
    print(stations_by_river(stations)["River Thames"])

if __name__ == "__main__":
    run()