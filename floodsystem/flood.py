from .station import MonitoringStation
from floodsystem.stationdata import update_water_levels

def stations_highest_rel_level(stations, N):
    """returns a list of the N stations (objects) at which the water level, 
    relative to the typical range, is highest"""
    
    #If N is greater than the number of stations, raise an error
    if N > len(stations):  
        raise Exception("N is greater than number of stations")

    #Update Water Levels
    update_water_levels(stations)

    #Create an empty list
    list_stations_highest_rel_level = []

    #Add a list of tuples to the list, (station.name, relative level)
    for station in stations:
        if station.typical_range != None and station.latest_level != None:
            list_stations_highest_rel_level += [(station.name, station.latest_level/station.typical_range[1])]

    #Order list
    list_stations_highest_rel_level.sort(key=lambda a:a[1], reverse = True)

    #Return first N items from list
    return list_stations_highest_rel_level[:N]
     