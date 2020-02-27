from kivy.app import App

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.slider import Slider

# Create a global variable that will hold the color of the pencil
global paint_color
paint_color = ListProperty([0, 0, 0, 1])  # Set the color of the pencil to black

global rad
rad = 30


class MyMain(Widget):

    def eraser(self):  # This method is called when someone clicks on the eraser button
        global paint_color
        paint_color = [255, 255, 255, 1]  # Set pencil color to white

    def pencil(self):  # This method is called when someone clicks on the pencil button
        global paint_color
        paint_color = [0, 0, 0, 1]  # Set pencil color to black

    def slider(self):
        global rad
        rad = 30


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
                rad = 30
                Ellipse(pos=(touch.x, touch.y), size=(rad / 2, rad / 2))
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        if "line" not in touch.ud:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
        touch.ud["line"].points += [touch.x, touch.y]


class Test(TabbedPanel):
    pass


class Test(TabbedPanel):  # Creates tab panel, all of it is done in kivy that is why we pass
    pass


# App will initialize everything that kivy needs
class CanvasApp(App):
    def build(self):
        return MyMain()


CanvasApp().run()
