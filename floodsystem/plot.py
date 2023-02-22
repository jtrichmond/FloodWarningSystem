"""Module contains functions for displaying data as graphs"""
from .station import *
from datetime import datetime
import matplotlib.pyplot as plt
from numpy import ones
from .analysis import *

def plot_water_levels(station: MonitoringStation, dates: list[datetime], levels: list[float]):
    """Plot the water levels over time for a station, alongside its typical high and low range values"""
    plt.plot(dates, levels, 'bx--', label="water level") # plots dates on x, levels on y, blue dashed line with crosses at data points
    onearray = ones(len(dates))
    if station.typical_range_consistent():
        plt.plot(dates, onearray*station.typical_range[0], label="typical low level")
        plt.plot(dates, onearray*station.typical_range[1], label="typical high level")
    
    plot_setup_and_display(station)


def plot_water_level_with_fit(station: MonitoringStation, dates: list[datetime], levels: list[float], p: int):
    """Plots the actual water level data for the station with the corresponding least-squares fit polynomial model of degree p.
    Will compute the polynomial model, which will have a shift in the dates to minimise floating point errors for large numbers"""
    poly, shift = polyfit(dates, levels, p)
    model_levels = convert_polynomial_to_level_data(dates, poly, shift)
    plt.plot(dates, model_levels, label="least squares regression model")

    plot_water_levels(station, dates, levels)

def plot_setup_and_display(station: MonitoringStation):
    """formats and displays plot"""
    plt.xlabel("Date")
    plt.ylabel("Water level / m")
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout() # Makes sure plot doesn't cut off date labels
    plt.show()