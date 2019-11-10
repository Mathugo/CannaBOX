from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.uix.screenmanager import FadeTransition, SwapTransition, WipeTransition
from collections.abc import Iterable

from fonts import loadFonts
from circularProgressBar import CircularProgressBar

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('Screen.kv')



class StartScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
"""
class RootScreen(ScreenManager):
    pass
"""
class GrowBox(App):
    def animate(self,dt):
        circProgressBarT = self.root.get_screen('menu').ids.cpT
        circProgressBarH = self.root.get_screen('menu').ids.cpH

        if circProgressBarT.value<circProgressBarT.max:
            circProgressBarT.value+=1
        else:
            circProgressBarT.value=circProgressBarT.min

        if circProgressBarH.value<circProgressBarH.max:
            circProgressBarH.value+=1
        else:
            circProgressBarH.value=circProgressBarH.min

    def build(self):
        Clock.schedule_interval(self.animate, 0.1)
        return sm

sm = ScreenManager(transition=WipeTransition())
sm.add_widget(StartScreen(name='start'))
sm.add_widget(MenuScreen(name='menu'))

if __name__ == '__main__':
    loadFonts()
    Window.fullscreen = 'auto'
    GrowBox().run()
