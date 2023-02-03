# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *
from trialdata import sample_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    stations = sample_stations()
    if __name__ == "__main__":
        for station in stations:
            print(station.typical_range)
            print(station.typical_range_consistent())

    for station in stations:
        assert station.typical_range_consistent() is True

    
    # Create a station with inconsistent level data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (10,0)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.typical_range_consistent() is False
    s = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    assert s.typical_range_consistent() is False

if __name__ == "__main__":
    test_typical_range_consistent()
