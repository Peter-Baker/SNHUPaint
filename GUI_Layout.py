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
from kivy.uix.image import Image
# Create a global variable that will hold the color of the pencil
global paint_color
global main_self
global maincanvas_self
global stencil
global name
global firstimg, image_widget, fboimage_widget
paint_color = ListProperty([0, 0, 0, 1])  # Set the color of the pencil to black
stencil = 1 #sets stencil to base pencil

global rad
rad = 50

global radShape
radShape = 50

global shapeSize
shapeSize = 50


class MyMain(Widget):
    global paint_color
    global fbo_self
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
    def filler(self):
        global stencil
        stencil = 8
    def slider(self, slideNum, *args):
        global rad
        rad = self.ids.slideNum.value

    def sliderShape(self, slideNumShape, *args):
        global shapeSize
        shapeSize = slideNumShape

    def update_button(self):
        global  paint_color
        global main_self
        main_self.ids.clr_button.background_color = paint_color
        main_self.ids.clr_button2.background_color = paint_color
    def color_picked(self, colorpicker):
        global paint_color
        paint_color = colorpicker
        MyMain.update_button(self)
    def set_color(self, *args):
        global paint_color
        global main_self
        main_self = self
        return paint_color
    def color_black(self):
        global paint_color
        paint_color = (0,0,0,1)
        MyMain.update_button(self)
    def text_color(self):
        global paint_color
        self.ids.txt_inpt_location.color = paint_color
    def filebtn(self):
        show = filePopup()
        popupWindow = (Popup(title="File Chooser", content=show, size_hint=(None, None), size=(600, 400)))
        popupWindow.open()

    def savebtn(self):
        show = savePopup()
        popupWindow = (Popup(title="Save Message", content=show, size_hint=(None, None), size=(280, 100)))
        popupWindow.open()
        Background.saveimage(self)

    def colorbtn(self):
        show = colorPopup()
        colorpopupWindow = (Popup(title="Pick A Color", content=show, size_hint=(None, None), size=(500, 300)))
        colorpopupWindow.open()

    def clearbtn(self):
        Background.clearingCanvas(self)

    def circle_draw(self, slideNum, *args):
        global stencil #Lower in the document.
        stencil = 5
        global shapeSize
        shapeSize = slideNum

    def square_draw(self, slideNum, *args):
        global stencil
        stencil = 6
        global shapeSize
        shapeSize = slideNum

    def line_draw(self, slideNum, *args):
        global stencil
        stencil = 7
        global shapeSize
        shapeSize = slideNum

class filePopup(BoxLayout):
    def selected(self,filename):
        global name
        self.ids.image.source = filename[0]
        name = filename[0]
        Background.fileImage(self, name)
        pass

