from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import Label as CoreLabel
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from functools import partial

from Screens.Home.circularProgressBar import CircularProgressBar
from Screens.DashBoard.DashBoard import *

class HomeScreen(DashScreen):
    def __init__(self,**kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(img=self.img_source)
        Clock.schedule_interval(self.animate_circle, 0.1)

    def animate_circle(self,dt):
        circProgressBarT = self.ids.cpT
        circProgressBarH = self.ids.cpH

        if circProgressBarT.value<circProgressBarT.max:
            circProgressBarT.value+=1
        else:
            circProgressBarT.value=circProgressBarT.min

        if circProgressBarH.value<circProgressBarH.max:
            circProgressBarH.value+=1
        else:
            circProgressBarH.value=circProgressBarH.min
