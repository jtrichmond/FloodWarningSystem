from .station import MonitoringStation
from .stationdata import update_water_levels
from .utils import sorted_by_key


def stations_level_over_threshold(stations: list[MonitoringStation], tol: float) -> list[tuple[MonitoringStation, float]]:
    """Given a list of monitoring stations and a relative water level fraction (tol), 
    returns a list of tuples containing MonitoringStation objects and their corresponding relative water levels that exceed or equal the tolerance value
    Return list sorted in descending order of relative level"""
    def over_tol(station: MonitoringStation, tol: float) -> bool:
        if station.relative_water_level() is not None:
            return station.relative_water_level() >= tol
        else:
            return False

    #filter the list for stations that have a relative water level over the tolerance. Convert the resulting filter object to a list
    stations_over_tol = list(filter(lambda x: over_tol(x, tol), stations))
    #Generate station: relative level pairs
    stations_over_tol =  [(station, station.relative_water_level()) for station in stations_over_tol]
    #Sort in descending order of relative level and return
    return sorted_by_key(stations_over_tol, 1, True)

def stations_highest_rel_level(stations: list[MonitoringStation], N: int) -> list[MonitoringStation]:
    """returns a list of the N stations (objects) at which the water level, 
    relative to the typical range, is highest
    If the number of stations with a relative level is less than N, all the valid stations will be returned (those without will not be included)"""
    
    #If N is greater than the number of stations, raise an error
    if N > len(stations):  
        raise Exception("N is greater than number of stations")

    #I updated this because I needed it for 2E. 
    """
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
    """
    #Set an arbitrarily small tolerance so that all stations with a relative water level are returned
    c = -9999
    rel_level_station_pairs = stations_level_over_threshold(stations, c)
    if N <= len(rel_level_station_pairs):
        return [rel_level_station_pairs[i][0] for i in range(N)] 
        # produces a list of the N stations in the list with highest rel levels
        #because list sorted in descending order by relative level, no need to re-sort, just use first N items
    else:
        return[stationpair[0] for stationpair in rel_level_station_pairs] # all stations from relative stations.