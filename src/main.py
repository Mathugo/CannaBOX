from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.uix.screenmanager import FadeTransition, SwapTransition, WipeTransition, SlideTransition
from collections.abc import Iterable
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget

### Import all screen file

from Screens.DashBoard.DashBoard import *
from Screens.Configure.Configure import *
from Screens.Graph.Graph         import *
from Screens.Home.Home           import *
from Screens.Schedule.Schedule   import *
from Screens.Settings.Settings   import *
from Screens.Start.Start         import *
from Screens.Timelapse.Timelapse import *


#### Start UP
Window.size = (1024, 600)
from fonts import loadFonts



class GrowBox(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.sm = ScreenManager(transition=FadeTransition())
        self.loadKvScreens()
        self.loadScreens()
    def build(self):
        #self.sm=sm
        return self.sm

    def remove_dash(self):
        screen = self.sm.current
        try:
            if screen == "home":
                self.home.remove_dash(0)
            elif screen == "graph":
                self.graph.remove_dash(0)
            elif screen == "schedule":
                self.schedule.remove_dash(0)
            elif screen == "timelapse":
                self.timelapse.remove_dash(0)
            elif screen == "settings":
                self.settings.remove_dash(0)
        except:
            pass

    def loadScreens(self):

        self.start= StartScreen(name='start')
        self.start.setSm(self.sm)
        self.configure=ConfigureScreen(name='configure')
        self.home=HomeScreen(name='home',img="../assets/Home/menu_home.png")
        self.graph=GraphScreen(name='graph',img="../assets/Graph/menu_graph.png")
        self.schedule=ScheduleScreen(name='schedule',img="../assets/Schedule/menu_schedule.png")
        self.timelapse=TimelapseScreen(name='timelapse',img="../assets/Timelapse/menu_timelapse.png")
        self.settings=SettingsScreen(name='settings',img="../assets/Settings/menu_settings.png")

        self.sm.add_widget(self.start)
        self.sm.add_widget(self.configure)
        self.sm.add_widget(self.home)
        self.sm.add_widget(self.graph)
        self.sm.add_widget(self.schedule)
        self.sm.add_widget(self.timelapse)
        self.sm.add_widget(self.settings)

    def loadKvScreens(self):
        Builder.load_file('Screens/Start/StartScreen.kv')
        Builder.load_file('Screens/DashBoard/DashBoard.kv')
        Builder.load_file('Screens/DashBoard/DashBoardScreen.kv')
        Builder.load_file('Screens/Home/HomeScreen.kv')
        Builder.load_file('Screens/Graph/GraphScreen.kv')
        Builder.load_file('Screens/Schedule/ScheduleScreen.kv')
        Builder.load_file('Screens/Timelapse/TimelapseScreen.kv')
        Builder.load_file('Screens/Settings/SettingsScreen.kv')


if __name__ == '__main__':
    loadFonts()
    GrowBox().run()
