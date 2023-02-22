from floodsystem.station import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

def run():
    """Requirements for task 2B: prints a list of stations where the current relative level is above 0.8"""
    stations = build_station_list()
    update_water_levels(stations) # Updates the water levels; build_station_list does not assign any latest_levels

    stations_above = stations_level_over_threshold(stations, 0.8)
    for i in range(len(stations_above)):
        print(str(stations_above[i][0].name) + " " + str(stations_above[i][1]))
    

if __name__ == "__main__":
    run()