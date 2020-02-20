from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.button import Button
from os.path import sep, expanduser, isdir, dirname
from kivy_garden.filebrowser import FileBrowser
import sys

Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Hello world!!'
    Button:
        text: 'Click here to dismiss'
        on_press: pop.dismiss()
''')


class UploadPopup:
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

class SimpleButton(Button):
    text = "Fire Popup !"
    def fire_popup(self):
        pops = UploadPopup()
        pops.open()

class SampleApp(App):
    def build(self):
        return SimpleButton()

SampleApp().run()