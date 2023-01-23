# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def get_station_id(self) -> str:
        """returns station id"""
        return self.station_id

    def get_measure_id(self) -> str:
        """returns measure id of station"""
        return self.measure_id

    def get_name(self) -> str:
        """returns name of station"""
        return self.name

    def get_coord(self) -> tuple[float, float]:
        """returns the station's coordinates"""
        return self.coord

    def get_typical_range(self) -> tuple[float, float]:
        """returns the typical water level range of the station"""
        return self.typical_range

    def get_river(self) -> str:
        """Returns the river on which the station is located"""
        return self.river

    def get_town(self) -> str:
        """returns the closest town to the station"""
        return self.town

    

