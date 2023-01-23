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

def distance_between_coords(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Returns the distance between the points given by the coords of p1 and p2"""
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2)
