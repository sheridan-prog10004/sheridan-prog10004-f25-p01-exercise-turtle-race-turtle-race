"""
Manages the race logic and the racers by creating them and having them
compete with each other. Module functions determine and announce the winner
"""
import turtle
import random

#define the module variables
leo = None
mikey = None
don = None

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
    dist = random.randint(10, 100)
    leo.forward(dist)

    dist = random.randint(10, 100)
    mikey.forward(dist)

    dist = random.randint(10, 100)
    don.forward(dist)

#determine the winner
def determineWinner():
    #TODO: Implement determining winner

    #announce the winner
    pass
