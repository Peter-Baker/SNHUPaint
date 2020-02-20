from kivy.app import App

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy_garden.filebrowser import FileBrowser
from kivy.uix.popup import Popup

class UploadPopup(Popup):
    def __init__(self, short_text='heading'):

        browser = FileBrowser(select_string='Select', cancel_state='down')
        browser.bind(on_success=self._fbrowser_success,
                     on_canceled=self._fbrowser_canceled,
                     on_submit=self._fbrowser_submit)

        self.popup = Popup(
            title=short_text,
            content=browser, size_hint=(0.9, 0.9),
            auto_dismiss=False
        )
        self.popup.open()

    def _fbrowser_canceled(self, instance):
        print('cancelled, Close self.')
        self.popup.dismiss()

    def _fbrowser_success(self, instance):
        print(instance.selection)
        self.popup.dismiss()

    def _fbrowser_submit(self, instance):
        print(instance.selection)
        self.popup.open()
class Background(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            if not self.collide_point(*touch.pos):
                Color(249, 0, 0)
                touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            touch.ud['line'].points += [touch.x, touch.y]


    def fire_popup(self):
        pops=UploadPopup()
        pops.open()
class Test(TabbedPanel):
    def pencil_button(self):
        Color(255, 0, 0)


class MyMain(Widget):
    pass


# App will initialize everything that kivy needs
class CanvasApp(App):
    def build(self):
        return MyMain()


CanvasApp().run()
