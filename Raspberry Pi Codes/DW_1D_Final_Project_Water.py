# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 2019
Last Updated on Thu Apr 25 2019

@author: Anthony Wong, Amanda Kosim, Lee Jia Le, Mridula Ratheesh,
         Ng Ming Hao Kenny

DW 1D RasPi Code for water sensor
"""


from time import sleep
from libdw import pyrebase
import RPi.GPIO as GPIO

# Link firebase via pyrebase.
url = "https://dw-project-d22fe.firebaseio.com/"
apikey = "AIzaSyCwGVwAcf2XLeRtMd1sbgt3NlNxPVmIc0E"

config = {
    "apiKey": apikey,
    "databaseURL": url,
    }

fb = pyrebase.initialize_app(config)
data = fb.database()

def check_rain(channel):
    '''This function checks whether it's raining or not using water sensor
    '''
    # Check sensor inputs: High indicates no rain
    if GPIO.input(channel) == GPIO.HIGH:
        String = "No"
        
    else:
        String = "Yes"

    return String

# Infinite loop creation to continually sense for changes.
while True:
    # Pin setup for water sensor.
    GPIO.setmode(GPIO.BOARD)
    PIN_RAIN = 12
    GPIO.setup(PIN_RAIN, GPIO.IN)

    # Get data from firebase
    rain_stat = data.child("users/user/0/raining").get()
    
    # Check status from water sensor
    print("is it raining?")
    status = check_rain(PIN_RAIN)
    print(status)
    
    # Change weather status in firebase if it doesn't match the sensor
    if rain_stat.val() != status:
        raining_ref = data.child("users/user/0/raining")
        raining_ref.set(status)
    
    GPIO.cleanup()
    sleep(5)