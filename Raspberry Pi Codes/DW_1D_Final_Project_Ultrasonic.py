# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 2019
Last Updated on Thu Apr 25 2019

@author: Anthony Wong, Amanda Kosim, Lee Jia Le, Mridula Ratheesh,
         Ng Ming Hao Kenny

DW 1D RasPi Code for Ultrasonic Sensor
"""


from time import sleep, time
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

def window_closed(distance):
    '''This function determines whether the window is closed or not based
    on the distance from the sensor which is passed as an argument
    '''
    
    # Conditional statements to determine whether window is closed.
    assert(distance>=0)    
    if float(distance)<=6.3:
        String = "Closed"
        data.child("users/user/0/window").set("Closed")

    elif float(distance)>6.3:
        String = "Open"
        data.child("users/user/0/window").set("Open")
        
    return String

# Infinite loop creation to continuously sense changes
while True:
    GPIO.setmode(GPIO.BOARD)
    # Setup of ultrasonic sensor pins.
    PIN_TRIGGER = 7
    PIN_ECHO = 11
        
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    
    # Let ultrasonic sensor settle for more consistent readings.
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    sleep(2)
    
    # Activating ultrasonic sensor to calculate distance.
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time()
        
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time()

    pulse_duration = (pulse_end_time - pulse_start_time)
    distance = round(pulse_duration * 17150, 2)
    print(distance)
    window_closed(distance)

    GPIO.cleanup()
    sleep(5)