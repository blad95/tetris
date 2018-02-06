#downwardMotion Class


from math import *
from graphics import *
from buttonClass import *
from random import *
import pygame
from widgetClass import *
from gridClass import *
pygame.init()



#rotation functions:
def rotate_top_to_right(x,y,theta):

    x_r = round((0)*cos(theta) + (1)*sin(theta))
    y_r = round((1)*sin(theta) + (0)*cos(theta))

    dir_x1 = x + x_r
    dir_y1 = y - y_r

    return dir_x1,dir_y1

def rotate_right_to_bottom(x,y,theta):

    x_r = abs(round((0)*cos(theta) - (1)*sin(theta)))
    y_r = abs(round((1)*sin(theta*-1) + (0)*cos(theta*-1)))

    dir_x1 = x - x_r
    dir_y1 = y - y_r

    return dir_x1,dir_y1

def rotate_bottom_to_right(x,y,theta):

    x_r = abs(round((0)*cos(theta) - (1)*sin(theta)))
    y_r = abs(round((1)*sin(theta*-1) + (0)*cos(theta*-1)))

    dir_x1 = x + x_r
    dir_y1 = y - y_r

    return dir_x1,dir_y1

def rotate_bottom_to_left(x,y,theta):

    x_r = round((0)*cos(theta) - (-1)*sin(theta))
    y_r = round((0)*cos(theta) - (-1)*sin(theta))

    dir_x3 = x - x_r
    dir_y3 = y + y_r
    
    return dir_x3, dir_y3

def rotate_bottom_to_left2(x,y,theta):

    x_r = round((0)*cos(theta) - (-2)*sin(theta))
    y_r = round((0)*cos(theta) - (-2)*sin(theta))

    dir_x4 = x - x_r
    dir_y4 = y + y_r
    
    
    return dir_x4, dir_y4



def rotate_left_to_top(x,y,theta):

    x_r = round((0)*cos(theta) - (-1)*sin(theta))
    y_r = round((-1)*sin(theta*-1)+ (0)*cos(theta*-1))

    dir_x3 = x - x_r
    dir_y3 = y - y_r

    
    return dir_x3,dir_y3

def rotate_left_to_top2(x,y,theta):

    x_r = round((0)*cos(theta) - (-2)*sin(theta))
    y_r = round((-2)*sin(theta*-1)+ (0)*cos(theta*-1))

    dir_x4 = x - x_r
    dir_y4 = y - y_r

    
    return dir_x4,dir_y4


#downward motion(self,gameGrid,tetris_object,xPos,yPos)
class downwardMotion:
    def __init__(self,gameGrid,tetris_object,xPos,yPos):

        self.gameGrid = gameGrid
        self.tetris_object = tetris_object
        
        #read in the values stored in xPos and yPos
        x1 = xPos[0]
        x2 = xPos[1]
        x3 = xPos[2]
        x4 = xPos[3]

        y1 = yPos[0]
        y2 = yPos[1]
        y3 = yPos[2]
        y4 = yPos[3]

        count = 0

        l_isFlat = False
        s_isFlat = True
        
        while (x1 > 0 and x2 >0 and x3>0 and x4>0):
            
            while( y1 >1 and y2>1 and y3>1 and y4>1):

                #create an instance var. that will make the 2nd box the center

                #center_of_oject
                xC = x2
                yC = y2
                
                print(x1,x2,x3,x4)
                print(y1,y2,y3,y4)

                if ( tetris_object.getLabel() == 'O_shape' ):
                    #print("this object is O_shape-d")
                              
                    #print("this object is l_shape-d")
                   
                    #create a new object
                    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
                    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()

