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
    pass
class LoadingScreen(Screen):
    def anim(self, dt):
        indication = Label(text="We need to do a few things first\nBefore starting your first session",font_name="QuickSand",font_size=50)
        self.add_widget(indication)
        a = Animation(opacity=0,duration=8)
        a.start(indication)

    def __init__(self,**kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        home_title = Label(text="Welcome",font_name="QuickSand",font_size=70)
        self.add_widget(home_title)
        a = Animation(opacity=0,duration=3)
        a.start(home_title)

        Clock.schedule_once(self.anim, 2.1)

        #super(LoadingScreen,self).__init__(**kwargs)
    #    a = Animation(opacity=0, duration=1)
        #tx = Label(text="Hello",font_name="QuickSand")
    #    a.start(tx)



class HomeScreen(Screen):
    def dash(self):
        self.add_widget(DashBoard())
class HomeScreenDash(Screen):
    pass

class DashBoard(FloatLayout):
    def __init__(self, **kwargs):
        super(DashBoard, self).__init__(**kwargs)
    #    self.manager = sm
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
    Builder.load_file('Screens/LoadingScreen.kv')
    Builder.load_file('Screens/HomeScreen.kv')
    Builder.load_file('Screens/GraphScreen.kv')
    Builder.load_file('Screens/ScheduleScreen.kv')
    Builder.load_file('Screens/TimelapseScreen.kv')
    Builder.load_file('Screens/SettingsScreen.kv')
