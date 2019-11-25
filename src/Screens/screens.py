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


class StartScreen(Screen):
    def __init__(self,**kwargs):
        super(StartScreen, self).__init__(**kwargs)

        Clock.schedule_interval(self.logo_anim,2)
        self.stop_image=1
        self.start_btn = Button(
                        size = (32,32),
                        size_hint = (1,1),
                        background_color = (0,0,0,0),
                        on_release = self.welcome)
        self.add_widget(self.start_btn)

    def logo_anim(self,dt):
        if self.stop_image:
            self.start_image = Image(source="../img/start_background.png",
                        color=(1,1,1,1),
                #        size_hint=(.4,.4),
                        pos_hint={'center_x': 0.5, 'center_y':0.5})
            self.add_widget(self.start_image)
            self.anim_image = Animation(opacity=0,duration=2)
            self.anim_image.start(self.start_image)

    def welcome(self,release):
        #self.remove_widget(self.start_btn)
        #self.remove_widget(self.start_image)
        #Animation.cancel_all(self.start_image, 'opacity')
        self.stop_image=0

        home_title = Label(text="Welcome",font_name="QuickSand",font_size=70)
        self.add_widget(home_title)
        a = Animation(opacity=0,duration=3)
        a.start(home_title)
        Clock.schedule_once(self.few_things, 3)

    def few_things(self, dt):
        indication = Label(text="We need to do a few things first\nBefore starting your first session",font_name="QuickSand",font_size=50)
        self.add_widget(indication)
        a = Animation(opacity=0,duration=8)
        a.start(indication)
        Clock.schedule_once(self.want_to_configure,8)

    def want_to_configure(self, dt):

        Clock.schedule_interval(self.anim_text,2)

        btnyes=Button(background_color =(1, 1, 1, 1),
                      color =(1, 1, 1, 1),
                      text="Yes",
                      font_size=40,
                      font_name="Cantarell",
                      size =(300, 300),
                      size_hint =(.13, .12),
                      pos_hint = {'center_x':0.5, 'center_y':0.3},
                      on_release = self.Goconfigure)

        btnskip=Button(background_color =(1, 1, 1, 1),
                      color =(1, 1, 1, 1),
                      text="Skip",
                      font_size=40,
                      font_name="Cantarell",
                      size =(300, 300),
                      size_hint =(.13, .12),
                      pos_hint = {'center_x':0.9, 'center_y':0.1},
                      on_release = self.Gohome)
        self.add_widget(btnskip)
        self.add_widget(btnyes)

    def anim_text(self,dt):
        wifi = Label(text="Do you want the webpage\nof your plant to be enable ?",font_name="QuickSand",font_size=50)
        self.add_widget(wifi)
        a = Animation(opacity=0.5,duration=2)
        a.start(wifi)

    def Gohome(self,release):
        self.sm.current = "home"

    def Goconfigure(self,release):
        self.sm.current="configure"

    def setSm(self, sm):
        self.sm=sm

class ConfigureScreen(Screen):

    def Gohome(self):
        self.sm.current="home"

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

class HomeScreen(DashScreen):
    def __init__(self,**kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(img=self.img_source)

class GraphScreen(DashScreen):
    def __init__(self, **kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(img=self.img_source)
        self.add_dash() # FIRST TIME TO DISPLAY WHEN CHANGING SCREEN

class ScheduleScreen(DashScreen):
    def __init__(self, **kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(img=self.img_source)
        self.add_dash() # FIRST TIME TO DISPLAY WHEN CHANGING SCREEN

class TimelapseScreen(DashScreen):
    def __init__(self, **kwargs):
        self.img_source=kwargs.pop('img',None)
        super().__init__(img=self.img_source)
        self.add_dash() # FIRST TIME TO DISPLAY WHEN CHANGING SCREEN

class SettingsScreen(DashScreen):
    def __init__(self, **kwargs):
        self.img_source =kwargs.pop('img',None)
        super().__init__(img=self.img_source)
        self.add_dash() # FIRST TIME TO DISPLAY WHEN CHANGING SCREEN

def load_screens_files():
    Builder.load_file('Screens/StartScreen.kv')
    Builder.load_file('Screens/DashBoard.kv')
    Builder.load_file('Screens/DashBoardScreen.kv')
    Builder.load_file('Screens/HomeScreen.kv')
    Builder.load_file('Screens/GraphScreen.kv')
    Builder.load_file('Screens/ScheduleScreen.kv')
    Builder.load_file('Screens/TimelapseScreen.kv')
    Builder.load_file('Screens/SettingsScreen.kv')
