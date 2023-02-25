from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import pytest
from datetime import timedelta

def test_plot_water_levels():
    stations = build_station_list()
    update_water_levels(stations)
    
    #Check that an error is raised if N is greater than number of stations
    with pytest.raises(Exception):
        dt = timedelta(days=10)
        plot_stations = stations_highest_rel_level(stations, 1000)
        for station in plot_stations:
            dates, levels = fetch_measure_levels(station.measure_id, dt)



if __name__ == "__main__":
    test_plot_water_levels()