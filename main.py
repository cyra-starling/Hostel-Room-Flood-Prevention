from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivy.core.window import Window

#Set the window size
Window.size = (600, 600)


class MainScreen(FloatLayout):
    #refresh is the update function
    def refresh(self):
        ##################################
        #             Update             #
        #            Function            #
        #              Here              #
        ##################################
        print ("refresh button is pressed")
        #Things to update:
        weather = "Sunny"
        temperature = 30
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