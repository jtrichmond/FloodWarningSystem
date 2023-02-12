# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from math import trunc
from .utils import sorted_by_key, sorted_by_property  # noqa
from .station import MonitoringStation
from haversine import haversine # added to pythonapp.yml as dependency

def stations_by_distance(stations: list[MonitoringStation], p: tuple[float, float]) -> list[tuple[MonitoringStation, float]]:
    """Returns a list of stations and their respective distances to the point at the coordinates of p.
    The returned list is sorted by distance, in ascending order."""
    #utils allows sort by key
    station_distance_list = []
    for station in stations:
        #Create tuple
        distance = distance_between_coords(station.coord, p)
        station_distance_list.append((station, distance))

    station_distance_list = sorted_by_key(station_distance_list, 1)
    return station_distance_list

def distance_between_coords(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Returns the distance between the points given by the coords of p1 and p2, using the Haversine formula from the haversine library.
    Units of kilometres"""
    return haversine(p1, p2)

def stations_within_radius(stations: list[MonitoringStation], centre: tuple[float,float], r: float) -> list[MonitoringStation]:
    """Returns a list of all stations from the input list that are within the given radius r from the given point centre, 
    including those exactly at that distance"""
    station_distance_list = stations_by_distance(stations, centre)

    #Binary search for the station that is the furthest away whilst still in range
    index_of_furthest_in_range = 0
    start, end = 0, len(station_distance_list) - 1
    while start <= end:
        mid = trunc((start + end)/2) # note that it rounds down
        if station_distance_list[mid][1] <= r:
            if mid > index_of_furthest_in_range:
                index_of_furthest_in_range = mid
            start = mid + 1
        else:
            end = mid - 1

    return [station_distance_list[i][0] for i in range(index_of_furthest_in_range + 1)]



def rivers_with_station(stations: list[MonitoringStation]) -> set:
    """Returns a set of rivers with monitoring stations"""
    
    #Create empty set
    set_of_rivers_with_station = set()
    
    #Add all rivers with stations to the set
    for station in stations:
        set_of_rivers_with_station.add(station.river)

    #Return completed set
    return set_of_rivers_with_station



def stations_on_given_river(river_name: str, stations: list[MonitoringStation]) -> list[MonitoringStation]:
    """Creates a list of all the stations on a given river
    returns station objects
    list sorted alphabetically by station name"""
    
    #Create empty list
    list_of_required_stations = []

    #Add all stations from given river to the list
    list_of_required_stations = list(filter(lambda station: station.river == river_name, stations))
    return sorted_by_property(list_of_required_stations, "name")



def stations_by_river(stations: list[MonitoringStation]) -> dict:
    """Returns a dictionary that maps river names to a list of station objects on that river"""

    dict_of_stations_by_river = {}
    list_of_rivers = list(rivers_with_station(stations))
    for river in list_of_rivers:
        dict_of_stations_by_river[river] = stations_on_given_river(river, stations)

    return dict_of_stations_by_river

def sum_station_number(river_name, stations: list[MonitoringStation]):
    """Sums number of stations on a required river"""

    #Create a variable, number of stations, value 0
    number_of_stations = 0

    #Count number of stations on required river
    for station in stations:
        if station.river == river_name:
            number_of_stations += 1

    #Returns number of stations on required river
    return number_of_stations


def rivers_by_station_number(stations: list[MonitoringStation], N):
    """Returns a list of (river name, number of stations) tuples, sorted by number of stations"""
     
    if N > len(rivers_with_station(stations)): 
        raise Exception("N is greater than number of stations")

    #Create empty list
    list_rivers_by_station_number = []

    #Adds tuples of (river name, number of stations) to list for every river
    for river in rivers_with_station(stations):
        list_rivers_by_station_number.append((river, sum_station_number(river, stations)))

    #Sorts list of tuples by their second element, in reverse order
    list_rivers_by_station_number.sort(key=lambda a:a[1], reverse = True)


    flag = False
    while flag == False and N < len(rivers_with_station(stations)):
        if list_rivers_by_station_number[N-1][1] == list_rivers_by_station_number[N][1]:
            N += 1
        else: flag = True
    
    return list_rivers_by_station_number[:N]