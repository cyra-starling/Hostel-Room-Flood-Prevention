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
#Set the window size
Window.size = (360, 640)

#------------------------- Firebase Codes -------------------------------#
url = 'https://dw-project-d22fe.firebaseio.com/'  # URL to Firebase database
apikey = 'AIzaSyCwGVwAcf2XLeRtMd1sbgt3NlNxPVmIc0E'  # unique token used for authentication

config = {
    "apiKey": apikey,
    "databaseURL": url,
}

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()
#------------------------- Firebase Codes -------------------------------#

class MainScreen(FloatLayout):
    #List of data
    weather_condition = "Cloudy"
    current_temperature = "25\u00B0C | 33\u00B0C"
    window_condition = "Closed"
     
    is_it_raining = False
      
    #refresh is the update function/get the current data of the weather
    def refresh(self):
        
        #Weather Condition
        self.weather_condition = db.child("forecasts").child("forecast").child("0").child("weather").get().val()
        
        #Temperature
        max_temp = db.child("forecasts").child("forecast").child("0").child("temperature").child("high").get().val()
        min_temp = db.child("forecasts").child("forecast").child("0").child("temperature").child("low").get().val()
        
        self.current_temperature = "{}\u00B0C | {}\u00B0C".format(max_temp,min_temp)
        
        ##################################
        #             Update             #
        #            Function            #
        #              Here              #
        ##################################
        print ("refresh button is pressed")
        
        #Keywords: Sunny.png, Rain.png, Thunderstorm.png, Cloudy.png
        #Updating Weather Conditions data
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

    def button_enabler(self,dt):
        if self.is_it_raining == True and self.window_condition == "Open":
            self.ids['closebutton'].disabled = False
            self.ids['closebutton'].background_color = 1,1,1,1
            self.ids['closebutton'].color = 1,1,1,1
            Clock.unschedule(self.button_enabler)
            Clock.schedule_interval(self.button_disabler,1)
    
    def button_disabler(self,dt):
        if self.is_it_raining == False or self.window_condition == "Closed":
            self.ids['closebutton'].disabled = True
            self.ids['closebutton'].background_color = 0,0,0,0
            self.ids['closebutton'].color = 0,0,0,0
            Clock.unschedule(self.button_disabler)
            Clock.schedule_interval(self.button_enabler,1)

    def close_window(self):
        print("Thymio, close the window please!")
        ##################################
        #             Thymio             #
        #             Command            #
        #              Here              #
        ##################################
        
#        Remember to add in the Python commands to disable the button once it has been closed


class ImageButton(ButtonBehavior, Image):
    #A custom widget which takes the behaviour of button and image = image button
    pass

class MyApp(App):
    def build(self):
        screen = MainScreen()
        Clock.schedule_interval(screen.button_enabler,1)
        Clock.schedule_interval(screen.refresh,120) #Refresh function is now called every 2 mins
        return screen
    
#Running the App
if __name__ == '__main__':
    MyApp().run()