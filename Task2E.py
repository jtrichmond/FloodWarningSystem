from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

def run():
    
    # Build list of stations
    stations = build_station_list()

    # Station name to find
    station_name = "Cam"

    # Find station
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dates))

    return print(plot_water_levels(station, 10.0))


if __name__ == "__main__":
    run()