from floodsystem.plot import *
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta

def run():
    """Functionality for 2F"""
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    p = 4
    dt = timedelta(days=2) # time difference of 2 days
    plot_stations = stations_highest_rel_level(stations, N)
    for station in plot_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_level_with_fit(station, dates, levels, p)

if __name__ == "__main__":
    run()