#bladimirHernandez
#Grid class


from math import *
from graphics import *
from random import *
import pygame
from widgetClass import *
pygame.init()


 
class Grid:
    """A grid of squares/buttons"""
    def __init__(self, win, startX, startY, numCols, numRows, squareWidth, squareHeight,color):
        """initializes a 2D list of blank button objects"""          
        #Set up an instance variable buttonMatrix (a list which will hold lists of buttons)
        self.nCols = numCols
        self.nRows = numRows
        self.widgetMatrix = []

        
        for y in range(numRows, startY, -1):#do it 17 times
            widgetRow = []
            #print("creates a widgetRow!")

            for x in range (startX, numCols):#do it 10 times
                #Button(win, Point(100,130), 70, 20, "Roll Dice", "blue")
                b = Widget(win, Point(x,y), squareWidth,squareHeight, color,'No')
                    #win,center,width,height,color,label):
                #b = b.setColor("white")
                widgetRow.append(b)
                #print("row appended!")
            #one row of buttons is complete, for the current y value
            #add that row to the matrix
            self.widgetMatrix.append(widgetRow)
                

            
    def getClickPos(self, clickPt):
        """returns the column and row number of the button that was clicked
           assumes the point clickPt is in/on the grid"""
        #rounding the x and y value fo the point that was clicked
        #returns interger value that represent the col and row number
        #of the button that was clicked
        #return round(clickPt.getX()), round(clickPt.getY()) 
        print(clickPt.getX(),clickPt.getY())
        for x in range(self.nCols):
            for y in range(self.nRows):
                if self.buttonMatrix[x][y].clicked(clickPt):
                    print("i")
                    print(x,y)
                    return x,y
                    
                    
        
    def setSquareColor(self, x, y, color):
        """set the button at postion [x][y] in the grid to the specified color.
        call this Method upont each click to change the color"""

        self.widgetMatrix[y][x].setColor(color)

    def setRowColor(self,rowNum,color):
        """Will set all buttons in the row to a color"""
        for x in range(self.nRows):
            self.widgetMatrix[x].setColor(color)

