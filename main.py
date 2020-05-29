from modules.bankholiday import bankholiday
from modules.weather import weather
from datetime import datetime
from decimal import Decimal


def exercise1(bh=None, w=None):
    try: 
        cityName = input("Which city do you wan to check ?\n")
        
        locations = bh.getLocations()
        location = input("Choose the region associate with your " + cityName + " city: " + str(locations) + ":\n")
        if location not in locations:
            raise ValueError("The region " + location + " is not supported")

        year = input("Which year do you want to check? ['YYYY']\n")
        datetime.strptime(year, '%Y')

        events = bh.getEventsNameByLocation(year=year,location=location)
        eventName = input("Choose a specific bank holiday: " + str(events) + ":\n")
        if eventName not in events:
            raise ValueError("The event " + eventName + " is not supported")

        dates = bh.getEventsDateByNameAndLocation(year=year,location=location,name=eventName)

        for date in dates:
            data = w.getTemperature(city=cityName,date=date)

    except Exception:
        raise

    print(
        "This is the Hight/Low temperature for " + data["city"] + " city at " + data["date"] + 
        "\nHight: " + str(data["high"]) +
        "\nLow: " + str(data["low"])
    )


def exercise2(bh=None, w=None):
    try: 
        cityName = input("Which city do you wan to check ?\n")
        
        locations = bh.getLocations()
        location = input("Choose the region associate with your " + cityName + " city: " + str(locations) + ":\n")
        if location not in locations:
            raise ValueError("The region " + location + " is not supported")


        events = bh.getEventsNameByLocation(year=None,location=location)
        eventName = input("Choose a specific bank holiday: " + str(events) + ":\n")
        if eventName not in events:
            raise ValueError("The event " + eventName + " is not supported")

        dates = bh.getEventsDateByNameAndLocation(year=None,location=location,name=eventName)
        dates.sort()
        
        rsp = { "high": None ,"date": None }
        for date in dates:
            data = w.getTemperature(city=cityName,date=date)
            if data is None:
                continue

            if rsp["high"] is None or data["high"] > rsp["high"]:
                rsp["high"] = data["high"]
                rsp["date"] = data["date"]

    except Exception:
        raise

    print("The highest temperature registered for " + eventName + " in " + cityName + " city is " + str(rsp["high"]) + ", register in " + str(rsp["date"]))


def main():   
    bankholidayData = bankholiday.BankHoliday()
    weatherData = weather.Weather()

    rsp = input("Which exercide do yo want to test [1,2] ?\n")
    if rsp == str(1):
        exercise1(bh=bankholidayData ,w=weatherData)
    elif rsp == str(2):
        exercise2(bh=bankholidayData ,w=weatherData)
    else:
        raise ValueError("This value is not supported")

if __name__ == "__main__":
    main()