import datetime
from floodsystem.analysis import polyfit

def test_polyfit():
    """checks that the polynomial model produced fits perfect data (i.e. pure quadratic, cubic)"""
    time_now = datetime.datetime.today()
    print(time_now)
    number_of_days = 11 # today through to 10 days ago
    dates = []
    #Generate dates
    for i in range (0,number_of_days):
        dates.append(time_now - datetime.timedelta(days = i))
    dates.reverse() # reverse so that earliest is at index 0

    y2 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    y3 = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    

    poly2, shift2 = polyfit(dates, y2, 4)
    poly3, shift3 = polyfit(dates, y3, 4)
    
    if __name__ == "__main__":
        print(poly2) 
        print(poly3)

    assert round(shift2 - shift3, 6) == 0 # same date range therefore should be shifted by same amount
    #generate values based off polynomial models
    model2 = [poly2(i) for i in range(number_of_days)]
    model3 = [poly3(i) for i in range(number_of_days)]

    for i in range(number_of_days):
        #Check that models conform to data
        assert round(y2[i] - model2[i], 6) == 0
        assert round(y3[i] - model3[i], 6) == 0

if __name__ == "__main__":
    test_polyfit()