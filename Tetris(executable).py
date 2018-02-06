#Bladimir Hernandez
#Tetris(executable).py

from math import *
from graphics import *
from buttonClass import *
from random import *
import pygame
from widgetClass import *
from gridClass import *
from downwardMotionClass import *
pygame.init()

class L_shape:

    def __init__(self,gameGrid,numCol,numRow):
        self.gameGrid = gameGrid
        self.numCol = numCol
        self.numRow = numRow

        firstX = round(numCol/2)
        
        #colorStuff
        self.color = 'orange'
        
        #color in the boxes in the grid to make the 'L_shape'
        gameGrid.setSquareColor(firstX,numRow,self.color)
        gameGrid.setSquareColor(firstX,numRow-1,self.color)
        gameGrid.setSquareColor(firstX,numRow-2,self.color)
        gameGrid.setSquareColor(firstX+1,numRow-2,self.color)

        self.xPosBox1 = firstX
        self.xPosBox2 = firstX
        self.xPosBox3 = firstX
        self.xPosBox4 = firstX+1

        #y positions of every box
        self.yPosBox1 = numRow
        self.yPosBox2 = numRow-1
        self.yPosBox3 = numRow-2
        self.yPosBox4 = numRow-2
        
        self.label = 'L_shape'
        
    def getLabel(self):
        return self.label
       

    def getXPostionBoxes(self):
        return self.xPosBox1, self.xPosBox2, self.xPosBox3, self.xPosBox4
    
    def getYPostionBoxes(self):
        return self.yPosBox1, self.yPosBox2, self.yPosBox3, self.yPosBox4

    def setXPositionBoxes(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):

        self.xPosBox1 = xPosBox1
        self.xPosBox2 = xPosBox2
        self.xPosBox3 = xPosBox3
        self.xPosBox4 = xPosBox4

        return xPosBox1, xPosBox2,xPosBox3,xPosBox4

    def setYPositionBoxes(self,yPosBox1,yPosBox2,yPosBox3,yPosBox4):

        self.yPosBox1 = yPosBox1
        self.yPosBox2 = yPosBox2
        self.yPosBox3 = yPosBox3
        self.yPosBox4 = yPosBox4

        return yPosBox1, yPosBox2,yPosBox3,yPosBox4
    
    def getColor(self):

        return self.color

        
class J_shape:

    def __init__(self,gameGrid,numCol,numRow):
        self.gameGrid = gameGrid
        self.numCol = numCol
        self.numRow = numRow

        firstX = round(numCol/2)
        #colorStuff
        self.color = 'blue'       

        #color in the boxes in the grid to make the 'J_shape'
        gameGrid.setSquareColor(firstX,numRow,self.color)
        gameGrid.setSquareColor(firstX,numRow-1,self.color)
        gameGrid.setSquareColor(firstX,numRow-2,self.color)
        gameGrid.setSquareColor(firstX-1,numRow-2,self.color)
        
        self.xPosBox1 = firstX
        self.xPosBox2 = firstX
        self.xPosBox3 = firstX
        self.xPosBox4 = firstX-1

        #y positions of every box
        self.yPosBox1 = numRow
        self.yPosBox2 = numRow-1
        self.yPosBox3 = numRow-2
        self.yPosBox4 = numRow-2
        
        self.label = 'J_shape'
    
    def getLabel(self):
        return self.label
       
    def getXPostionBoxes(self):
        return self.xPosBox1, self.xPosBox2, self.xPosBox3, self.xPosBox4
    
    def getYPostionBoxes(self):
        return self.yPosBox1, self.yPosBox2, self.yPosBox3, self.yPosBox4

    def setXPositionBoxes(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):

        self.xPosBox1 = xPosBox1
        self.xPosBox2 = xPosBox2
        self.xPosBox3 = xPosBox3
        self.xPosBox4 = xPosBox4

        return xPosBox1, xPosBox2,xPosBox3,xPosBox4

    def setYPositionBoxes(self,yPosBox1,yPosBox2,yPosBox3,yPosBox4):

        self.yPosBox1 = yPosBox1
        self.yPosBox2 = yPosBox2
        self.yPosBox3 = yPosBox3
        self.yPosBox4 = yPosBox4

        return yPosBox1, yPosBox2,yPosBox3,yPosBox4
    
    def getColor(self):

        return self.color

