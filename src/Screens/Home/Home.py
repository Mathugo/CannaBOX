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
import os

from Screens.Home.circularProgressBar import CircularProgressBar
from Screens.DashBoard.DashBoard import *

class HomeScreen(DashScreen):
    def __init__(self,**kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(img=self.img_source)
        self.circProgressBarH = self.ids.cpH
        self.circProgressBarT = self.ids.cpT
        self.circProgressBarH.value=1
        self.circProgressBarT.value=1
        Clock.schedule_interval(self.animate_circle, 0.5)
    def animate_circle(self,dt):

        valueT = 25
        valueH = 55
        self.circProgressBarH.value = valueH
        self.circProgressBarT.value = valueT
    #    self.circProgressBarH.pos_hint = {'center_x': 0.5, 'center_y':0.5}
    #    self.circProgressBarH.pos_hint = {'center_x': 0.7, 'center_y':0.5}

    #    command="cat Screens/Home/tmp/temp.tmp"
    #    result = os.popen(command)
    #    result = list(result)
    #    result = [item.strip('"\n"') for item in result]
    #    print("Result : "+result[0])
    #    self.circProgressBarT.value = int(result[0])
    #    command="cat Screens/Home/tmp/hygro.tmp"
    #    result = os.popen(command)
    #    result = list(result)
    #    result = [item.strip('"\n"') for item in result]
    #    print("Result : "+result[0])

    #    self.circProgressBarH.value = int(result[0])

    #    if self.circProgressBarT.value<self.circProgressBarT.max:
    #        self.circProgressBarT.value+=1
    #    else:
    #        self.circProgressBarT.value=self.circProgressBarT.min

    #    if self.circProgressBarH.value<self.circProgressBarH.max:
    #        self.circProgressBarH.value+=1
    #    else:
    #        self.circProgressBarH.value=self.circProgressBarH.min
