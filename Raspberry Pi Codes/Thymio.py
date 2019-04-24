from pythymiodw import *
from time import sleep
from libdw import pyrebase

# URL to Firebase database
url = 'https://dw-project-d22fe.firebaseio.com/'

# Unique token used for authentication
apikey = 'AIzaSyCwGVwAcf2XLeRtMd1sbgt3NlNxPVmIc0E'

config = {
    "apiKey": apikey,
    "databaseURL": url,
}

'''
Create a firebase object by specifying the URL of the database 
and its secret token. The firebase object has functions put and get,
that allows user to put data onto the database and also retrieve data
from the database.
'''
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Create a robot object
robot = ThymioReal()

while True:
    '''
    Check the value of database child 'thymio' in the database at an interval
    of 0.5 seconds. Continue checking as long as the value is 'None'.
    '''
    user = db.child("users").child("user").child("0")
    water_list = user.child("thymio").get()
    water_value = str(water_list.val())

    # If 'None', don't do anything
    if water_value == "None":
        time.sleep(0.5)

    else:
        # If 'Yes', the program moves the robot forward to close the window.
        if water_value == "Yes":
            robot.wheels(100, 100)
            user = db.child("users").child("user").child("0")
            user.child("thymio").set("None")

        # If 'No', the robot moves back to open the window.
        elif water_value == "No":
            robot.wheels(-100, -100)
            user = db.child("users").child("user").child("0")
            user.child("thymio").set("None")

        # The robot moves for 3 seconds and is terminated.
        robot.sleep(3)
        robot.wheels(0,0)        