from kivy.app import App

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line



class Test(TabbedPanel):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyWidget(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CanvasApp(App):

    def build(self):
        return Test()


CanvasApp().run()
