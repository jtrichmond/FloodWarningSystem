# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""
#uses operator module for sorting by attributes. this module added to pythonapp.yml
from operator import attrgetter

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def sorted_by_property(x:list, property:str, reverse = False) -> list:
    """Returns a list sorted by the value of the property specified, in ascending order. Can be in reverse order by setting reverse to True"""
    #attrgetter allows multiple levels of sorting. Could expand so that property is a tuple to be unpacked, then use that for multi level sort.
    return sorted(x, key = attrgetter(property), reverse=reverse)