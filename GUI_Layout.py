import os
import kivy.garden.filebrowser
from kivy.app import App

class TestApp(App):

    def build(self):
        user_path = os.path.join(get_home_directory(), 'Documents')
        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')])
        browser.bind(on_success=self._fbrowser_success,
                     on_canceled=self._fbrowser_canceled,
                     on_submit=self._fbrowser_submit)
        return browser

    def _fbrowser_canceled(self, instance):
        print('cancelled, Close self.')

    def _fbrowser_success(self, instance):
        print(instance.selection)

    def _fbrowser_submit(self, instance):
        print(instance.selection)

TestApp().run()