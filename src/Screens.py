from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class StartScreen(Screen):
    pass

class HomeScreen(Screen):
    pass
class HomeScreenDash(Screen):
    pass

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
    Builder.load_file('Screens/HomeScreenDash.kv')
    Builder.load_file('Screens/GraphScreen.kv')
    Builder.load_file('Screens/GraphScreenDash.kv')
    Builder.load_file('Screens/ScheduleScreen.kv')
    Builder.load_file('Screens/ScheduleScreenDash.kv')
    Builder.load_file('Screens/TimelapseScreen.kv')
    Builder.load_file('Screens/TimelapseScreenDash.kv')
    Builder.load_file('Screens/SettingsScreen.kv')
    Builder.load_file('Screens/SettingsScreenDash.kv')
