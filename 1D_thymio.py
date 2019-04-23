from pythymiodw import *
from time import sleep
from libdw import pyrebase


url = 'https://dw-project-d22fe.firebaseio.com/'
# URL to Firebase database
apikey = 'AIzaSyCwGVwAcf2XLeRtMd1sbgt3NlNxPVmIc0E'
# unique token used for authentication

config = {
    "apiKey": apikey,
    "databaseURL": url,
}

# Create a firebase object by specifying the URL of the database
#and its secret token.
# The firebase object has functions put and get, that
#allows user to put data onto
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True:
    # Check the value of water_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the water_list is not in the
    # database (ie. it is None). If water_list is a valid list, the program
    # exits the while loop and controls the robot to move forward to close the
    # window
    robot = ThymioReal()  # create a robot object
    water_list = db.child("thymio").get()
    water_value = str(water_list.val())
    
    if water_value == "None":
        time.sleep(0.5)
    
    else:
        if water_value == "Yes":
            robot.wheels(100, 100)

        elif water_value == "No":
            robot.wheels(-100, -100)
        
        robot.sleep(3)
        robot.quit()
        db.child("thymio").set("None")

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)
