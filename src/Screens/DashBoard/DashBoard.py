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


class DashScreen(Screen):
    def __init__(self, **kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(**kwargs)
        self.anim_duration=1

    def add_dash(self):
        self.dash_widget=DashBoard()
        self.dash_widget.setImg(self.img_source)

        self.add_widget(self.dash_widget)
        Clock.schedule_once(self.add_button, self.anim_duration)
    def remove_dash(self,dt):
        self.dash_widget.remove()
        Clock.schedule_once(self.remove_dash_clock,self.anim_duration)
    def remove_dash_clock(self,dt):
        self.remove_widget(self.dash_widget)
        self.remove_widget(self.btn1)
    def add_button(self,dt):
        btn1 = Button(
                    background_color =(0, 0, 0, 0),
                    color =(1, 1, 1, 1),
                    size =(32, 32),
                    size_hint =(.08, .12),
                    pos =(0, 530))
        btn1.bind(on_press = self.remove_dash)
        self.btn1=btn1
        self.add_widget(btn1)

class DashBoard(FloatLayout):
    def __init__(self,**kwargs):
        #self.img_source=kwargs.get('img_source',None)
        super().__init__(**kwargs)
        self.img = self.ids.img_dash
        self.anim_duration=1
        animation = Animation(x=0)
        animation = Animation(x=300, t='in_out_back',duration=self.anim_duration)
        animation.start(self)

    def setImg(self, psource):
        self.img.source=psource
    def remove(self):
        animation = Animation(x=300)
        animation = Animation(x=0, t='in_out_back',duration=self.anim_duration)
        animation.start(self)
