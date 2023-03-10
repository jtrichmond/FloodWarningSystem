# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *
from trialdata import sample_stations, create_invalid_typical_range_stations, create_invalid_relative_level_stations


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

    
    
    stations = create_invalid_typical_range_stations()
    for station in stations:
        assert station.typical_range_consistent() is False



def test_inconsistent_range_stations():
    valid = sample_stations()
    invalid = create_invalid_typical_range_stations()

    stations = valid + invalid

    assert inconsistent_typical_range_stations(stations) == invalid

def test_relative_water_level():
    valid = sample_stations()
    invalid = create_invalid_relative_level_stations()
    stations = valid + invalid
    for station in stations:
        if __name__ == "__main__":
                print(station.name, station.relative_water_level())
        if station in valid and station.latest_level != None:
            assert station.relative_water_level() == (station.latest_level - station.typical_range[0])/(station.typical_range[1] - station.typical_range[0])
        else:
            assert station.relative_water_level() == None

if __name__ == "__main__":
    test_create_monitoring_station()
    test_typical_range_consistent()
    test_relative_water_level()
