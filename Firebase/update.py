import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import datetime

cred = credentials.Certificate("../keys/dw-project.json")
# Not Included
firebase_admin.initialize_app(cred, {'databaseURL': 'https://dw-project-d22fe.firebaseio.com/'})

ref = db.reference()

users_ref = ref.child()

'''
Firebase Database Structure

dic = {
    'users': {
        'user':
            [
                {"id": 1, "window": "closed", "raining":"Yes"},
                {"id": 2, "window": "closed", "raining":"No"}
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

users_ref.set(dic)
print(users_ref.get())
'''

# - - - -


class WeatherData:
    def __init__(self):
        self._response = self.weatherapi_get()

    def get_weather(self):
        return self._response

    def api_call(self):

        string = str(datetime.datetime.now())
        datevalues = string.split()
        dateparam = datevalues[0]
        time24hrs = datevalues[1].split(".")[0]

        finalDate = f"{dateparam}T{time24hrs}"

        weatherurl = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast'
        data = {'date_time': finalDate}
        weatherresponse = requests.get(weatherurl, params=data)
        weatherjson = weatherresponse.json()

        temperatureurl = 'https://api.data.gov.sg/v1/environment/24-hour-weather-forecast'

        temperatureresponse = requests.get(temperatureurl,params=data)
        temperaturejson = temperatureresponse.json()

        return [weatherjson, temperaturejson]

    def weatherapi_get(self):
        json = self.api_call()
        response = []

        for item in json[0]['items'][0]['forecasts']:
            if item['area'] == 'Changi':
                response.append(item['forecast'])

        a = json[1]['items'][0]['general']['temperature']

        for item in a:
            response.append(a[item])

        return response

    weather = property(get_weather)


currentWeather = WeatherData()
print(currentWeather.weather)

# Refresh function: currentWeather.weatherapi_get()
# Returns a list of [ weatherstatus, mintemp, maxtemp ]
# To set the text of respective labels in kivy, reference using id, with a new function
