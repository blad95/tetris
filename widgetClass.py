#bladimirHernandez
#widget class:

from math import *
from graphics import *
#from buttonClass import *
from random import *
import pygame
#from widgetClass import *

pygame.init()

class Widget:
    """A widget is the building block that makes up each of the 7 different
    different tetris Objects."""

    def __init__(self,win,center,width,height,color,label):
        """creates a square with these initial coordinates"""
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h

        #p1 and p2 form the two corners of the button
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.color = color
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        self.label = Text(center, label)
        #self.label.draw(win)
        self.active = False
        self.activate()
        #self.rect.undraw()
        
    def clicked(self, p):
        "Returns true if button active and Point p is inside."
        if self.active == True and self.xmin <= p.getX() <= self.xmax\
           and self.ymin <= p.getY() <= self.ymax:
            return True
    
    def getLabel(self):
        "Returns the label string of this button"
        return self.label.getText()
    
    def activate(self):
        "Sets this button to 'active'."
        self.rect.setFill(self.color)
        self.rect.setOutline('black')
        self.label.setStyle('bold')
        self.label.setFill('white')
        self.rect.setWidth(2)
        self.active = True  #boolean variable that tracks "active"-ness to True


    def deactivate(self):
        "Sets this button to 'inactive'"
        self.label.setFill('white')
        self.rect.setWidth(1)
        self.active = False

    def setColor(self,color):
        "Sets this button to a specific color"
        self.rect.setFill(color)
