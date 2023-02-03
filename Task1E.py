from floodsystem.geo import sum_station_number
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """requirements for Task 1E"""
    stations = build_station_list()

    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    run()