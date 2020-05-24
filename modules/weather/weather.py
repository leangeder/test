import requests
import datetime

class Weather(object):
    
    source_url = 'https://www.metaweather.com/api/location/'

    def __init__(self):
        return None

    def getWoeid(self,city):
        woeid = None

        try:
            if city != None:
                data = requests.get(self.source_url + 'search/?query=' + city).json()
        except (requests.RequestException, ValueError):
            raise

        if len(data) == 1:
            woeid = data[0]["woeid"]
        return woeid

    def getTemperature(self ,city ,date ):
        temperature = None

        if city is None or date is None:
            return temperature

        woied = self.getWoeid(city)

        try:
            data = requests.get(self.source_url + str(woied) + date.strftime("/%Y/%m/%d/")).json()
        except (requests.RequestException, ValueError):
            raise

        for d in data:
            temperature = { 'city': city, 'date': str(date), 'low': d["min_temp"], 'high': d["max_temp"] }

        return temperature