class savePopup(BoxLayout):
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
    global maincanvas_self
    global paint_color
    global stencil
    paint_color = [0, 0, 0, 1]
    paint = paint_color

    def __init__(self, **kwargs):
        global maincanvas_self
        maincanvas_self = self
        super(Background, self).__init__(**kwargs)
        with self.canvas:
            self.fbo = Fbo(size=(800, 450))
        maincanvas_self.fbo.add(Rectangle(size=(800, 450), rgba=(1, 1, 1, 1)))

    def clearingCanvas(self):
        with maincanvas_self.canvas:
            Color(255, 255, 255)
            # Add a rectangle
            Rectangle(pos=self.pos, size=(800, 450))
        with maincanvas_self.fbo:  # Adding the maincanvas_self.fbo will allow the eye dropper to be used on it
            Color(255, 255, 255)
            # Add a rectangle
            Rectangle(pos=self.pos, size=(800, 450))


    def setColor(self):  # Should reset color, but Error: kivy.properties.ListProperty object is not iterable
        self.paint = paint_color


    def saveimage(self):
        maincanvas_self.fbo.texture.save(filename='D:/screenshot.png')

    def fileImage(self,name):
        global firstimg
        global image_widget,fboimage_widget
        try:
            firstimg
        except NameError:
            firstimg = False
        if firstimg:
            #maincanvas_self.remove_widget(image_widget)
            maincanvas_self.canvas.remove(fboimage_widget)
            maincanvas_self.fbo.remove(fboimage_widget)
            maincanvas_self.canvas.add(Rectangle(size=(800, 450), rgba=(1, 1, 1, 1)))
            maincanvas_self.fbo.add(Rectangle(size=(800, 450), rgba=(1, 1, 1, 1)))
            maincanvas_self.canvas.add
        else:
            firstimg = True

        image_widget = Image(source=name, size=(800, 450)) #Rescaling Image
        x = float(image_widget.texture.size[0])
        y = float(image_widget.texture.size[1])
        xchange = x/800
        ychange = y/450
        if xchange > ychange:
            x = x/xchange
            y = y/xchange
            u = 450 - y
            u = u/2
            poss = (0,u)
        elif ychange > xchange:
            x = x / ychange
            y = y / ychange
            v = 800 - x
            v = v/2
            poss = (v,0)
        else:
            x = x / xchange
            y = y / ychange
            poss = (0,0)
        fboimage_widget = Rectangle(source=name,size=(x,y),pos=(poss)) #End of rescaling image
        with maincanvas_self.fbo:
            Color(rgba=(1, 1, 1, 1))
            maincanvas_self.fbo.add(Rectangle(size=(800, 450), rgba=(1,1,1,1)))
            maincanvas_self.fbo.add(fboimage_widget)

        with maincanvas_self.canvas:
            Color(rgba=(1,1,1,1))
            maincanvas_self.canvas.add(Rectangle(size=(800, 450), rgba=(1, 1, 1, 1)))
            maincanvas_self.canvas.add(fboimage_widget)


        #maincanvas_self.add_widget(image_widget)

    def on_touch_down(self, touch):  # When someone clicks down on the white canvas...
        global paint_color
        global rad
        global shapeSize
        if stencil == 1: #Stencil for Pen
            self.setColor()  # This is where I call that function - when the error happens
            with self.canvas:
                if not self.collide_point(*touch.pos) and 460 > touch.y > -10:  # Make sure click is on white canvas, and not TabbedPanel
                    Color(rgba=self.paint)  # Set color to paint_color value
                    Ellipse(pos=(touch.x - 12, touch.y - 11), size=(rad / 2, rad / 2))
                    touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)
                with self.fbo:
                    if not self.collide_point(*touch.pos):
                        Color(rgba=self.paint)
                        Ellipse(pos=(touch.x - 12, touch.y - 11), size=(rad / 2, rad / 2))
                        touch.ud['linefbo'] = Line(points=(touch.x, touch.y), width=15)


        if stencil == 2: #Stencil for Dropper
            with self.canvas:
                if not self.collide_point(*touch.pos) and 450 > touch.y > 0:
                    r, g, b, a = ['', '', '', '']
                    viv_color = self.fbo.get_pixel_color(touch.x, touch.y)
                    r = viv_color[0]
                    g = viv_color[1]
                    b = viv_color[2]
                    a =viv_color[3]
                    float(r)
                    float(g)
                    float(b)
                    float(a)
                    r /= 255
                    g /= 255
                    b /= 255
                    a /= 255
                    viv_color = [r,g,b,a]
                    if viv_color == [0.0, 0.0, 0.0, 0.0]:
                        viv_color = [1.0, 1.0, 1.0, 1.0]

                    paint_color = viv_color
                    MyMain.update_button(main_self)

        if stencil == 3:#Stencil for Eraser
            self.setColor()  # This is where I call that function - when the error happens
            with self.canvas:
                if not self.collide_point(*touch.pos) and 460 > touch.y > -10:  # Make sure click is on white canvas, and not TabbedPanel
                    Color([0, 0, 0, 1])  # Set color to paint_color value
                    Ellipse(pos=(touch.x, touch.y), size=(rad / 2, rad / 2))
                    touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)
                    with self.fbo:
                        if not self.collide_point(*touch.pos):
                            Color([1, 1, 1])
                            Ellipse(pos=(touch.x - 12, touch.y - 11), size=(rad / 2, rad / 2))
                            touch.ud['linefbo'] = Line(points=(touch.x, touch.y), width=15)
        if stencil == 4:#Stencil for moving text
            with self.canvas:
                if not self.collide_point(*touch.pos):
                    if 445 > touch.y > 5:
                        main_self.ids.txt_inpt_location.pos = ((touch.x - 50), (touch.y - 50))

        if stencil == 5: #circle creation
            if not self.collide_point(*touch.pos) and 460 > touch.y > -10:
                with self.canvas:
                    Color(paint_color[0], paint_color[1], paint_color[2])
                    # Add a rectangle
                    Ellipse(pos=(touch.x - 12, touch.y - 11), size=(shapeSize, shapeSize))
                    #   Line(circle=(xVal, yVal, slideNum))
                with maincanvas_self.fbo:  # Adding the maincanvas_self.fbo will allow the eye dropper to be used on it
                    Color(paint_color[0], paint_color[1], paint_color[2])
                    # Add a rectangle
                    Rectangle(pos=(touch.x - 12, touch.y - 11), size=(shapeSize, shapeSize))

        if stencil == 6: #square creation
            if not self.collide_point(*touch.pos) and 460 > touch.y > -10:
                with self.canvas:
                    Color(paint_color[0], paint_color[1], paint_color[2])
                    # Add a rectangle
                    Rectangle(pos=(touch.x - 12, touch.y - 11), size=(shapeSize, shapeSize))
                with maincanvas_self.fbo:  # Adding the maincanvas_self.fbo will allow the eye dropper to be used on it
                    Color(paint_color[0], paint_color[1], paint_color[2])
                    # Add a rectangle
                    Rectangle(pos=(touch.x - 12, touch.y - 11), size=(shapeSize, shapeSize))

        if stencil == 7: #line creation
            if not self.collide_point(*touch.pos) and 460 > touch.y > -10:
                with self.canvas:
                    Color(paint_color[0], paint_color[1], paint_color[2])
                    # Add a rectangle
                    Rectangle(pos=(touch.x - 12, touch.y - 11), size=(shapeSize * 6, 5))
                with maincanvas_self.fbo:  # Adding the maincanvas_self.fbo will allow the eye dropper to be used on it
                    Color(paint_color[0], paint_color[1], paint_color[2])
                    # Add a rectangle
                    Rectangle(pos=(touch.x - 12, touch.y - 11), size=(shapeSize * 6, 5))

        if stencil == 8:
            with self.canvas:
                Color(paint_color[0], paint_color[1], paint_color[2])
                Rectangle(pos=(0, 0), size=(800, 470)) #paints a rectangle the size of the canvas to fill screen
            with maincanvas_self.fbo:
                Color(paint_color[0], paint_color[1], paint_color[2])
                Rectangle(pos=(0, 0), size=(800, 470))

    def on_touch_move(self, touch):
        if stencil == 4:#Stencil for moving text
            with self.canvas:
                if not self.collide_point(*touch.pos):
                    if 445 > touch.y > 5:
                        main_self.ids.txt_inpt_location.pos = ((touch.x - 50), (touch.y - 50))

        if 460 > touch.y > -10:
            if "line" not in touch.ud:
                global rad
                touch.ud["line"] = Line(points=(touch.x, touch.y), width=rad / 2)
            touch.ud["line"].width = rad / 3.9
            touch.ud["line"].points += [touch.x, touch.y]  # Points are the position
        if 460 > touch.y > -10:
            if "linefbo" not in touch.ud:
                touch.ud["linefbo"] = Line(points=(touch.x, touch.y), width=rad / 2)
            touch.ud["linefbo"].width = rad / 3.9
            touch.ud["linefbo"].points += [touch.x, touch.y]

class Test(TabbedPanel):  # Creates tab panel, all of it is done in kivy that is why we pass
    pass


class CanvasApp(App):
    def build(self):
        return MyMain()


CanvasApp().run()