class O_shape:

    def __init__(self,gameGrid,numCol,numRow):
        self.gameGrid = gameGrid
        self.numCol = numCol
        self.numrow = numRow

        #colorStuff
        self.color = "yellow"

        firstX = round(numCol/2)
        
        #color in the boxes in the grid to make the 'O_shape'
        gameGrid.setSquareColor(firstX,numRow,self.color)#first box
        gameGrid.setSquareColor(firstX+1,numRow,self.color)#second...
        gameGrid.setSquareColor(firstX+1 ,numRow-1,self.color)
        gameGrid.setSquareColor(firstX,numRow-1,self.color)
        
        self.xPosBox1 = firstX
        self.xPosBox2 = firstX+1
        self.xPosBox3 = firstX+1
        self.xPosBox4 = firstX

        #y positions of every box
        self.yPosBox1 = numRow
        self.yPosBox2 = numRow
        self.yPosBox3 = numRow-1
        self.yPosBox4 = numRow-1
        
        self.label = 'O_shape'
    
    def getLabel(self):
        return self.label
       


    def getXPostionBoxes(self):
        return self.xPosBox1, self.xPosBox2, self.xPosBox3, self.xPosBox4
    
    def getYPostionBoxes(self):
        return self.yPosBox1, self.yPosBox2, self.yPosBox3, self.yPosBox4

    def setXPositionBoxes(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):

        self.xPosBox1 = xPosBox1
        self.xPosBox2 = xPosBox2
        self.xPosBox3 = xPosBox3
        self.xPosBox4 = xPosBox4

        return xPosBox1, xPosBox2,xPosBox3,xPosBox4

    def setYPositionBoxes(self,yPosBox1,yPosBox2,yPosBox3,yPosBox4):

        self.yPosBox1 = yPosBox1
        self.yPosBox2 = yPosBox2
        self.yPosBox3 = yPosBox3
        self.yPosBox4 = yPosBox4

        return yPosBox1, yPosBox2,yPosBox3,yPosBox4
    
    def getColor(self):

        return self.color
       
class T_shape:

    def __init__(self,gameGrid,numCol,numRow):
        self.gameGrid = gameGrid
        self.numCol = numCol
        self.numRow = numRow

        firstX = round(numCol/2)
        #colorStuff
        self.color = 'purple'
            
        #color in the boxes in the grid to make the 'T_shape'
        gameGrid.setSquareColor(firstX,numRow,self.color)
        gameGrid.setSquareColor(firstX,numRow-1,self.color)
        gameGrid.setSquareColor(firstX-1,numRow-1,self.color)
        gameGrid.setSquareColor(firstX+1,numRow-1,self.color)
        
        self.xPosBox1 = firstX
        self.xPosBox2 = firstX
        self.xPosBox3 = firstX-1
        self.xPosBox4 = firstX+1

        #y positions of every box
        self.yPosBox1 = numRow
        self.yPosBox2 = numRow-1
        self.yPosBox3 = numRow-1
        self.yPosBox4 = numRow-1
     
        self.label = 'T_shape'
    
    def getLabel(self):
        return self.label
       

    def getXPostionBoxes(self):
        return self.xPosBox1, self.xPosBox2, self.xPosBox3, self.xPosBox4
    def getYPostionBoxes(self):
        return self.yPosBox1, self.yPosBox2, self.yPosBox3, self.yPosBox4
    
    def setXPositionBoxes(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):

        self.xPosBox1 = xPosBox1
        self.xPosBox2 = xPosBox2
        self.xPosBox3 = xPosBox3
        self.xPosBox4 = xPosBox4

        return xPosBox1, xPosBox2,xPosBox3,xPosBox4

    def setYPositionBoxes(self,yPosBox1,yPosBox2,yPosBox3,yPosBox4):

        self.yPosBox1 = yPosBox1
        self.yPosBox2 = yPosBox2
        self.yPosBox3 = yPosBox3
        self.yPosBox4 = yPosBox4

        return yPosBox1, yPosBox2,yPosBox3,yPosBox4
    
    def getColor(self):

        return self.color

    
    def getLabel(self):
        return self.label
    
