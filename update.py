import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import datetime

cred = credentials.Certificate("dw-project.json")
# .gitignore the JSON credentials
firebase_admin.initialize_app(cred, {'databaseURL': 'https://dw-project-d22fe.firebaseio.com/'})

ref = db.reference()

users_ref = ref.child('users/user/0')
forecasts_ref = ref.child('forecasts/forecast/0')

'''
#Firebase Database Structure

dic = {
    'users': {
        'user':
            [
                {"id": 1, "window": "closed", "raining":"Yes","thymio": "None"},
                {"id": 2, "window": "closed", "raining":"No", "thymio": "None"}
            ]


    },
    "forecasts": {
        "forecast":
            [
                {"region": "Changi", "weather": "Sunny", "temperature": {"low": 24, "high": 36}

                 },
                {"region": "Bedok", "weather": "Rainy", "temperature": {"low": 28, "high": 32}

                 }

            ]
    }

}
'''


class WeatherData:
    def __init__(self):
        self.weatherapi_get()
        # Call get_api function

    def api_call(self, **kwargs):

        string = str(datetime.datetime.now())
        datevalues = string.split()
        dateparam = datevalues[0]
        time24hrs = datevalues[1].split(".")[0]

        finalDate = f"{dateparam}T{time24hrs}"
        # Setup of date-time values to request for API

        weatherurl = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast'
        data = {'date_time': finalDate}
        weatherresponse = requests.get(weatherurl, params=data)
        weatherjson = weatherresponse.json()
        # JSON Response for Weather

        temperatureurl = 'https://api.data.gov.sg/v1/environment/24-hour-weather-forecast'

        temperatureresponse = requests.get(temperatureurl, params=data)
        temperaturejson = temperatureresponse.json()
        # JSON Response for Temperature

        return [weatherjson, temperaturejson]

    def weatherapi_get(self, **kwargs):
        json = self.api_call()
        # Call api from data.gov.sg and returns 2 json files respectively

        weatherjson = json[0]
        temperaturejson = json[1]

        # Access Forecast for Area : "Changi"
        for item in weatherjson['items'][0]['forecasts']:
            if item['area'] == 'Changi':
                weather = item['forecast']

        # Access Temperature for max_temp and min_temp in the day
        high = temperaturejson['items'][0]['general']['temperature']['high']
        low = temperaturejson['items'][0]['general']['temperature']['low']

        # Updates Firebase on the current weather status
        forecasts_ref.update({"region":"Changi","weather":f"{weather}",
                              "temperature": {"low": f"{low}", "high": f"{high}"}})

