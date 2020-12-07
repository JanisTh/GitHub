################################
#                              #
# SNAKE.PY                     #
#                              #
# Author:  Janis thüer         #
# Date:    18. November 2020   #
#                              #
################################
  

###########
# IMPORTS #
###########


from gturtle import *


#####################
# GLOBAL PROPERTIES #
#####################

# Key codes


# Co
# Turtle properties

frame = TurtleFrame()
frameTurtle = makeTurtle()
frameTurtle.hideTurtle()
frameTurtle.setPenColor("blue")
snakeTurtle = Turtle (frameTurtle,"snake.png") # defines the main Turtle, that she has to be stay in the frame and her look.
snakeTurtle.penUp()
appleTurtle = Turtle (frameTurtle,"apple.png")

#instant settings

frameSize = 500 # defines the size of the frame.

# General properties

points = 0
highScore = 0
lastKey = None
dangerZone = 10 
a = 100
i = 0

name = input("Geben Sie Ihren Namen ein") #  wants to find out the name of the player.

#############
# FUNCTIONS #
#############


def square(): # draws the main frame.
    frameTurtle.setPos(-250, -250) 
    repeat 4: # repeats the function which should draw the frame.
        frameTurtle.fd (frameSize)
        frameTurtle.rt(90)


# FUNCTIONS ON SPECIFIC TURTLES


# Checks whether the snake (turtle) is alive or not.


def snakeTurtleIsAlive(): 
   
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY() # find out the coordinates of the snake.
    if posX > 245 or posX < -245 or posY > 245 or posY < -245: # find out if the turtle should be dead.
        playTone(250, 1000)
        print "Game Over"
        return False # stop game if  the snake is dead.
    

    
    return True

def apple():  # defines the apple which is getting to  be captured by the snake.
    
    global appleTurtle
    if appleTurtle == None:
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize) 
    else:
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)


       
def statusbar(): # defines a "statusbar" where general informations are telled while the game is running.
       
        addStatusBar(25)
        setStatusText("Player name: "+name +" | Game: "+ str(points)+" points ")


def eatApple(): # says that if the Turtle is in the given range of the apple she should catch them.
    
    posAX = appleTurtle.getX()
    posAY = appleTurtle.getY()
    dist = snakeTurtle.distance(posAX, posAY) 
    
    if dist < dangerZone:     # DangerZone means the given area where the apple is eaten
        global points
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize) # brings the new apples to their random positions.
        points = points +1
        playTone(00)
        snakeTurtle.setStatusText("Player name: "+name +" | Game: "+ str(points)+" points ")


# GENERAL METHODS



# Waits until a name is entered by a dialog.
# It saves the name to the global variable name.

def waitForInputName():
    global name 
    




# MAIN METHODS


# The function to play the game.
# Reset some stuff first, like the snake turtle, points, etc.

def play():
    global points # we want to change the value
    global i
    global name
    snakeTurtle.addStatusBar(25)
    snakeTurtle.setStatusText("Player name: "+ name +" | Game: "+ str(points)+" points ")
    print "Play function started" 


    i = 0
    isAlive = True
    while (isAlive): # Run the game while the snake is alive
        
        # Turn, move the snake here
        # the turtle is controlled with this code
        
        facing = snakeTurtle.heading()
        keyPressed = getKeyCode()
        if keyPressed == 37:
            if facing == 0 or  facing == 180: # LEFT
                snakeTurtle.setHeading(270)
        if keyPressed == 39:
            if facing == 0 or  facing == 180: # RIGHT
                snakeTurtle.setHeading(90)
        if keyPressed == 38:
            if facing == 90 or facing == 270: # UP
                snakeTurtle.setHeading(0)
        if keyPressed == 40:
            if facing == 270 or facing == 90: # DOWN
                snakeTurtle.setHeading(180)
       
        eatApple()
        snakeTurtle.fd(8)
        snakeTurtle.speed(80)
        snakeTurtleIsAlive()
        # Check if the snake is still alive
        isAlive = snakeTurtleIsAlive()

        i = i + 1

    # The game is over now

# MAIN METHODS

# The main function.
# Set up stuff here that stays alive for the whole application.


def main():
    statusbar()
    print "Main function started" 
    square()

    # Wait until a name is input
    waitForInputName()

    
    # createFrameTurtle() <- You could write a function with this name

    # Start the actual game
    play()


#############
# MAIN CODE #
#############


# Only call the main function here.
# Put all general functionality into the main function.
main()

# No code here! Everything goes in main, play or other functions!
