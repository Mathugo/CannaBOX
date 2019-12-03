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

class ConfigureScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.interface="wlp2s0"

        self.scanBtn = Button(
                        size =(300, 300),
                        size_hint =(.13, .12),
                        background_color = (1,1,1,1),
                        text = "Scan wifi connection",
                        font_name = "QuickSand",
                        pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                        on_release = self.getESSID)
        self.add_widget(self.scanBtn)

    def getESSID(self, btn):
        print(" btn : "+str(btn))
        command="sudo iwlist {} scan |grep ESSID"
        result= os.popen(command.format(self.interface))
        result= list(result)
        ssid_list=[item.lstrip('SSID:').strip('"\n"') for item in result]
        ssid_list=[item.replace('ESSID:"','') for item in ssid_list]
        ssid_list=[item.replace(' ','') for item in ssid_list]
        print(ssid_list[0])