##                    #print the positions
##                    print(x1,x2,x3,x4)
##                    print(y1,y2,y3,y4)
##                    
                    dir_x1 = x1
                    dir_x2 = x2
                    dir_x3 = x3
                    dir_x4 = x4
                    
                    ##  x-direction stuff goes here  ##


                    for event in pygame.event.get():
                        if (event.type==pygame.KEYDOWN):
                            
                            if (event.key==pygame.K_LEFT):
                                #add 1 to the x positions of all boxes
                                dir_x1 = x1 -1
                                dir_x2 = x2 -1
                                dir_x3 = x3 -1
                                dir_x4 = x4 -1
                                #moveX = -5
                            if (event.key==pygame.K_RIGHT):
                                #subtract
                                dir_x1 = x1 +1
                                dir_x2 = x2 +1
                                dir_x3 = x3 +1
                                dir_x4 = x4 +1
                                #moveX = 5
                            if (event.key==pygame.K_UP):
                                #rotate counterclowise
                                moveY = -5
                            if (event.key==pygame.K_DOWN):
                                #rotateclockwise
                                moveY = 5
                                
                    #erase the APPROPRIATE previous yPositions
                    previousY1 = y1
                    previousY2 = y2
                    previousY3 = y3
                    previousY4 = y4

                    #color these coordinates 'white'
                    gameGrid.setSquareColor( x1, previousY1, 'white')
                    gameGrid.setSquareColor( x2, previousY2, 'white')
                    gameGrid.setSquareColor( x3, previousY3, 'white')
                    gameGrid.setSquareColor( x4, previousY4, 'white')
                    
                    #make it go down by subtracting fromt he yPosBox<#>
                    lower_y1 = y1-1
                    lower_y2 = y2-1
                    lower_y3 = y3-1
                    lower_y4 = y4-1
                            
                    #set the newPositions ( Y )
                    tetris_object.setXPositionBoxes(dir_x1,dir_x2,dir_x3,dir_x4)
                    tetris_object.setYPositionBoxes(lower_y1 ,lower_y2 ,lower_y3 ,lower_y4 )
                    
                    #create the object in the grid
                    gameGrid.setSquareColor( dir_x1, lower_y1, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x2, lower_y2, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x3, lower_y3, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x4, lower_y4, tetris_object.getColor())

                if ( tetris_object.getLabel() == 'l_shape' ):
                    #create a new object
                    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
                    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()
                    
##                  #get the x positions
                    dir_x1 = x1
                    dir_x2 = x2
                    dir_x3 = x3
                    dir_x4 = x4

                    #get the y positions
                    dir_y1 = y1
                    dir_y2 = y2
                    dir_y3 = y3
                    dir_y4 = y4

                    
                    for event in pygame.event.get():
                        if (event.type==pygame.KEYDOWN):
                            
                            if (event.key==pygame.K_LEFT):
                                
                                dir_x1 = x1 -1
                                dir_x2 = x2 -1
                                dir_x3 = x3 -1
                                dir_x4 = x4 -1
                                
                            if (event.key==pygame.K_RIGHT):
                                
                                dir_x1 = x1 +1
                                dir_x2 = x2 +1
                                dir_x3 = x3 +1
                                dir_x4 = x4 +1
                                
                            if (event.key==pygame.K_UP):

                                if (l_isFlat == False):
                                #rotate counterclowise

                                    #make it flat:
                                    dir_x1, dir_y1 = rotate_top_to_right(x1,y1,90)
                                    dir_x3, dir_y3 = rotate_bottom_to_left(x3,y3,90)
                                    dir_x4, dir_y4 = rotate_bottom_to_left2(x4,y4,90)
                                    isFlat = True