class s_shape:

    def __init__(self,gameGrid,numCol,numRow):
        self.gameGrid = gameGrid
        self.numCol = numCol
        self.numRow = numRow

        firstX = round(numCol/2)
        #colorStuff
        self.color = 'green'

        #color in the boxes in the grid to make the 's_shape'
        gameGrid.setSquareColor(firstX,numRow,self.color)
        gameGrid.setSquareColor(firstX,numRow -1,self.color)
        gameGrid.setSquareColor(firstX-1,numRow -1,self.color)
        gameGrid.setSquareColor(firstX+1,numRow,self.color)
        

        self.xPosBox1 = firstX
        self.xPosBox2 = firstX
        self.xPosBox3 = firstX-1
        self.xPosBox4 = firstX+1

        #y positions of every box
        self.yPosBox1 = numRow
        self.yPosBox2 = numRow-1
        self.yPosBox3 = numRow-1
        self.yPosBox4 = numRow

        self.label = 's_shape'
    



    def getXPostionBoxes(self):
        return self.xPosBox1, self.xPosBox2, self.xPosBox3, self.xPosBox4
    
    def getYPostionBoxes(self):
        return self.yPosBox1, self.yPosBox2, self.yPosBox3, self.yPosBox4

    def setXPositionBoxes(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):

        self.xPosBox1 = xPosBox1
        self.xPosBox2 = xPosBox2
        self.xPosBox3 = xPosBox3
        self.xPosBox4 = xPosBox4

        return xPosBox1, xPosBox2,xPosBox3,xPosBox4

    def setYPositionBoxes(self,yPosBox1,yPosBox2,yPosBox3,yPosBox4):

        self.yPosBox1 = yPosBox1
        self.yPosBox2 = yPosBox2
        self.yPosBox3 = yPosBox3
        self.yPosBox4 = yPosBox4

        return yPosBox1, yPosBox2,yPosBox3,yPosBox4
    
    def getColor(self):

        return self.color

    def getLabel(self):
        return self.label
 
class z_shape:

    def __init__(self, gameGrid, numCol, numRow): #TODO: add direction

        #color in the boxes in the grid to make the 'z_shape'
        
        self.numCol = 9
        self.numRow = 19
        self.gameGrid = gameGrid
        
        firstX = round(numCol/2)
        #colorStuff
        self.color = 'red'

        gameGrid.setSquareColor(firstX,numRow,self.color)    #first colored box
        gameGrid.setSquareColor(firstX+1,numRow,self.color)  #second colored box
        gameGrid.setSquareColor(firstX+1,numRow-1,self.color)#third colored box
        gameGrid.setSquareColor(firstX+2,numRow-1,self.color)#fourth colored box
        self.xPosBox1 = firstX
        self.xPosBox2 = firstX+1
        self.xPosBox3 = firstX+1
        self.xPosBox4 = firstX+2

        #y positions of every box
        self.yPosBox1 = numRow
        self.yPosBox2 = numRow
        self.yPosBox3 = numRow-1
        self.yPosBox4 = numRow-1

        #label to indicate its shape
        self.label = 'z_shape'

    def getXPostionBoxes(self):
        return self.xPosBox1, self.xPosBox2, self.xPosBox3, self.xPosBox4
    
    def getYPostionBoxes(self):
        return self.yPosBox1, self.yPosBox2, self.yPosBox3, self.yPosBox4

    def setXPositionBoxes(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):

        self.xPosBox1 = xPosBox1
        self.xPosBox2 = xPosBox2
        self.xPosBox3 = xPosBox3
        self.xPosBox4 = xPosBox4

        return xPosBox1, xPosBox2,xPosBox3,xPosBox4

    def setYPositionBoxes(self,yPosBox1,yPosBox2,yPosBox3,yPosBox4):

        self.yPosBox1 = yPosBox1
        self.yPosBox2 = yPosBox2
        self.yPosBox3 = yPosBox3
        self.yPosBox4 = yPosBox4

        return yPosBox1, yPosBox2,yPosBox3,yPosBox4
    
    def getColor(self):

        return self.color
    
    def getLabel(self):
        return self.label

class l_shape:

    def __init__(self, gameGrid, numCol, numRow): #TODO: add direction

        #color in the boxes in the grid to make the 'l_shape'
        self.gameGrid = gameGrid
        self.numCol = 9
        self.numRow = 19

        firstX = round(numCol/2)
        #colorStuff
        self.color = 'blue'

        gameGrid.setSquareColor(firstX,numRow,self.color)    #first colored box
        gameGrid.setSquareColor(firstX,numRow-1,self.color)  #second colored box
        gameGrid.setSquareColor(firstX,numRow-2,self.color)#third colored box
        gameGrid.setSquareColor(firstX,numRow-3,self.color)#fourth colored box

        self.xPosBox1 = firstX
        self.xPosBox2 = firstX
        self.xPosBox3 = firstX
        self.xPosBox4 = firstX

        #y positions of every box
        self.yPosBox1 = numRow
        self.yPosBox2 = numRow-1
        self.yPosBox3 = numRow-2
        self.yPosBox4 = numRow-3

        #label to indicate its shape
        self.label = 'l_shape'

    def getXPostionBoxes(self):
        return self.xPosBox1, self.xPosBox2, self.xPosBox3, self.xPosBox4
    
    def getYPostionBoxes(self):
        return self.yPosBox1, self.yPosBox2, self.yPosBox3, self.yPosBox4
    
    def setXPositionBoxes(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):

        self.xPosBox1 = xPosBox1
        self.xPosBox2 = xPosBox2
        self.xPosBox3 = xPosBox3
        self.xPosBox4 = xPosBox4

        return xPosBox1, xPosBox2,xPosBox3,xPosBox4

    def moveRight(self,xPosBox1,xPosBox2,xPosBox3,xPosBox4):
        self.xPosBox1 = xPosBox1 +1
        self.xPosBox2 = xPosBox2 +1
        self.xPosBox3 = xPosBox3 +1
        self.xPosBox4 = xPosBox4 +1

        return xPosBox1,xPosBox2,xPosBox3,xPosBox4

    def setYPositionBoxes(self,yPosBox1,yPosBox2,yPosBox3,yPosBox4):

        self.yPosBox1 = yPosBox1
        self.yPosBox2 = yPosBox2
        self.yPosBox3 = yPosBox3
        self.yPosBox4 = yPosBox4

        return yPosBox1, yPosBox2,yPosBox3,yPosBox4
    
    def getColor(self):

        return self.color
    
    
    def getLabel(self):
        return self.label

