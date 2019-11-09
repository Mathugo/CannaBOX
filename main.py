from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('Screen.kv')

def loadFonts():
    LabelBase.register(name="QuickSand",
        fn_regular="fonts/Quicksand-Regular.otf",
        fn_bold="fonts/QuickSand-Bold.otf"
    )
    LabelBase.register(name="Cantarell",
        fn_regular="fonts/Cantarell-Regular.ttf",
        fn_bold="fonts/Cantarell-Bold.ttf"
    )
    LabelBase.register(name="OpenSans",
        fn_regular="fonts/OpenSans-Regular.ttf",
        fn_bold="fonts/OpenSans-Bold.ttf"
    )
    LabelBase.register(name="Amble",
        fn_regular="fonts/Amble-Regular.ttf",
        fn_bold="fonts/Amble-Bold.ttf"
    )



class StartScreen(Screen):
    pass
class MenuScreen(Screen):
    pass


class RootScreen(ScreenManager):
    pass

class CircularProgressBar(ProgressBar):
    pass

sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(MenuScreen(name='menu'))

class MainApp(App):
    def build(self):
        return sm

#    def build(self):
#        return RootScreen()

if __name__ == '__main__':
    #sm = ScreenManager()
    #sm.add_widget(StartScreen(name='start'))
    #sm.add_widget(MenuScreen(name='menu'))
    loadFonts()
    Window.fullscreen = 'auto'
    MainApp().run()
