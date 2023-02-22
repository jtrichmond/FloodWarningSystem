from floodsystem.flood import *
from floodsystem.station import *
from trialdata import sample_stations, create_stations_level_over_threshold_data

def test_stations_level_over_threshold():
    stations = create_stations_level_over_threshold_data()
    tol = 0.8
    stations_over_tol = stations_level_over_threshold(stations, tol)
    if __name__ == "__main__":
        for station in stations:
            print(station.name)
        for stationpair in stations_over_tol:
            print(stationpair[0].name)
            print(stationpair[1])


    station_objects_over_tol = [pair[0] for pair in stations_over_tol] # first item in tuple, the station


    for station in stations:
        print(station.name)
        try:
            index = station_objects_over_tol.index(station) # tries to find the index of the station in the over_tol list
        except ValueError:
            pass # station not in list
        else:
            assert station.relative_water_level() == stations_over_tol[index][1] #check values are the same

        if station in station_objects_over_tol:
            assert station.relative_water_level() >= tol
        elif station.relative_water_level() is not None: #Not in list and not None
            assert station.relative_water_level() < tol
        else: #Not in list and None
            assert station.relative_water_level() is None
    
    if len(stations_over_tol) > 1:
        for i in range(len(stations_over_tol) -1):
            assert stations_over_tol[i][1] >= stations_over_tol[i+1][1] # Checks sorted in reverse order

if __name__ == "__main__":
    test_stations_level_over_threshold()
    