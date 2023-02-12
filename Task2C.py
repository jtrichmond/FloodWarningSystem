from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    N = 10

    list_stations_highest_rel_level = stations_highest_rel_level(stations, N)
    for i in range(N):
        print(list_stations_highest_rel_level[i][0], list_stations_highest_rel_level[i][1])

if __name__ == "__main__":
    run()