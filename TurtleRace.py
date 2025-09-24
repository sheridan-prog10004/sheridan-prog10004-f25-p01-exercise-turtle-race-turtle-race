"""
Version 1: In this version, the turtle race has a falt single-file structure
"""

#access the libraries/modules required for the program
import turtle
import random

#create the race track/window where the race takes place
raceTrack = turtle.Screen()
raceTrack.bgcolor("lightgreen")

#create the racer variables/objects
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

#position the racers on the starting line
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
dist = random.randint(10, 100)
leo.forward(dist)

dist = random.randint(10, 100)
mikey.forward(dist)

dist = random.randint(10, 100)
don.forward(dist)

#determine the winner

#announce the winner

#wait for the user to click before exiting
raceTrack.exitonclick()