from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from libdw import pyrebase

# Set the window size for Kivy
Window.size = (360, 640)

#---------------------------- Firebase Codes ---------------------------------#
# URL to Firebase Database
url = 'https://dw-project-d22fe.firebaseio.com/'

# Unique token used for authentication
apikey = 'AIzaSyCwGVwAcf2XLeRtMd1sbgt3NlNxPVmIc0E'

config = {
    "apiKey": apikey,
    "databaseURL": url,
}

'''
Create a firebase object by specifying the URL of the database and its secret
token. The firebase object has functions put and get, that allows user to put
data onto the database and also retrieve data from the database.
'''

firebase = pyrebase.initialize_app(config)
db = firebase.database()


class MainScreen(FloatLayout):
    '''
    This class contains all the widgets of the app and all the methods used
    to operate the app.
    '''
    
    # List of attributes that will be updated
    weather_condition = "Cloudy"
    current_temperature = "25\u00B0C | 33\u00B0C"
    window_condition = "Closed"
     
    is_it_raining = False
      
    # Refresh is the update function/get the current data of the weather
    def refresh(self, **kwargs):
        '''
        This function gets required data from the firebase and will update
        the text attribute from labels in the GUI to match current condition
        of window and weather.
        '''
        
        #--------------------- Getting data from firebase --------------------#
        fcast = db.child("forecasts").child("forecast").child("0")

        # Getting weather condition from firebase
        self.weather_condition = fcast.child("weather").get().val()
        
        # Getting temperature from firebase
        max_t = fcast.child("temperature").child("high").get().val()
        min_t = fcast.child("temperature").child("low").get().val()

        # Accessing user data from firebase
        user = db.child('users').child('user').child('0')

        # Getting rain sensor data from firebase
        rain = user.child('raining').get().val()
        

        # Window condition
        self.window_condition = user.child('window').get().val()


        #-------------------- Updating the text labels -----------------------#
        
        # Update temperature label
        self.current_temperature = "{}\u00B0C | {}\u00B0C".format(max_t,min_t)

        # Updating Weather Conditions data
        # File names: Sunny.png, Rain.png, Thunderstorm.png, Cloudy.png
        if self.weather_condition == "Sunny":
            self.ids['weatherpic'].source = 'Sunny.png'
            self.ids['weather'].text ='Sunny'
            self.ids['temperature'].text = self.current_temperature
            
        elif self.weather_condition == "Thunderstorm":
            self.ids['weatherpic'].source = 'Thunderstorm.png'
            self.ids['weather'].text = 'Thunderstorm'
            self.ids['temperature'].text = self.current_temperature
            
        elif self.weather_condition == "Cloudy":
            self.ids['weatherpic'].source = 'Cloudy.png'
            self.ids['weather'].text = 'Cloudy'
            self.ids['temperature'].text = self.current_temperature
            
        elif self.weather_condition == 'Rain':
            self.ids['weatherpic'].source = 'Rain.png'
            self.ids['weather'].text = 'Rain'
            self.ids['temperature'].text = self.current_temperature
        
        # Updating label for data from rain sensor (raining or not)
        if rain == "Yes":
            self.ids['rainsensor'].text = "It's raining!"

        else:
            self.ids['rainsensor'].text = "No water detected"

        # Update text on window condition
        self.ids['windowcond'].text = self.window_condition
    
    def open_window(self):
        '''
        This function will tell thymio to open the window through firebase
        '''

        user = db.child('users').child('user').child('0')
        print("Thymio, open the window please!")
        
        # Changed the firebase child thymio to 'No' to make it open the window
        db.child('thymio').set('No')
        
        # Update the firebase and tell that the window is open
        user.child('window').set("Open")
        self.refresh()

    def close_window(self):
        '''
        This function will tell thymio to open the window through firebase
        '''

        user = db.child('users').child('user').child('0')
        print("Thymio, close the window please!")

        # Changed the firebase child thymio to 'Yes' to make it close the window
        db.child('thymio').set('Yes')

        # Update the firebase and tell that the window is closed
        user.child('window').set("Closed")
        self.refresh()


class ImageButton(ButtonBehavior, Image):
    # A custom widget which takes the behaviour of button and image
    pass


class MyApp(App):
    def build(self):
        # This function creates an object of MainScreen class and returns it
        screen = MainScreen()
        # Refresh function is now called every 2 mins
        Clock.schedule_interval(screen.refresh,120) 
        return screen


#Running the App
if __name__ == '__main__':
    MyApp().run()