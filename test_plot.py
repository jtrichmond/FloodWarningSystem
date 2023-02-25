from floodsystem.plot import *
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from trialdata import sample_stations
from floodsystem.datafetcher import fetch_measure_levels
import pytest
from datetime import timedelta

def test_plot_water_levels():
    stations = sample_stations()
    update_water_levels(stations)
    
    dt = timedelta(days=10) # time difference of 10 days
    plot_stations = stations_highest_rel_level(stations, 3)

    for station in plot_stations:
        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt)
        except KeyError:
            print("KeyError: Missing historical data for " + station.name)
        else:
            #Check that error is raised for incorret levels input
            with pytest.raises(Exception):
                plot_water_levels(station, dates, [1,2])

            #Check that error is raised for incorret dates input
            with pytest.raises(Exception):
                plot_water_levels(station, ["sunset"], levels)
            
            #Check that error is raised for incorrect station input
            with pytest.raises(Exception):
                plot_water_levels("Waterloo", dates, levels)

            #Check that len(dates) == len(levels) for each station
            assert type(dates) == list
            assert type(levels) == list
            assert len(dates) == len(levels)



def test_plot_water_levels_with_fit():
    stations = sample_stations()
    update_water_levels(stations)
    
    dt = timedelta(days=10) # time difference of 10 days
    plot_stations = stations_highest_rel_level(stations, 3)
    p = 3

    for station in plot_stations:
            try:
                dates, levels = fetch_measure_levels(station.measure_id, dt)
            except KeyError:
                print("KeyError: Missing historical data for " + station.name)
            else:

                #Check that lenghts of lists to be plotted match up
                poly, shift = polyfit(dates, levels, p)
                model_levels = convert_polynomial_to_level_data(dates, poly, shift)
                assert len(dates) == len(model_levels)
                assert len(levels) == len(model_levels)
               
                #Check that length of polynomial equal p
                datenums = date2num(dates)
                shift = datenums[0]
                p_coeff = np.polyfit(datenums - shift, levels, p)
                ploy = np.poly1d(p_coeff)
                assert len(poly) == p

if __name__ == "__main__":
    test_plot_water_levels()
    test_plot_water_levels_with_fit()