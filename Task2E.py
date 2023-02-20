from floodsystem.plot import *
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    plot_stations = stations_highest_rel_level(stations, 5)


if __name__ == "__main__":
    run()