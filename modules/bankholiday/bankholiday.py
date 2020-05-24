import requests
from datetime import datetime

class BankHoliday(object):
    
    source_url = 'https://www.gov.uk/bank-holidays.json'

    def __init__(self):
        try:
            data = requests.get(self.source_url).json()
            
        except (requests.RequestException, ValueError):
            raise

        self.data = []
        for d in data:
            self.data.append(data.get(d))

    def getLocations(self):
        locations = []
        
        for d in self.data:
            locations.append(d["division"])
        return locations

    def getEventsNameByLocation(self,year=None,location=None):
        events = []
        
        for d in self.data:
            if d["division"] != location:
                pass

            for dd in d["events"]:
                v = datetime.strptime(dd["date"], "%Y-%m-%d")
                if (year is None or year == str(v.year)) and dd["title"] not in events:
                    events.append(dd["title"])
        return events

    def getEventsDateByNameAndLocation(self,year=None,location=None,name=None):
        dates = []
        
        for d in self.data:
            if d["division"] != location:
                pass
        
            for dd in d["events"]:
                v = datetime.strptime(dd["date"], "%Y-%m-%d")
                if (year is None or year == str(v.year)) and name == dd["title"] and v not in dates:
                    dates.append(v)
        return dates