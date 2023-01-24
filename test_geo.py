from floodsystem.geo import *

"""Unit test for the geo module"""

def test_distance_between_coords():
    #using example from haversine docs
    p1 = (45.7597, 4.8422)
    p2 = (48.8567, 2.3508)
    x =  distance_between_coords(p1, p2)
    assert round(x, 5) == 392.21725 # 5 digits after decimal point

