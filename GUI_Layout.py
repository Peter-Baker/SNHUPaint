from kivy.app import App

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy_garden.filebrowser import FileBrowser
from kivy.uix.popup import Popup

class Background(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            if not self.collide_point(*touch.pos):
                Color(249, 0, 0)
                touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            touch.ud['line'].points += [touch.x, touch.y]

class Test(TabbedPanel):
    def pencil_button(self):
        Color(255, 0, 0)

    def open_file_btn_pressed(self, *args):

        self._fbrowser = FileBrowser(select_string='Open')
        self._fbrowser.bind(on_success=self._file_load,
                            on_canceled=self._cancel_popup)

        self._popup = Popup(title='Open File', content=self._fbrowser,
                            size_hint=(0.9, 0.9), auto_dismiss=False)

        self._popup.open()


class MyMain(Widget):
    pass


# App will initialize everything that kivy needs
class CanvasApp(App):
    def build(self):
        return MyMain()


CanvasApp().run()
