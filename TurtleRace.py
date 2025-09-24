"""
Version 1: In this version, the turtle race has a falt single-file structure
"""

#access the libraries/modules required for the program
import turtle
import random

#create the race track/window where the race takes place
def createRaceTrack():
    raceTrack = turtle.Screen()
    raceTrack.bgcolor("lightgreen")
    return raceTrack

#create the racer variables/objects
def registerRacers():
    leo = turtle.Turtle()
    leo.shape("turtle")
    leo.shapesize(3,3,1)
    leo.color("darkgreen")
    leo.penup()

    mikey = turtle.Turtle()
    mikey.shape("turtle")
    mikey.shapesize(3, 3, 1)
    mikey.color("darkred")
    mikey.penup()

    don = turtle.Turtle()
    don.shape("turtle")
    don.shapesize(3, 3, 1)
    don.color("blue")
    don.penup()
    return leo,mikey,don

#position the racers on the starting line
def positionRacers(leo, mikey, don):
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
def runRace(leo, mikey, don):
    dist = random.randint(10, 100)
    leo.forward(dist)

    dist = random.randint(10, 100)
    mikey.forward(dist)

    dist = random.randint(10, 100)
    don.forward(dist)

#determine the winner
def determineWinner(leo, mikey, done):
    #TODO: Implement determining winner

    #announce the winner
    pass

#run the main program statements
raceTrack = createRaceTrack()
racer1, racer2, racer3 = registerRacers()
positionRacers(racer1, racer2, racer3)
runRace(racer1, racer2, racer3)
determineWinner(racer1, racer2, racer3)

#wait for the user to click before exiting
raceTrack.exitonclick()