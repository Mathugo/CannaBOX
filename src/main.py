from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.uix.screenmanager import FadeTransition, SwapTransition, WipeTransition, SlideTransition
from collections.abc import Iterable
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget

#### Start UP
Window.size = (1024, 600)
from fonts import loadFonts
from circularProgressBar import CircularProgressBar
from Screens.screens import *

sm = ScreenManager(transition=FadeTransition())
load_screens_files()

# DECLARE SCREENS # 


class GrowBox(App):

    def animate_circle(self,dt):

        circProgressBarT = self.root.get_screen('home').ids.cpT
        circProgressBarH = self.root.get_screen('home').ids.cpH


        if circProgressBarT.value<circProgressBarT.max:
            circProgressBarT.value+=1
        else:
            circProgressBarT.value=circProgressBarT.min

        if circProgressBarH.value<circProgressBarH.max:
            circProgressBarH.value+=1
        else:
            circProgressBarH.value=circProgressBarH.min

    def build(self):
        self.sm=sm
        self.loadScreens()
        Clock.schedule_interval(self.animate_circle, 0.1)
        return sm

    def loadScreens(self):

        global sm
        #sm.add_widget(StartScreen(name='start'))
        self.home=HomeScreen(name='home')
        self.graph=GraphScreen(name='graph')
        self.schedule=ScheduleScreen(name='schedue')
        self.timelapse=TimelapseScreen(name='timelapse')
        self.settings=SettingsScreen(name='settings')

        sm.add_widget(self.home)
        sm.add_widget(self.graph)
        sm.add_widget(self.schedule)
        sm.add_widget(self.timelapse)
        sm.add_widget(self.settings)


if __name__ == '__main__':
    loadFonts()

    GrowBox().run()
