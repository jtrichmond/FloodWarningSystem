import datetime
from floodsystem.analysis import polyfit

def test_polyfit():
    time_now = datetime.datetime.today()
    print(time_now)
    number_of_days = 10
    x = []
    for i in range (0,number_of_days):
        x.append(time_now - datetime.timedelta(days = i))
    print(x)
    y2 = [0, 1, 4, 9, 25, 36, 49, 64, 81, 100]
    y3 = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

    poly = polyfit(x, y3, 3)
    
    print(poly) 

if __name__ == "__main__":
    test_polyfit()