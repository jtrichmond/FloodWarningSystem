from .floodsystem.geo import *

"""Unit test for the geo module"""

def test_distance_between_coords():
    p1 = (1,2)
    p2 = (4.0, 6.0)
    assert distance_between_coords(p1, p2) == 5

