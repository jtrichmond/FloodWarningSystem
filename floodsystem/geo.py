# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from math import trunc
from .utils import sorted_by_key  # noqa
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

