#import matplotlib
#import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels


def plot_water_levels(station, dates, levels):
    
    fetch_measure_levels(station.measure_id, 10)
    time = []
    water_level = []

    return fetch_measure_levels(station.measure_id, dates)