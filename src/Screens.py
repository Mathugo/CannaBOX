from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class StartScreen(Screen):
    pass
class LoadingScreen(Screen):
    pass

class HomeScreen(Screen):
    def dash(self):
        self.add_widget(DashBoard())
class HomeScreenDash(Screen):
    pass

class DashBoard(FloatLayout):
    def __init__(self, **kwargs):
        super(DashBoard, self).__init__(**kwargs)
    #    animation = Animation(pos=(0, 0), t='out_bounce')
    #    animation += Animation(pos=(200, 100), t='out_bounce')
    #    animation = Animation(size=(300, 600), duration = 1.)
    #    animation = Animation(x=300, t='in_quad', duration=1.5)
        #animation = Animation(pos=(0,0))
        #animation &= Animation(size=(500, 500))
        #animation += Animation(size=(100, 50))
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
    Builder.load_file('Screens/HomeScreenDash.kv')
    Builder.load_file('Screens/GraphScreen.kv')
    Builder.load_file('Screens/GraphScreenDash.kv')
    Builder.load_file('Screens/ScheduleScreen.kv')
    Builder.load_file('Screens/ScheduleScreenDash.kv')
    Builder.load_file('Screens/TimelapseScreen.kv')
    Builder.load_file('Screens/TimelapseScreenDash.kv')
    Builder.load_file('Screens/SettingsScreen.kv')
    Builder.load_file('Screens/SettingsScreenDash.kv')
