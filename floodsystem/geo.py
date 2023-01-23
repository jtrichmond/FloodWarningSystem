# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from math import sqrt # for distances

def stations_by_distance(stations: list[MonitoringStation], p: tuple[float, float]) -> list[tuple[MonitoringStation, float]]:
    """Returns a list of stations and their respective distances to the point at the coordinates of p.
    The returned list is sorted by distance, in ascending order."""
    #Using insertion sort style, could be more efficient if a quick or merge sort were used.
    station_distance_list = []
    for station in stations:
        #Create tuple
        coord = station.get_coord()
        distance = distance_between_coords(coord, p)
        station_distance_tuple = (station, distance)
        #insert into list
        flag = False #true when index of a distance in the list less than or equal to current distance is found
        i = 0
        while not flag and i < len(station_distance_list):
            if distance <= station_distance_list[i][1]:
                flag = True
                station_distance_list.insert(i, station_distance_tuple)
            else:
                i+=1

        if flag == False:
            station_distance_list.append(station_distance_tuple)
        else:
            raise Exception("Tuple was not inserted into the list, even though the flag was raised")

        return station_distance_list

def distance_between_coords(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Returns the distance between the points given by the coords of p1 and p2"""
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2)
