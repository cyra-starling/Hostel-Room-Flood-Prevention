import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class MainScreen(BoxLayout):
    pass

class MyApp(App):

    def build(self):
        return MainScreen()


#Running the App
if __name__ == '__main__':
    MyApp().run()