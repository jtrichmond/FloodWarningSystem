from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
from random import randint # for sampling

"""Unit test for the geo module"""

def test_distance_between_coords():
    #using example from haversine docs
    p1 = (45.7597, 4.8422)
    p2 = (48.8567, 2.3508)
    x =  distance_between_coords(p1, p2)
    assert round(x, 5) == 392.21725 # 5 digits after decimal point

def test_stations_by_distance():
    stations = build_station_list()
    point = (52.2053, 0.1218)
    stations_distance_list = stations_by_distance(stations, point)
    assert len(stations_distance_list) == len(stations)
    assert stations_distance_list[randint(len(stations))][0] in stations
    for i in range(len(stations) -1):
        assert stations_distance_list[i][1] <= stations_distance_list[i+1][1]


