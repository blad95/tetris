#bladimirHernandez
#button class:

from graphics import *
from math import *
from graphics import *
from random import *
import pygame
from widgetClass import *

     

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """
        

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('white')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True
        self.activate()
        #self.rect.undraw()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        #print("clicked", p.getX(), p.getY(), self.xmin, self.xmax)
        self.active = True
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.rect.setFill('white')

        self.active = True          #boolean variable that tracks "active"-ness to True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.rect.setFill('lightgray')
        self.rect.setOutline('lightgray')
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False #boolean variable that tracks "active"-ness to False



    def setColor(self,color):
        "Sets this button to a specified color"
        self.rect.setFill(color)
        
    def undraw(self):
        """Undraws the button and deactivates it."""
        self.rect.undraw()
        self.label.undraw()
        self.deactivate()

    def draw(self, gwin):
        """Draws an already defined button and activates it."""
        self.rect.draw(gwin)
        self.label.draw(gwin)
        self.activate()

    def draw(self, win):

        """Draw the object in graphwin, which should be a GraphWin
        object.  A GraphicsObject may only be drawn into one
        window. Raises an error if attempt made to draw an object that
        is already visible."""

        if self.canvas and not self.canvas.isClosed(): raise GraphicsError(OBJ_ALREADY_DRAWN)
        if graphwin.isClosed(): raise GraphicsError("Can't draw to closed window")
        self.canvas = graphwin
        self.id = self._draw(graphwin, self.config)
        if graphwin.autoflush:
            _root.update()

            
    def undraw(self):

        """Undraw the object (i.e. hide it). Returns silently if the
        object is not currently drawn."""
        
        if not self.canvas: return
        if not self.canvas.isClosed():
            self.canvas.delete(self.id)
            if self.canvas.autoflush:
                _root.update()
        self.canvas = None
        self.id = None