##                                #if it is already flat    
                                else:
                                    dir_x1, dir_y1 = rotate_top_to_right(x1,y1,-90)
                                    dir_x3, dir_y3 = rotate_bottom_to_left(x3,y3,-90)
                                    dir_x4, dir_y4 = rotate_bottom_to_left2(x4,y4,-90)

                                    isFlat = False
                                    
                                
                            if (event.key==pygame.K_DOWN):


                                if (l_isFlat == False):
                                #rotate counterclowise

                                    #make it flat:
                                    dir_x1, dir_y1 = rotate_top_to_right(x1,y1,90)
                                    dir_x3, dir_y3 = rotate_bottom_to_left(x3,y3,90)
                                    dir_x4, dir_y4 = rotate_bottom_to_left2(x4,y4,90)
                                    l_isFlat = True

                                #if it is already flat    
                                else:
                                    dir_x1, dir_y1 = rotate_top_to_right(x1,y1,-90)
                                    dir_x3, dir_y3 = rotate_bottom_to_left(x3,y3,-90)
                                    dir_x4, dir_y4 = rotate_bottom_to_left2(x4,y4,-90)

                                    l_isFlat = False
                                    

                    #erase the APPROPRIATE previous yPositions
                    previousY1 = y1
                    previousY2 = y2
                    previousY3 = y3
                    previousY4 = y4

                    #color these coordinates 'white'
                    gameGrid.setSquareColor( x1, previousY1, 'white')
                    gameGrid.setSquareColor( x2, previousY2, 'white')
                    gameGrid.setSquareColor( x3, previousY3, 'white')
                    gameGrid.setSquareColor( x4, previousY4, 'white')
                    
                    #make it go down by subtracting fromt the yPosBox<#>
                    lower_y1 = dir_y1-1
                    lower_y2 = dir_y2-1
                    lower_y3 = dir_y3-1
                    lower_y4 = dir_y4-1
                            
                    #set the newPositions ( Y )
                    tetris_object.setXPositionBoxes(dir_x1,dir_x2,dir_x3,dir_x4)
                    tetris_object.setYPositionBoxes(lower_y1 ,lower_y2 ,lower_y3 ,lower_y4 )

                    #create the object in the grid
                    gameGrid.setSquareColor( dir_x1, lower_y1, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x2, lower_y2, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x3, lower_y3, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x4, lower_y4, tetris_object.getColor())

                    x1 = dir_x1
                    x2 = dir_x2
                    x3 = dir_x3
                    x4 = dir_x4

                    y1 = dir_y1
                    y2 = dir_y2
                    y3 = dir_y3
                    y4 = dir_y4
                        

                    


                if ( tetris_object.getLabel() == 's_shape' ):
                    #create a new object
                    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
                    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()

##                    #print the positions
##                    print(x1,x2,x3,x4)
##                    print(y1,y2,y3,y4)
##                    
##                  #get the x positions
                    dir_x1 = x1
                    dir_x2 = x2
                    dir_x3 = x3
                    dir_x4 = x4

                    #get the y positions
                    dir_y1 = y1
                    dir_y2 = y2
                    dir_y3 = y3
                    dir_y4 = y4


                    
                    ##  x-direction stuff goes here  ##
                    for event in pygame.event.get():
                        if (event.type==pygame.KEYDOWN):
                            
                            if (event.key==pygame.K_LEFT):
                                #add 1 to the x positions of all boxes
                                dir_x1 = x1 -1
                                dir_x2 = x2 -1
                                dir_x3 = x3 -1
                                dir_x4 = x4 -1
                                #moveX = -5
                            if (event.key==pygame.K_RIGHT):
                                #subtract
                                dir_x1 = x1 +1
                                dir_x2 = x2 +1
                                dir_x3 = x3 +1
                                dir_x4 = x4 +1
                                #moveX = 5
                               
                            if (event.key==pygame.K_UP):


                                if (s_isFlat == True):
                                #rotate counterclowise

                                    #make it turns 90 to the right:
                                    
                                    dir_x2, dir_y2 = rotate_bottom_to_left(x2,y2,90)
                                    dir_y3 = dir_y3 + 2
                                    dir_x4, dir_y4 = rotate_right_to_bottom(x4,y4,-90)
                                    print("flat")
                                    s_isFlat = False
                                    

                                #if it is not flat    
                                else:
                                    print("not flat")
                                    dir_x2, dir_y2 = rotate_bottom_to_left(x2,y2,-90)
                                    dir_y3 = dir_y3 - 2
                                    dir_x4, dir_y4 = rotate_bottom_to_right(x4,y4,90)
                                    s_isFlat = True
