"""Module contains functions for displaying data as graphs"""
from .station import *
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def plot_water_levels(station: MonitoringStation, dates: list[datetime], levels: list[float]):
    plt.plot(dates, levels, 'bx--') # plots dates on x, levels on y, blue dashed line with crosses at data points
    plt.xlabel("Date")
    plt.ylabel("Water level / m")
    plt.title(station.name)
    plt.xticks(rotation=45)

    plt.tight_layout() # Makes sure plot doesn't cut off date labels
    plt.show()