"""
Manages the race logic and the racers by creating them and having them
compete with each other. Module functions determine and announce the winner
"""
import turtle
import random
from tkinter import messagebox
import RaceTrack

#define the module variables
leo = None
mikey = None
don = None
TURTLE_HEIGHT = 50

def createRacer(color):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.shapesize(3,3,1)
    racer.color(color)
    racer.penup()
    return racer

#create the racer variables/objects
def registerRacers():
    global leo, mikey, don
    leo = createRacer("darkgreen")
    mikey = createRacer("darkred")
    don = createRacer("blue")

#position the racers on the starting line
def positionRacers():
    leo.left(180)
    leo.forward(200)
    leo.right(90)

    mikey.left(90)

    don.forward(200)
    don.left(90)

    #prepare the racers for the race
    leo.pendown()
    mikey.pendown()
    don.pendown()

#run the race
def runRace():

    #repeat taking random steps for as long as the turtles have not crossed the finish line
    finishLine = RaceTrack.raceTrack.window_height() / 2 - TURTLE_HEIGHT
    finishLineReached = False
    while not finishLineReached:
        #advanced the turtles
        dist = random.randint(10, 100)
        leo.forward(dist)

        dist = random.randint(10, 100)
        mikey.forward(dist)

        dist = random.randint(10, 100)
        don.forward(dist)

        #check whether the finish line was reached by any of the racers
        if leo.ycor() > finishLine or mikey.ycor() > finishLine or don.ycor() > finishLine:
            #one of the racers have finsihed the race
            finishLineReached = True

        #TODO: ensure the turtles do pass the finish line and the race stops as soon as the top of the turtle
        #reaches the finish line exactly


#determine the winner
def determineWinner():
    """ Checks which of the three turtles has advanced furthest into the race and returns
        the winning turtle. The functions returns None if there was a tie. Afer calculating
        the winner, the function prints the race result.
    """
    #check whichever racer went the furthest
    winner = None
    raceResult = ""
    if leo.ycor() > mikey.ycor() and leo.ycor() > don.ycor():
        #leo won the race
        winner = leo
        raceResult = "Leo has won the race"
    elif mikey.ycor() > don.ycor() and mikey.ycor() > leo.ycor():
        #mikey won the race
        winner = mikey
        raceResult = "Mikey has won the race"
    elif don.ycor() > mikey.ycor() and don.ycor() > leo.ycor():
        #don won the race
        winner = don
        raceResult = "Don has won the race"
    else:
        winner = None
        raceResult = "Race is tied! Try again."

    #announce the winner
    messagebox.showinfo("Turtle Race", raceResult)
    return winner