##                                    
                                
                            if (event.key==pygame.K_DOWN):
                                #rotateclockwise
                                
                                if (s_isFlat == True):
                                #rotate counterclowise

                                    #make it turns 90 to the right:
                                    
                                    dir_x2, dir_y2 = rotate_bottom_to_left(x2,y2,90)
                                    dir_y3 = dir_y3 + 2
                                    dir_x4, dir_y4 = rotate_right_to_bottom(x4,y4,-90)
                                    print("flat")
                                    s_isFlat = False
                                    

                                #if it is not flat    
                                else:
                                    print("not flat")
                                    dir_x2, dir_y2 = rotate_bottom_to_left(x2,y2,-90)
                                    dir_y3 = dir_y3 - 2
                                    dir_x4, dir_y4 = rotate_bottom_to_right(x4,y4,90)
                                    s_isFlat = True
##                                    
                                
##                                    
                    #erase the APPROPRIATE previous yPositions
                    previousY1 = y1
                    previousY2 = y2
                    previousY3 = y3
                    previousY4 = y4

                    #color these coordinates 'white'
                    gameGrid.setSquareColor( x1, previousY1, 'white')
                    gameGrid.setSquareColor( x2, previousY2, 'white')
                    gameGrid.setSquareColor( x3, previousY3, 'white')
                    gameGrid.setSquareColor( x4, previousY4, 'white')
                    
                    #make it go down by subtracting fromt he yPosBox<#>
                    lower_y1 = dir_y1-1
                    lower_y2 = dir_y2-1
                    lower_y3 = dir_y3-1
                    lower_y4 = dir_y4-1
                            
                    #set the newPositions ( Y )
                    tetris_object.setXPositionBoxes(dir_x1,dir_x2,dir_x3,dir_x4)
                    tetris_object.setYPositionBoxes(lower_y1 ,lower_y2 ,lower_y3 ,lower_y4 )
                    #create the object in the grid
                    gameGrid.setSquareColor( dir_x1, lower_y1, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x2, lower_y2, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x3, lower_y3, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x4, lower_y4, tetris_object.getColor())
                    
                    x1 = dir_x1
                    x2 = dir_x2
                    x3 = dir_x3
                    x4 = dir_x4

                    y1 = dir_y1
                    y2 = dir_y2
                    y3 = dir_y3
                    y4 = dir_y4

############################ ############################ ############################
            
                if ( tetris_object.getLabel() == 'L_shape' ):
                    #create a new object
                    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
                    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()
##                    
                    dir_x1 = x1
                    dir_x2 = x2
                    dir_x3 = x3
                    dir_x4 = x4
                    
                    ##  x-direction stuff goes here  ##


                    for event in pygame.event.get():
                        if (event.type==pygame.KEYDOWN):
                            
                            if (event.key==pygame.K_LEFT):
                                #add 1 to the x positions of all boxes
                                dir_x1 = x1 -1
                                dir_x2 = x2 -1
                                dir_x3 = x3 -1
                                dir_x4 = x4 -1
                                #moveX = -5
                            if (event.key==pygame.K_RIGHT):
                                #subtract
                                dir_x1 = x1 +1
                                dir_x2 = x2 +1
                                dir_x3 = x3 +1
                                dir_x4 = x4 +1
                                #moveX = 5
                            if (event.key==pygame.K_UP):
                                #rotate counterclowise
                                moveY = -5
                            if (event.key==pygame.K_DOWN):
                                #rotateclockwise
                                moveY = 5
                    #erase the APPROPRIATE previous yPositions
                    previousY1 = y1
                    previousY2 = y2
                    previousY3 = y3
                    previousY4 = y4

                    #color these coordinates 'white'
                    gameGrid.setSquareColor( x1, previousY1, 'white')
                    gameGrid.setSquareColor( x2, previousY2, 'white')
                    gameGrid.setSquareColor( x3, previousY3, 'white')
                    gameGrid.setSquareColor( x4, previousY4, 'white')
                    
                    #make it go down by subtracting fromt he yPosBox<#>
                    lower_y1 = y1-1
                    lower_y2 = y2-1
                    lower_y3 = y3-1
                    lower_y4 = y4-1
                            
                    #set the newPositions ( Y )
                    tetris_object.setXPositionBoxes(dir_x1,dir_x2,dir_x3,dir_x4)
                    tetris_object.setYPositionBoxes(lower_y1 ,lower_y2 ,lower_y3 ,lower_y4 )
                    #create the object in the grid
                    gameGrid.setSquareColor( dir_x1, lower_y1, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x2, lower_y2, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x3, lower_y3, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x4, lower_y4, tetris_object.getColor())

                if ( tetris_object.getLabel() == 'J_shape' ):
                    #create a new object
                    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
                    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()

