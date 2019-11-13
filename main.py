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

#### Start UP
Window.size = (1024, 600)
from fonts import loadFonts

Builder.load_file('StartScreen.kv')
Builder.load_file('MenuScreen.kv')

from circularProgressBar import CircularProgressBar

# DECLARE SCREENS # 

class StartScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
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
        self.icon = "assets/ico/feuilles.png"
        Clock.schedule_interval(self.animate, 0.1)
        return sm

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name='start'))
sm.add_widget(MenuScreen(name='menu'))

if __name__ == '__main__':
    loadFonts()
#    Window.fullscreen = 'auto'
    #C
    GrowBox().run()
