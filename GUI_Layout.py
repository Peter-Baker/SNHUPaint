from tkinter import TRUE, ARC

from kivy.app import App

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.graphics import *
# from kivy.graphics import Color, Ellipse, Line
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.button import Button
# Create a global variable that will hold the color of the pencil
global paint_color
global main_self
global stencil
paint_color = ListProperty([0, 0, 0, 1])  # Set the color of the pencil to black
stencil = 1 #sets stencil to base pencil

global rad
rad = 30


class MyMain(Widget):
    global paint_color
    paint_color = [0, 0, 0, 1]

    def eraser(self):  # This method is called when someone clicks on the eraser button
        global stencil #Lower in the document. This is so you cannot switch the color of the eraser and it also allows us to easily turn off and on the drawing
        stencil = 3

    def pencil(self):  # This method is called when someone clicks on the pencil button
        global stencil #Lower in the document.
        stencil = 1
    def dropper(self):
        global stencil
        stencil = 2
    def text(self):
        global main_self
        main_self = self
        global stencil
        stencil = 4
    def slider(self, slideNum, *args):
        global rad
        rad = self.ids.slideNum.value

    def update_button(self):
        global  paint_color
        global main_self
        main_self.ids.clr_button.background_color = paint_color
    def color_picked(self, colorpicker):
        global paint_color
        paint_color = colorpicker
        MyMain.update_button(self)
    def set_color(self, *args):
        global paint_color
        global main_self
        main_self = self
        return paint_color

    def filebtn(self):
        show = filePopup()
        popupWindow = (Popup(title="File Chooser", content=show, size_hint=(None, None), size=(600, 400)))
        popupWindow.open()

    def colorbtn(self):
        show = colorPopup()
        colorpopupWindow = (Popup(title="Pick A Color", content=show, size_hint=(None, None), size=(500, 300)))
        colorpopupWindow.open()

    def clearbtn(self):
        #show = clearPopup()
        #clearpopupWindow = Popup(title='Test popup', content=show, size_hint=(None, None), size=(400, 400))
        #clearpopupWindow.open()
        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(Label(text="Are you sure you want to clear the project? \n Once clicked it cannot be re-done!"))
        btn1 = Button(text = "YES TO CLEAR")
        btn2 = Button(text = "NO TO GO BACK")
        box.add_widget(btn1)
        box.add_widget(btn2)

        popup = Popup(title='Check if Correct', title_size=(30),
                      title_align='center', content=box,
                      size_hint=(None, None), size=(400, 400), auto_dismiss=True)
        btn2.bind(on_press = popup.dismiss)
        #btn1.bind(on_press = self.canvas.after.clear) #This will be where we will call something to clear the canvas
        popup.open()


    def circle_draw(self, xVal, yVal, slideNum, *args):
        with self.canvas:
            # Add a red color
            Color(1, 0, 0)

            # Add a rectangle
            Ellipse(pos=(xVal, yVal), size=(slideNum, slideNum))
            #Line(circle=(xVal, yVal, slideNum))

    def square_draw(self, xVal, yVal, slideNum, *args):
        with self.canvas:
            # Add a red color
            Color(1, 0, 0)  # Need to figure out colors

            # Add a rectangle
            Rectangle(pos=(xVal, yVal), size=(slideNum, slideNum))

    def line_draw(self, xVal, yVal, slideNum, *args):
        with self.canvas:
            # Add a red color
            Color(1, 0, 0)  # Need to figure out colors

            # Add a rectangle
            Rectangle(pos=(xVal, yVal), size=(slideNum*6, 5))


class filePopup(BoxLayout):
    def selected(self,filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass


class clearPopup(FloatLayout):
    pass


class colorPopup(FloatLayout):

    def get_picked(self, colorpicker, *args):
        global paint_color
        paint_color = colorpicker
        MyMain.update_button(self)
    def set_color(self, colorpicker, *args):
        global paint_color
        return paint_color
    pass

class shapePopup(FloatLayout):
    pass

class Background(Widget):
    global main_self
    global paint_color
    global stencil
    paint_color = [0, 0, 0, 1]
    paint = paint_color


    def setColor(self):  # Should reset color, but Error: kivy.properties.ListProperty object is not iterable
        self.paint = paint_color

    def on_touch_down(self, touch):  # When someone clicks down on the white canvas...
        global rad
        if stencil == 1: #Stencil for Pen
            self.setColor()  # This is where I call that function - when the error happens
            with self.canvas:
                if not self.collide_point(*touch.pos):  # Make sure click is on white canvas, and not TabbedPanel
                    Color(rgba=self.paint)  # Set color to paint_color value
                    Ellipse(pos=(touch.x, touch.y), size=(rad / 2, rad / 2))
                    touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)
        if stencil == 2: #Stencil for Dropper
            with self.canvas:
                if not self.collide_point(*touch.pos):
                    print(touch.x, touch.y)
        if stencil == 3:#Stencil for Eraser
            self.setColor()  # This is where I call that function - when the error happens
            with self.canvas:
                if not self.collide_point(*touch.pos):  # Make sure click is on white canvas, and not TabbedPanel
                    Color([0, 0, 0, 1])  # Set color to paint_color value
                    Ellipse(pos=(touch.x, touch.y), size=(rad / 2, rad / 2))
                    touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)
        if stencil == 4:#Stencil for moving text
            with self.canvas:
                if not self.collide_point(*touch.pos):
                    if 445 > touch.y > 5:
                        main_self.ids.txt_inpt_location.pos = ((touch.x - 50), (touch.y - 50))

    def on_touch_move(self, touch):
        if stencil == 4:#Stencil for moving text
            with self.canvas:
                if not self.collide_point(*touch.pos):
                    if 445 > touch.y > 5:
                        main_self.ids.txt_inpt_location.pos = ((touch.x - 50), (touch.y - 50))
        if "line" not in touch.ud:
            global rad
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=rad / 2)
        touch.ud["line"].width = rad / 3.9
        touch.ud["line"].points += [touch.x, touch.y]  # Points are the position

class Test(TabbedPanel):  # Creates tab panel, all of it is done in kivy that is why we pass
    pass


class CanvasApp(App):
    def build(self):
        return MyMain()


CanvasApp().run()
