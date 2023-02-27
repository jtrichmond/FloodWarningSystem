"""Module containing functions for mathematical analysis of data"""
from datetime import datetime
from matplotlib.dates import date2num
import numpy as np

def polyfit(dates: list[datetime], levels: list[float], p: int) -> tuple[np.poly1d, float]:
    """for given dates and corresponding water levels, determines a least squares fit of a polynomial of degree p to water level data
    Returns a polynomial as a np.poly1d object, and any shifting of the date axis used to minimise floating point errors
    A subtraction of time as the shift (i.e. reducing the timestamp value) is taken as a positive shift
    Assumes the dates are in ascending order, oldest first"""
    #change datetime to float
    datenums = date2num(dates)
    # shift values so that earliest is at 0
    shift = datenums[0]
    # generate least-squares polynomial coefficients for levels against shifted data
    p_coeff = np.polyfit(datenums - shift, levels, p)
    #create polynomial object
    poly = np.poly1d(p_coeff)
    return poly, shift


def convert_polynomial_to_level_data(dates: list[datetime], poly: np.poly1d, shift: float) -> list[float]:
    """Converts a polynomial model into water level data for the dates given, using the shift in x value indicated by shift
    Ideally, shift should equal the earliest value in dates, as this is the convention used in polyfit"""
    datenums = date2num(dates)
    shifted_dates = datenums - shift
    #evaluate polynomial for each shifted date, producing list
    levels = [poly(shifted_date) for shifted_date in shifted_dates]
    return levels
