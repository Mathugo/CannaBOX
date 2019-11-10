from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.graphics import Line, Rectangle, Color, Ellipse
from kivy.clock import Clock
from collections.abc import Iterable
from math import ceil
from kivy.core.text import Label as CoreLabel
from kivy.uix.progressbar import ProgressBar

_DEFAULT_THICKNESS = 10
_DEFAULT_CAP_STYLE = 'round'
_DEFAULT_PRECISION = 10
_DEFAULT_PROGRESS_COLOUR = (1, 0, 0, 1)
_DEFAULT_BACKGROUND_COLOUR = (0.26, 0.26, 0.26, 1)
_DEFAULT_MAX_PROGRESS = 100
_DEFAULT_MIN_PROGRESS = 0
_DEFAULT_WIDGET_SIZE = 200
_DEFAULT_TEXT_LABEL = CoreLabel(text="{}%", font_size=40)

class CircularProgressBarHygro(ProgressBar):

    def __init__(self,**kwargs):
        super(CircularProgressBarHygro,self).__init__(**kwargs)

        self._thickness = _DEFAULT_THICKNESS
        self._cap_style = _DEFAULT_CAP_STYLE
        self._cap_precision = _DEFAULT_PRECISION
        self._progress_colour = _DEFAULT_PROGRESS_COLOUR
        self._background_colour = _DEFAULT_BACKGROUND_COLOUR
        self._max_progress = _DEFAULT_MAX_PROGRESS
        self._min_progress = _DEFAULT_MIN_PROGRESS
        self._widget_size = _DEFAULT_WIDGET_SIZE
        self._text_label = _DEFAULT_TEXT_LABEL

        self.thickness = 30
        self.text_loading_beg="Humidity : "
        self.text_loading_end=" %"
        self.label = CoreLabel(text="0",
                               font_size=self.thickness,
                               font_name="fonts/Amble-Regular",
                               color=(1,1,0.5,1),
                               padding_x=2,
                               padding_y=2,
                               pos_hint={'x': 0, 'center_y': .5},
                               size_hint=(None, None)
                               )
        self.texture_size= None
        self.refresh_text()
        self.draw()


    def draw(self):
        with self.canvas:
            self.canvas.clear()
            #No progress
            Color(0.26,0.26,0.26)
            #Color(self.background_colour)
            Ellipse(pos=self.pos, size=self.size)
            #Progress Circle
            Color(1,0.2,0.4)
            #Color(self.progress_colour)
            Ellipse(pos=self.pos,size=self.size,angle_end=(self.value/100.0)*360)#will be replaced with necessary data
            #Inner Circle
            Color(0.3,0.2,0.5)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
            #Inner text
            Color(1, 1, 1, 1)
            Rectangle(texture=self.label.texture,size=self.texture_size,pos=(self.size[0]/2-self.texture_size[0]/2,self.size[1]/2 - self.texture_size[1]/2))
            self.label.text = self.text_loading_beg+str(int(self.value))+self.text_loading_end

    def refresh_text(self):
        self.label.refresh()
        self.texture_size=list(self.label.texture.size)
    def set_value(self, value):
        self.value = value
        self.label.text = self.text_loading_beg+str(int(self.value))+self.text_loading_end
        self.refresh_text()
        self.draw()

class CircularProgressBarTemp(ProgressBar):

    def __init__(self,**kwargs):
        super(CircularProgressBarTemp,self).__init__(**kwargs)

        self._thickness = _DEFAULT_THICKNESS
        self._cap_style = _DEFAULT_CAP_STYLE
        self._cap_precision = _DEFAULT_PRECISION
        self._progress_colour = _DEFAULT_PROGRESS_COLOUR
        self._background_colour = _DEFAULT_BACKGROUND_COLOUR
        self._max_progress = _DEFAULT_MAX_PROGRESS
        self._min_progress = _DEFAULT_MIN_PROGRESS
        self._widget_size = _DEFAULT_WIDGET_SIZE
        self._text_label = _DEFAULT_TEXT_LABEL

        self.thickness = 30
        self.text_loading_beg="Temperature : "
        self.text_loading_end=" °C"
        self.label = CoreLabel(text="0",
                               font_size=self.thickness,
                               font_name="fonts/Amble-Regular",
                               color=(1,1,0.5,1),
                               halign="center",
                               pos_hint= {'center_x': .2, 'center_y': .5}
                               )
        self.texture_size= None
        self.refresh_text()
        self.draw()


    def draw(self):
        with self.canvas:
            self.canvas.clear()
            #No progress
            Color(0.26,0.26,0.26)
            #Color(self.background_colour)
            Ellipse(pos=self.pos, size=self.size)
            #Progress Circle
            Color(1,0,0)
            #Color(self.progress_colour)
            Ellipse(pos=self.pos,size=self.size,angle_end=(self.value/100.0)*360)#will be replaced with necessary data
            #Inner Circle
            Color(0,0,0)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
            #Inner text
            Color(1, 1, 1, 1)
            Rectangle(texture=self.label.texture,size=self.texture_size,pos=(self.size[0]/2-self.texture_size[0]/2,self.size[1]/2 - self.texture_size[1]/2))
            self.label.text = self.text_loading_beg+str(int(self.value))+self.text_loading_end

    def refresh_text(self):
        self.label.refresh()
        self.texture_size=list(self.label.texture.size)
    def set_value(self, value):
        self.value = value
        self.label.text = self.text_loading_beg+str(int(self.value))+self.text_loading_end
        self.refresh_text()
        self.draw()