##                    #print the positions
##                    print(x1,x2,x3,x4)
##                    print(y1,y2,y3,y4)
##                    
                    dir_x1 = x1
                    dir_x2 = x2
                    dir_x3 = x3
                    dir_x4 = x4
                    
                    ##  x-direction stuff goes here  ##


                    for event in pygame.event.get():
                        if (event.type==pygame.KEYDOWN):
                            
                            if (event.key==pygame.K_LEFT):
                                #add 1 to the x positions of all boxes
                                dir_x1 = x1 -1
                                dir_x2 = x2 -1
                                dir_x3 = x3 -1
                                dir_x4 = x4 -1
                                #moveX = -5
                            if (event.key==pygame.K_RIGHT):
                                #subtract
                                dir_x1 = x1 +1
                                dir_x2 = x2 +1
                                dir_x3 = x3 +1
                                dir_x4 = x4 +1
                                #moveX = 5
                            if (event.key==pygame.K_UP):
                                #rotate counterclowise
                                moveY = -5
                            if (event.key==pygame.K_DOWN):
                                #rotateclockwise
                                moveY = 5
                    #erase the APPROPRIATE previous yPositions
                    previousY1 = y1
                    previousY2 = y2
                    previousY3 = y3
                    previousY4 = y4

                    #color these coordinates 'white'
                    gameGrid.setSquareColor( x1, previousY1, 'white')
                    gameGrid.setSquareColor( x2, previousY2, 'white')
                    gameGrid.setSquareColor( x3, previousY3, 'white')
                    gameGrid.setSquareColor( x4, previousY4, 'white')
                    
                    #make it go down by subtracting fromt he yPosBox<#>
                    lower_y1 = y1-1
                    lower_y2 = y2-1
                    lower_y3 = y3-1
                    lower_y4 = y4-1
                            
                    #set the newPositions ( Y )
                    tetris_object.setXPositionBoxes(dir_x1,dir_x2,dir_x3,dir_x4)
                    tetris_object.setYPositionBoxes(lower_y1 ,lower_y2 ,lower_y3 ,lower_y4 )
                    #create the object in the grid
                    gameGrid.setSquareColor( dir_x1, lower_y1, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x2, lower_y2, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x3, lower_y3, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x4, lower_y4, tetris_object.getColor())
                if ( tetris_object.getLabel() == 'z_shape' ):
                    #create a new object
                    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
                    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()

