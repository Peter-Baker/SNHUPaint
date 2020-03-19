from kivy.app import App

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

# Create a global variable that will hold the color of the pencil
global paint_color
clr_picker = ColorPicker()
paint_color = ListProperty([0, 0, 0, 1])  # Set the color of the pencil to black

global rad
rad = 30


class MyMain(Widget):
    global paint_color
    paint_color = [0, 0, 0, 1]

    def eraser(self):  # This method is called when someone clicks on the eraser button
        global paint_color
        paint_color = [255, 255, 255, 1]  # Set pencil color to white

    def pencil(self):  # This method is called when someone clicks on the pencil button
        global paint_color
        paint_color = [0, 0, 0, 1]  # Set pencil color to black

    def slider(self, slideNum, *args):
        global rad
        rad = self.ids.slideNum.value

    def color_picked(self, colorpicker, *args):
        global paint_color
        paint_color = colorpicker.color
        print(paint_color)



class TextInputPopup(FloatLayout):
    pass



class Background(Widget):
    global paint_color
    paint_color = [0, 0, 0, 1]
    paint = paint_color

    def setColor(self):  # Should reset color, but Error: kivy.properties.ListProperty object is not iterable
        self.paint = paint_color

    def on_touch_down(self, touch):  # When someone clicks down on the white canvas...
        self.setColor()  # This is where I call that function - when the error happens
        with self.canvas:
            if not self.collide_point(*touch.pos):  # Make sure click is on white canvas, and not TabbedPanel
                Color(rgba=self.paint)  # Set color to paint_color value
                global rad
                Ellipse(pos=(touch.x, touch.y), size=(rad/2, rad/2))
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        if "line" not in touch.ud:
            global rad
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=rad/2)
        touch.ud["line"].width = rad/3.9
        touch.ud["line"].points += [touch.x, touch.y]  # Points are the position


class Test(TabbedPanel):  # Creates tab panel, all of it is done in kivy that is why we pass
    pass


class CanvasApp(App):
    def build(self):
        return MyMain()


CanvasApp().run()
