from tkinter import TRUE, ARC

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

# Create a global variable that will hold the color of the pencil
global paint_color
clr_picker = ColorPicker()
paint_color = ListProperty([0, 0, 0, 1])  # Set the color of the pencil to black

global rad
rad = 30


class MyMain(Widget):
    # Stores current drawing tool used
    drawing_tool = "rectangle"

    # Tracks whether left mouse is down
    left_but = "up"

    # x and y positions for drawing with pencil
    x_pos, y_pos = None, None

    # Tracks x & y when the mouse is clicked and released
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

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

    def btn(self):
        show_popup()

# ---------- CATCH MOUSE UP ----------

    def left_but_down(self, event=None):
        self.left_but = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    # ---------- CATCH MOUSE UP ----------

    def left_but_up(self, event=None):
        self.left_but = "up"

        # Reset the line
        self.x_pos = None
        self.y_pos = None

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        # If mouse is released and line tool is selected
        # draw the line
        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "text":
            self.text_draw(event)

    # ---------- CATCH MOUSE MOVEMENT ----------

    def motion(self, event=None):

        if self.drawing_tool == "pencil":
            self.pencil_draw(event)

    # ---------- DRAW PENCIL ----------

    def pencil_draw(self, event=None):
        if self.left_but == "down":

            # Make sure x and y have a value
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,                        event.x, event.y, smooth=TRUE)

            self.x_pos = event.x
            self.y_pos = event.y

    # ---------- DRAW LINE ----------

    def line_draw(self, event=None):

        # Shortcut way to check if none of these values contain None
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="green")

    # ---------- DRAW OVAL ----------

    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,                              self.y2_line_pt):

            # fill : Color option names are here http://wiki.tcl.tk/37701
            # outline : border color
            # width : width of border in pixels

            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt,                                              self.x2_line_pt, self.y2_line_pt,
                                        fill="midnight blue",
                                        outline="yellow",
                                        width=2)

    # ---------- DRAW RECTANGLE ----------

    def rectangle_draw(self, event=None):
        print("Made it into function")
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,                              self.y2_line_pt):
            print("Made it into if")
            # fill : Color option names are here http://wiki.tcl.tk/37701
            # outline : border color
            # width : width of border in pixels

            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt,                  self.x2_line_pt, self.y2_line_pt,
                fill="midnight blue",
                outline="yellow",
                width=2)




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
                Ellipse(pos=(touch.x, touch.y), size=(rad / 2, rad / 2))
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        if "line" not in touch.ud:
            global rad
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=rad / 2)
        touch.ud["line"].width = rad / 3.9
        touch.ud["line"].points += [touch.x, touch.y]  # Points are the position


def show_popup():
    show = TextInputPopup()

    popupWindow = (Popup(title="Enter Text", content=show, size_hint=(None, None), size=(400, 200)))

    popupWindow.open()


class Test(TabbedPanel):  # Creates tab panel, all of it is done in kivy that is why we pass
    pass


class CanvasApp(App):
    def build(self):
        return MyMain()


CanvasApp().run()
