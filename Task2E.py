from floodsystem.plot import *
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta

def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    dt = timedelta(days=10) # time difference of 10 days
    plot_stations = stations_highest_rel_level(stations, N)
    for station in plot_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    run()