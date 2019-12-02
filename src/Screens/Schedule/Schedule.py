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

from Screens.DashBoard.DashBoard import *


class ScheduleScreen(DashScreen):
    def __init__(self, **kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(img=self.img_source)
        self.add_dash() # FIRST TIME TO DISPLAY WHEN CHANGING SCREEN