def file_read(filename):
    #File reader - reads the file named 'filename'.txt
    
    file = open(filename + ".txt", "r") #opens file named 'filename'.txt
    readFile = file.read() #reads the whole file as a string    **
    return readFile #returns one string containing the whole text       
       
def startMenu():

    #create a window for the GUI
    startWin = GraphWin("Welcome!", 900,650)
    startWin.setBackground("dodgerblue")
    
    welcomeText = file_read('welcome')
    welcomeText = Text(Point(450,100), welcomeText) #the text is displayed
    welcomeText.setFill("Black")
    welcomeText.setStyle("bold")
    welcomeText.setSize(36)
    welcomeText.draw(startWin)

    
    #create and color the 'start' button
    startButton = Button(startWin, Point(450,350), 200,75, '')
    startButton.setColor("green")
    
    startLabel = "Start"
    startLabel = Text(Point(450,350),startLabel)
    startLabel.setFill("white")
    startLabel.setStyle("bold")
    startLabel.setSize(26)
    startLabel.draw(startWin)

    #create and color the 'exit' button
    ExitButton = Button(startWin, Point(450, 450), 200, 75, '')
    ExitButton.setColor("red")
    
    exitLabel = "Exit"
    exitLabel = Text(Point(450,450),exitLabel)
    exitLabel.setFill("white")
    exitLabel.setStyle("bold")
    exitLabel.setSize(26)
    exitLabel.draw(startWin)

    #create and color the 'about' button
    aboutButton = Button(startWin, Point(110,550),200,75,'')
    aboutButton.setColor("orange")
    
    aboutLabel = "About"
    aboutLabel = Text(Point(110,550),aboutLabel)
    aboutLabel.setFill("white")
    aboutLabel.setStyle("bold")
    aboutLabel.setSize(26)
    aboutLabel.draw(startWin)

    #create and color the 'how to play' button
    howToButton = Button(startWin, Point(790,550),200,75,'')
    howToButton.setColor("yellow")

    howToLabel = "How To Play"
    howToLabel = Text(Point(790,550),howToLabel)
    howToLabel.setFill("white")
    howToLabel.setStyle("bold")
    howToLabel.setSize(26)
    howToLabel.draw(startWin)
    

    pt = startWin.getMouse()

    if ( ExitButton.clicked(pt) ):
        #close the windows
        startWin.close()

    if ( startButton.clicked(pt) ):
        #close the windows
        startWin.close()
        gameWindow()
        
    if ( aboutButton.clicked(pt) ):
        #close the windows
        #startWin.close()
        startWin.close()
        aboutMenu()

    if ( howToButton.clicked(pt) ):
        startWin.close()
        #open the how to play window
        helpMenu()

def helpMenu():
    helpWin = GraphWin("Info", 900, 650)
    helpWin.setCoords(0,0,900,650)
    helpWin.setBackground("dodgerblue")
    #read the how to play text file
    helpInstructions = file_read('help')

    helpInstructions = Text(Point(450,425), helpInstructions) #the text is displayed
    helpInstructions.setFill("white")
    helpInstructions.setStyle("bold")
    helpInstructions.setSize(24)
    helpInstructions.draw(helpWin)

    #create and color the 'back' button
    backButton = Button(helpWin, Point(790,550),200,75,'')
    backButton.setColor("yellow")

    backLabel = "Back"
    backLabel = Text(Point(790,550),backLabel)
    backLabel.setFill("white")
    backLabel.setStyle("bold")
    backLabel.setSize(26)
    backLabel.draw(helpWin)

    pt = helpWin.getMouse()
    
    if ( backButton.clicked(pt) ):
        helpWin.close()
        #open the how to play window
        startMenu()

