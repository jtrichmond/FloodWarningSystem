from floodsystem.station import *
from floodsystem.stationdata import build_station_list
from floodsystem.flood import *

def run():
    """Requirements for task 2B: prints a list of stations where the current relative level is above 0.8"""
    stations = build_station_list()
    #converts filter object to list, filter object is returned from method, contains stations which fit criteria
    """
    Work in progress
    stations_above = stations_level_over_threshold(stations, 0.8)
    for i in range(len(stations_above)):
        print(str(stations_above[i][0]) + " " + str(stations_above[i][1]))
    """

if __name__ == "__main__":
    run()