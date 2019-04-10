from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
#Set the window size
Window.size = (360, 640)


class MainScreen(FloatLayout):
    #List of data
    weather_condition = "Cloudy"
    current_temperature = "-2\u00B0C"
    window_condition = "Closed"
    
    weatherpic = ObjectProperty(None)
    weather = ObjectProperty(None)
    temperature = ObjectProperty(None)
    
    #refresh is the update function
    def refresh(self):
        ##################################
        #             Update             #
        #            Function            #
        #              Here              #
        ##################################
        print ("refresh button is pressed")
        
        #Updating Weather Conditions data
        if self.weather_condition == "Sunny":
            self.weatherpic.source = 'Sunny.png'
            self.weather.text ='Sunny'
            self.temperature.text = self.current_temperature
            
        elif self.weather_condition == "Thunderstorm":
            self.weatherpic.source = 'Thunderstorm.png'
            self.weather.text = 'Thunderstorm'
            self.temperature.text = self.current_temperature
            
        elif self.weather_condition == "Cloudy":
            self.weatherpic.source = 'Cloudy.png'
            self.weather.text = 'Cloudy'
            self.temperature.text = self.current_temperature
            
        elif self.weather_condition == 'Rain':
            self.weatherpic.source = 'Rain.png'
            self.weather.text = 'Rain'
            self.temperature.text = self.current_temperature
            
        
            
        
        #After this is all the ifs to change the text and image in kivy but idk how yet
        #Keywords: Sunny.png, Rain.png, Thunderstorm.png, Cloudy.png
        #The source that needs to be changed is the image to show the weather (I put a comment)

class ImageButton(ButtonBehavior, Image):
    #Just so that the button can be image lmao  
    pass

class MyApp(App):
    def build(self):
        return MainScreen()
    
#Running the App
if __name__ == '__main__':
    MyApp().run()