##                    #print the positions
##                    print(x1,x2,x3,x4)
##                    print(y1,y2,y3,y4)
##                    
                    dir_x1 = x1
                    dir_x2 = x2
                    dir_x3 = x3
                    dir_x4 = x4
                    
                    ##  x-direction stuff goes here  ##


                    for event in pygame.event.get():
                        if (event.type==pygame.KEYDOWN):
                            
                            if (event.key==pygame.K_LEFT):
                                #add 1 to the x positions of all boxes
                                dir_x1 = x1 -1
                                dir_x2 = x2 -1
                                dir_x3 = x3 -1
                                dir_x4 = x4 -1
                                #moveX = -5
                            if (event.key==pygame.K_RIGHT):
                                #subtract
                                dir_x1 = x1 +1
                                dir_x2 = x2 +1
                                dir_x3 = x3 +1
                                dir_x4 = x4 +1
                                #moveX = 5
                            if (event.key==pygame.K_UP):
                                #rotate counterclowise
                                moveY = -5
                            if (event.key==pygame.K_DOWN):
                                #rotateclockwise
                                moveY = 5
                    #erase the APPROPRIATE previous yPositions
                    previousY1 = y1
                    previousY2 = y2
                    previousY3 = y3
                    previousY4 = y4

                    #color these coordinates 'white'
                    gameGrid.setSquareColor( x1, previousY1, 'white')
                    gameGrid.setSquareColor( x2, previousY2, 'white')
                    gameGrid.setSquareColor( x3, previousY3, 'white')
                    gameGrid.setSquareColor( x4, previousY4, 'white')
                    
                    #make it go down by subtracting fromt he yPosBox<#>
                    lower_y1 = y1-1
                    lower_y2 = y2-1
                    lower_y3 = y3-1
                    lower_y4 = y4-1
                            
                    #set the newPositions ( Y )
                    tetris_object.setXPositionBoxes(dir_x1,dir_x2,dir_x3,dir_x4)
                    tetris_object.setYPositionBoxes(lower_y1 ,lower_y2 ,lower_y3 ,lower_y4 )
                    #create the object in the grid
                    gameGrid.setSquareColor( dir_x1, lower_y1, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x2, lower_y2, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x3, lower_y3, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x4, lower_y4, tetris_object.getColor())
                if ( tetris_object.getLabel() == 'T_shape' ):
                    #create a new object
                    x1,x2,x3,x4 = tetris_object.getXPostionBoxes()
                    y1,y2,y3,y4 = tetris_object.getYPostionBoxes()

##                    #print the positions
##                    print(x1,x2,x3,x4)
##                    print(y1,y2,y3,y4)
##                    
                    dir_x1 = x1
                    dir_x2 = x2
                    dir_x3 = x3
                    dir_x4 = x4
                    
                    ##  x-direction stuff goes here  ##


                    for event in pygame.event.get():
                        if (event.type==pygame.KEYDOWN):
                            
                            if (event.key==pygame.K_LEFT):
                                #add 1 to the x positions of all boxes
                                dir_x1 = x1 -1
                                dir_x2 = x2 -1
                                dir_x3 = x3 -1
                                dir_x4 = x4 -1
                                #moveX = -5
                            if (event.key==pygame.K_RIGHT):
                                #subtract
                                dir_x1 = x1 +1
                                dir_x2 = x2 +1
                                dir_x3 = x3 +1
                                dir_x4 = x4 +1
                                #moveX = 5
                            if (event.key==pygame.K_UP):
                                #rotate counterclowise
                                moveY = -5
                            if (event.key==pygame.K_DOWN):
                                #rotateclockwise
                                moveY = 5
                    #erase the APPROPRIATE previous yPositions
                    previousY1 = y1
                    previousY2 = y2
                    previousY3 = y3
                    previousY4 = y4

                    #color these coordinates 'white'
                    gameGrid.setSquareColor( x1, previousY1, 'white')
                    gameGrid.setSquareColor( x2, previousY2, 'white')
                    gameGrid.setSquareColor( x3, previousY3, 'white')
                    gameGrid.setSquareColor( x4, previousY4, 'white')
                    
                    #make it go down by subtracting fromt he yPosBox<#>
                    lower_y1 = y1-1
                    lower_y2 = y2-1
                    lower_y3 = y3-1
                    lower_y4 = y4-1
                            
                    #set the newPositions ( Y )
                    tetris_object.setXPositionBoxes(dir_x1,dir_x2,dir_x3,dir_x4)
                    tetris_object.setYPositionBoxes(lower_y1 ,lower_y2 ,lower_y3 ,lower_y4 )
                    #create the object in the grid
                    gameGrid.setSquareColor( dir_x1, lower_y1, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x2, lower_y2, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x3, lower_y3, tetris_object.getColor())
                    gameGrid.setSquareColor( dir_x4, lower_y4, tetris_object.getColor())
            break
