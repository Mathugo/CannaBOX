from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import Label as CoreLabel
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial


class StartScreen(Screen):
    def anim(self, dt):
        indication = Label(text="We need to do a few things first\nBefore starting your first session",font_name="QuickSand",font_size=50)
        self.add_widget(indication)
        a = Animation(opacity=0,duration=8)
        a.start(indication)

    def __init__(self,**kwargs):
        super(StartScreen, self).__init__(**kwargs)
        home_title = Label(text="Welcome",font_name="QuickSand",font_size=70)
        self.add_widget(home_title)
        a = Animation(opacity=0,duration=3)
        a.start(home_title)

        Clock.schedule_once(self.anim, 2.1)


class HomeScreen(Screen):
    def add_dash(self):
        self.dash_widget=DashBoard()
        self.add_widget(self.dash_widget)
        #Clock.schedule_once(self.add_button, 1)
    def add_button(self,dt):
        btn1 = Button(text="Hello",
                    background_color =(1, 1, 1, 1),
                    color =(1, 1, 1, 1),
                    size =(32, 32),
                    size_hint =(.2, .2),
                    pos =(300, 250))
        #btn1.bind(on_press = callback)
        self.add_widget(btn1)

class DashBoard(FloatLayout):
    def __init__(self, **kwargs):
        super(DashBoard, self).__init__(**kwargs)
        animation = Animation(x=0)
        animation = Animation(x=300, t='in_out_back')
        animation.start(self)

class GraphScreen(Screen):
    pass
class GraphScreenDash(Screen):
    pass
class ScheduleScreen(Screen):
    pass
class ScheduleScreenDash(Screen):
    pass

class TimelapseScreen(Screen):
    pass
class TimelapseScreenDash(Screen):
    pass

class SettingsScreen(Screen):
    pass
class SettingsScreenDash(Screen):
    pass


def load_screens_files():
    Builder.load_file('Screens/StartScreen.kv')
    Builder.load_file('Screens/HomeScreen.kv')
    Builder.load_file('Screens/GraphScreen.kv')
    Builder.load_file('Screens/ScheduleScreen.kv')
    Builder.load_file('Screens/TimelapseScreen.kv')
    Builder.load_file('Screens/SettingsScreen.kv')
