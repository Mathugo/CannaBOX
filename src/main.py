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
from Screens import *

sm = ScreenManager(transition=FadeTransition())
load_screens_files()

# DECLARE SCREENS # 


class GrowBox(App):
    def animate_circle(self,dt):

        #tx = self.root.get_screen('loading').ids.things
        #anim.start(tx)
        #anim = Animation(pos=(100,100), t='out_bounce')

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
        Clock.schedule_interval(self.animate_circle, 0.1)
        return sm


def loadScreens():

    global sm
    sm.add_widget(LoadingScreen(name='loading'))
    #sm.add_widget(StartScreen(name='start'))
    home = HomeScreen(name='home')
    sm.add_widget(home)
    sm.add_widget(HomeScreenDash(name='homedash'))
    sm.add_widget(GraphScreen(name='graph'))
    sm.add_widget(GraphScreenDash(name='graphdash'))
    sm.add_widget(ScheduleScreen(name='schedule'))
    sm.add_widget(ScheduleScreenDash(name='scheduledash'))
    sm.add_widget(TimelapseScreen(name='timelapse'))
    sm.add_widget(TimelapseScreenDash(name='timelapsedash'))
    sm.add_widget(SettingsScreen(name='settings'))
    sm.add_widget(SettingsScreenDash(name='settingsdash'))


if __name__ == '__main__':
    loadFonts()
    loadScreens()
    GrowBox().run()
