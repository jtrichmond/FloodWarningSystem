# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from math import sqrt # for distances
from haversine import haversine # need to install locally.

def stations_by_distance(stations: list[MonitoringStation], p: tuple[float, float]) -> list[tuple[MonitoringStation, float]]:
    """Returns a list of stations and their respective distances to the point at the coordinates of p.
    The returned list is sorted by distance, in ascending order."""
    #utils allows sort by key
    station_distance_list = []
    for station in stations:
        #Create tuple
        coord = station.get_coord()
        distance = distance_between_coords(coord, p)
        station_distance_list.append((station, distance))

    sorted_by_key(station_distance_list, 1)
    return station_distance_list

def distance_between_coords(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Returns the distance between the points given by the coords of p1 and p2, using the Haversine formula from the haversine library.
    Units of kilometres"""
    return haversine(p1, p2)
