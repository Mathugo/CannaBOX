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
        self.ssid_list=None
        self.ESSID_btn = []

    def run(self):
        self.getESSID()
        indication = Label(text="{} wireless network available".format(len(self.ssid_list)),
                           font_name="QuickSand",
                           font_size=50,
                           pos_hint = {'center_x': 0.5,'center_y':0.8})
        self.add_widget(indication)
        if self.ssid_list != None:
            x = 0.5
            y = 0.2
            for ssid in self.ssid_list:
                btn = Button(text=ssid,
                            font_name="Cantarell",
                            bold=True,
                            font_size=20,
                            size = (32,32),
                            size_hint = (.2,.13),
                            pos_hint = {'center_x': x, 'center_y': y})
                y+=0.1
                self.ESSID_btn.append(btn)
                self.add_widget(btn)


    def getESSID(self, **kwargs):
        command="sudo iwlist {} scan |grep ESSID"
        result= os.popen(command.format(self.interface))
        result= list(result)
        self.ssid_list=[item.lstrip('SSID:').strip('"\n"') for item in result]
        self.ssid_list=[item.replace('ESSID:"','') for item in self.ssid_list]
        self.ssid_list=[item.replace(' ','') for item in self.ssid_list]

        print(self.ssid_list[0])