def aboutMenu():
    
    aboutWin = GraphWin("About", 900, 650)
    aboutWin.setCoords(0,0,900,650)
    aboutWin.setBackground("dodgerblue")
    #read the "about.txt file"
    aboutText = file_read('advisory')
    
    aboutText = Text(Point(450,325), aboutText) #the text is displayed
    aboutText.setFill("white")
    aboutText.setStyle("bold")
    aboutText.setSize(24)
    aboutText.draw(aboutWin)

    #create and color the 'back' button
    backButton = Button(aboutWin, Point(790,550),200,75,'')
    backButton.setColor("orange")

    backLabel = "Back"
    backLabel = Text(Point(790,550),backLabel)
    backLabel.setFill("white")
    backLabel.setStyle("bold")
    backLabel.setSize(26)
    backLabel.draw(aboutWin)

    pt = aboutWin.getMouse()
    
    if ( backButton.clicked(pt) ):
        aboutWin.close()
        #open the how to play window
        startMenu()


def gameWindow():

    def createRandomTetris():
        
        #generate random tetris objects
        randomTetrisObjects= []
        for i in range(10):
            j = randrange(1,7)

            randomTetrisObjects.append(j)
        print(randomTetrisObjects) #contains 10 objects


        #z = randrange(1,7)
        for z in randomTetrisObjects:
            
            if ( z == 1 ):
                #if the integer is 1, assign it to a tetris object
                return l_shape(gameGrid, numCol, numRow)
            
            if ( z == 2):
                return L_shape(gameGrid, numCol, numRow)
            
            if ( z == 3):
                return J_shape(gameGrid, numCol, numRow)

            if ( z == 4):
                return O_shape(gameGrid, numCol, numRow)

            if ( z == 5):
                return z_shape(gameGrid, numCol, numRow)

            if ( z == 6):
                return T_shape(gameGrid, numCol, numRow)

            if ( z == 7):
                return s_shape(gameGrid, numCol, numRow)


    
    gameWin = GraphWin("Tetris", 600, 600)
    gameWin.setCoords(-3, 22, 22, -3)    #make the bakground sky blue
    gameWin.setBackground("dodgerblue")

    

    ##add code here that creates a quitButton
    quitButton = Button(gameWin, Point(20,-2), 3,1, 'Quit')
    quitButton.setColor("red")

    #makeGrid(win,startX,startY, numCols, numRows, squareWidth, squareHeight, color)
    gameGrid = Grid(gameWin, 0, 0, 10, 20, 1, 1,'white')

    #hardcode the numCol and numRow variables
    numCol = 9
    numRow = 19
    
#create a random object
    
    #random tetris
    #tetris_object = createRandomTetris()

    #specific tetris code
    tetris_object = L_shape(gameGrid, numCol, numRow)
    
    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()
    
    #make a list to place x1,x2,x3,x4    
    xPos = [x1,x2,x3,x4]
    yPos = [y1,y2,y3,y4]


    #game is in play##
        
    while (True):
        
        #create the first object
        downwardMotion(gameGrid,tetris_object,xPos,yPos)

        #random tetris
        #tetris_object = createRandomTetris()

        #specific tetris code
        tetris_object = L_shape(gameGrid, numCol, numRow)
        
        x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
        y1,y2,y3,y4 = tetris_object.getYPostionBoxes()
        
        #make a list to place x1,x2,x3,x4    
        xPos = [x1,x2,x3,x4]
        yPos = [y1,y2,y3,y4]
        
        #pt = gameWin.getMouse()



#    l_object = TestButton.make_l_shape()



##    while not quitButton.clicked(pt):
##        pt = gameWin.getMouse()
##        print(round(pt.getX()), round(pt.getY()))
##        if -.5 <= pt.getX() <= 19.5 and -.5 <= pt.getY() < 19.5:
##            pt_x, pt_y = grid.getClickPos(pt)
##            grid.setSquareColor(pt_x,pt_y,"blue")
##            grid.setRowColor(pt_x,"blue")
##            print(pt_x, pt_y, "clicked",pt.getX(),pt.getY())
##        #if quitButton.clicked(pt):
##            #quitButton.activate()
##        pt = gameWin.getMouse()
##        


    gameWin.close()




startMenu()
#helpMenu()
#aboutMenu()
#gameWindow()
