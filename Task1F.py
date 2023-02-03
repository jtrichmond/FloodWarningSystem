from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_property

def run(): # this is wrong
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)
    inconsistent = sorted_by_property(inconsistent, "name")
    names = [station.name for station in inconsistent]
    print(names)


if __name__ == "__main__":
    run()