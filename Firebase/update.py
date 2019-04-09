import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import datetime

cred = credentials.Certificate("../keys/dw-project.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://dw-project-d22fe.firebaseio.com/'})

ref = db.reference()

users_ref = ref.child('test')
'''
a = dict({
    "items":
        {
            "item":
                [
                    {
                        "id": "0001",
                        "type": "donut",
                        "name": "Cake",
                        "ppu": 0.55,
                        "batters":
                            {
                                "batter":
                                    [
                                        {"id": "1001", "type": "Regular"},
                                        {"id": "1002", "type": "Chocolate"},
                                        {"id": "1003", "type": "Blueberry"},
                                        {"id": "1004", "type": "Devil's Food"}
                                    ]
                            },
                        "topping":
                            [
                                {"id": "5001", "type": "None"},
                                {"id": "5002", "type": "Glazed"},
                                {"id": "5005", "type": "Sugar"},
                                {"id": "5007", "type": "Powdered Sugar"},
                                {"id": "5006", "type": "Chocolate with Sprinkles"},
                                {"id": "5003", "type": "Chocolate"},
                                {"id": "5004", "type": "Maple"}
                            ]
                    }
                ]
        }

})

users_ref.set(a)

print(users_ref.get())
'''
# - - - -


class WeatherData:
    def __init__(self):
        self._response = self.weather_get()

    def get_weather(self):
        return self._response

    def api_call(self):

        string = str(datetime.datetime.now())
        datevalues = string.split()
        dateparam = datevalues[0]
        time24hrs = datevalues[1].split(".")[0]

        finalDate = f"{dateparam}T{time24hrs}"

        url = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast'
        data = {'date_time': finalDate}
        response = requests.get(url, params=data)
        json = response.json()

        return json

    def weather_get(self):
        json = self.api_call()

        for item in json['items'][0]['forecasts']:
            if item['area'] == 'Changi':
                return item['forecast']
    weather = property(get_weather)


currentWeather = WeatherData()
print(currentWeather.weather)
