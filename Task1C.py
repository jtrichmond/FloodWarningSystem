from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_property

def run():
    stations = build_station_list()
    point = (52.2053, 0.1218)
    distance = 10 #km
    stations_in_range = stations_within_radius(stations, point, distance)
    stations_in_range = sorted_by_property(stations_in_range, 'name')
    print([station.name for station in stations_in_range])

if __name__ == "__main__":
    run()
