from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10

    list_stations_highest_rel_level = stations_highest_rel_level(stations, N)
    """
    for i in range(N):
        #print(list_stations_highest_rel_level[i][0], list_stations_highest_rel_level[i][1]) stations_highest_rel_level only returns station objects, not a tuple
    """
    for station in list_stations_highest_rel_level:
        print(station.name + " " + str(station.relative_water_level()))


if __name__ == "__main__":
    run()