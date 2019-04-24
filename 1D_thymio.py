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

# Create a firebase object by specifying the URL of the database and its secret
# token.
# The firebase object has functions put and get, that allows user to put data
# onto the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True:
    # Create a robot object
    robot = ThymioReal()

    # Check the value of database child 'thymio' in the database at an interval
    # of 0.5 seconds. Continue checking as long as the value is 'None'.
    water_list = db.child("thymio").get()
    water_value = str(water_list.val())

    if water_value == "None":
        time.sleep(0.5)

    else:
        # If value is 'Yes', the program moves the robot to close the window.
        # 'forward' movement => robot.wheels(100, 100)
        if water_value == "Yes":
            robot.wheels(100, 100)
        # If 'No', the robot moves to open the window.
        # 'backward' movement => robot.wheels(-100, -100)
        elif water_value == "No":
            robot.wheels(-100, -100)

        # The robot moves for 3 seconds and is terminated.
        robot.sleep(3)
        robot.quit()

        # Reset the value of the database child to 'None'
        db.child("thymio").set("None")
