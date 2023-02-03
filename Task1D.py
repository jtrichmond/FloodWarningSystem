from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_on_given_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""
    #Changed because of change of return from stations_by_river to objects not names
    stations = build_station_list()

    print(str(len(rivers_with_station(stations))) + " stations. First 10 - " 
    + str(sorted(rivers_with_station(stations))[:10]))

    #don't need to run this 3 times
    """print(stations_by_river(stations)["River Aire"])
    print(stations_by_river(stations)["River Cam"])
    print(stations_by_river(stations)["River Thames"])"""
    river_stations_dict = stations_by_river(stations)
    print([station.name for station in river_stations_dict["River Aire"]])
    print([station.name for station in river_stations_dict["River Cam"]])
    print([station.name for station in river_stations_dict["River Thames"]])

if __name__ == "__main__":
    run()