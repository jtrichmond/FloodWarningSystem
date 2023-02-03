from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
from trialdata import sample_stations

"""Unit test for the geo module"""

def test_distance_between_coords():
    #using example from haversine docs
    p1 = (45.7597, 4.8422)
    p2 = (48.8567, 2.3508)
    x =  distance_between_coords(p1, p2)
    assert round(x, 5) == 392.21726 # 5 digits after decimal point

def test_stations_by_distance():
    stations = build_station_list()
    point = (52.2053, 0.1218)
    stations_distance_list = stations_by_distance(stations, point)
    assert len(stations_distance_list) == len(stations)
    for i in range(len(stations) -1):
        assert stations_distance_list[i][0] in stations
        assert stations_distance_list[i][1] <= stations_distance_list[i+1][1]

def test_stations_within_range():
    stations = build_station_list()
    point = (52.2053, 0.1218) # Cambridge, as known number of stations nearby
    distance = 10 #km
    stations_near = stations_within_radius(stations, point, distance)
    assert len(stations_near) == 11 # from representative output in 1C. If this test in particular fails, check the data was not corrupted.
    for station in stations_near:
        assert station in stations
        assert distance_between_coords(station.coord, point) <= 10

def test_stations_by_river():
    stations = sample_stations()
    
    #Check correct result is returned for sample data for first function
    sample_rivers_with_station = rivers_with_station(stations)
    assert "River Parrett" in sample_rivers_with_station 
    assert "River Glen" in sample_rivers_with_station
    assert "River Dikler" in sample_rivers_with_station
    assert len(sample_rivers_with_station) == 3

    #Check correct result is returned for sample data for second function
    assert "Surfleet Sluice" in stations_by_river(stations)["River Glen"]
    assert "Bourton Dickler" in stations_by_river(stations)["River Dikler"]

    #Check lengths of returned lists is correct
    assert len(stations_by_river(stations)["River Parrett"]) == 1
    assert len(stations_by_river(stations)["River Glen"]) == 2



def test_rivers_by_station_number():
    stations = sample_stations()

    #Check an integer is returned for first function
    assert isinstance(sum_station_number("River Glen", stations), int) == True
    assert isinstance(sum_station_number("River Dikler", stations), int) == True
    assert sum_station_number("River Glen", stations) == 2
    assert sum_station_number("River Parrett", stations) == 1

    #print(rivers_by_station_number(stations, 1))
    

if __name__ == "__main__":
    test_stations_by_river()
    test_rivers_by_station_number()