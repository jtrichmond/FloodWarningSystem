
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for task 1B"""
    stations = build_station_list()
    point = (52.2053, 0.1218)
    stations_distance_list = stations_by_distance(stations, point)
    outputTuples = []
    for stationPair in stations_distance_list[:10]:
        outputTuples.append((stationPair[0].name, stationPair[0].town, stationPair[1]))
    print(outputTuples)

    outputTuples = []
    for stationPair in stations_distance_list[-10:]:
        outputTuples.append((stationPair[0].name, stationPair[0].town, stationPair[1]))
    print(outputTuples)



if __name__ == "__main__":
    run()
