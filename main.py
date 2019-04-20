from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.clock import Clock
#Set the window size
Window.size = (360, 640)


class MainScreen(FloatLayout):
    #List of data
    weather_condition = "Cloudy"
    current_temperature = "25\u00B0C | 33\u00B0C"
    window_condition = "Closed"
    
    weatherpic = ObjectProperty(None)
    weather = ObjectProperty(None)
    temperature = ObjectProperty(None)
    
    is_it_raining = False

    #refresh is the update function
    def refresh(self, dt):
        ##################################
        #             Update             #
        #            Function            #
        #              Here              #
        ##################################
        print ("refresh button is pressed")
        
        #Keywords: Sunny.png, Rain.png, Thunderstorm.png, Cloudy.png
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