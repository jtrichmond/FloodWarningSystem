# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
from operator import methodcaller # for inconsistent_typical_range_stations


class MonitoringStation:
    """This class represents a river level monitoring station"""
    #Changed to add property decorators for extension task. Effectively read only, unless setter methods added
    #Variable names now have leading underscores to indicate protected status

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self._station_id = station_id
        self._measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = label
        if isinstance(label, list):
            self._name = label[0]

        self._coord = coord
        self._typical_range = typical_range
        self._river = river
        self._town = town

        self._latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    #all read only other than measure id and latest level
    @property
    def station_id(self) -> str:
        """returns station id"""
        return self._station_id

    @property
    def measure_id(self) -> str:
        """returns measure id of station"""
        return self._measure_id

    @property
    def name(self) -> str:
        """returns name of station"""
        return self._name

    @property
    def coord(self) -> tuple[float, float]:
        """returns the station's coordinates"""
        return self._coord

    @property
    def typical_range(self) -> tuple[float, float]:
        """returns the typical water level range of the station"""
        return self._typical_range

    @property
    def river(self) -> str:
        """Returns the river on which the station is located"""
        return self._river

    @property
    def town(self) -> str:
        """returns the closest town to the station"""
        return self._town

    @property
    def latest_level(self): #unsure of type, assuming int or float when not NoneType
        return self._latest_level

    @latest_level.setter
    def latest_level(self, value):
        if not (isinstance(value, (int, float)) or value == None):
            raise TypeError(str(value) + " was not an integer, float, or NoneType, so is not a valid latest_level")
        else:
            self._latest_level = value


    def typical_range_consistent(self) -> bool:
        """Checks the typical high/low range data of the station for consistency 
        (i.e., that data is available and the high level is greater than the low level).
        Returns True if the data is consistent"""
        if self.typical_range is None or self.typical_range[0] > self.typical_range[1]:
            return False
        else:
           return True

def inconsistent_typical_range_stations(stations: list[MonitoringStation]) -> list[MonitoringStation]:
    return filter(methodcaller("typical_range_consistent"), stations)
    

