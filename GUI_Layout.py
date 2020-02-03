import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_string("""

<Test>:
    size_hint: 1, .23
    pos_hint: {'center_x': .5, 'center_y': .89}
    tab_height: 25
    tab_width: 50
    do_default_tab: False

    TabbedPanelItem:        
        text: 'Home'
        StripLayout:
            background_color: (1, 1, 1, 1)
            Label:
                text: 'Colors'
                pos: (65, 435)
                font_size: 12
            Button:
                text: ''
                size: (25, 25)
                pos: (30, 530)
                background_color: (0, 1, 0, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (65, 530)
                background_color: (1, 0, 0, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (30, 495)
                background_color: (0, 0, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (65, 495)
                background_color: (1, 0.2, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (100, 530)
                background_color: (1, 1, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (100, 495)
                background_color: (.75, 0, .25, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (135, 495)
                background_color: (.2, .3, .5, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (135, 530)
                background_color: (.4, .4, .4, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (170, 495)
                background_color: (.1, .2, .3, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (170, 530)
                background_color: (0, 0, 0, 1)
            Button:
                text: ''
                size: (40, 40)
                pos: (220, 510)
                background_color: (2, 2, 2, 1)
            Label:
                pos: (203, 445)
                text: 'CurrentColor'
                font_size: 12
            Button:
                text: ''
                size: (40, 40)
                pos: (320, 510)
                background_color: (1, 2, 2, 1)
            Label:
                pos: (289, 445)
                text: 'Brush'
                font_size: 12
            Button:
                text: ''
                size: (25, 25)
                pos: (400, 530)
                background_color: (1, 1, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (435, 530)
                background_color: (1, 1, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (400, 495)
                background_color: (1, 1, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (435, 495)
                background_color: (1, 1, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (470, 530)
                background_color: (1, 1, 1, 1)
            Button:
                text: ''
                size: (25, 25)
                pos: (470, 495)
                background_color: (1, 1, 1, 1)
            Label:
                pos: (398, 433)
                text: 'Tools'
                font_size: 12
            
    TabbedPanelItem:
        text: 'Edit'
        Label:
            text: 'Edit tab content will be here'
""")

class Test(TabbedPanel):
    pass

class MyWidget(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CanvasApp(App):

    def build(self):
        return Test()

CanvasApp().run()