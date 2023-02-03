def run():
    from floodsystem.geo import sum_station_number
    from floodsystem.geo import rivers_by_station_number
    from floodsystem.stationdata import build_station_list

    stations = build_station_list()

    print(rivers_by_station_number(stations, 100))

if __name__ == "__main__":
    run()