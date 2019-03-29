from kivy.app import App
from kivy.uix.widget import Widget

class MainScreen(Widget):
    pass

class MyApp(App):

    def build(self):
        return MainScreen()


#Running the App
if __name__ == '__main__':
    MyApp().run()