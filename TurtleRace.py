"""
Version 1: In this version, the turtle race has a falt single-file structure
"""

#access the libraries/modules required for the program
import turtle

#create the race track/window where the race takes place
raceTrack = turtle.Screen()
raceTrack.bgcolor("lightgreen")

#create the racers: larry, curly and moe
larry = turtle.Turtle()
larry.shape("turtle")
larry.shapesize(3,3,1)
larry.color("darkgreen")
larry.penup()

curly = turtle.Turtle()
curly.shape("turtle")
curly.shapesize(3, 3, 1)
curly.color("darkred")
curly.penup()

moe = turtle.Turtle()
moe.shape("turtle")
moe.shapesize(3, 3, 1)
moe.color("blue")
moe.penup()

#position the racers on the starting line
larry.left(180)
larry.forward(200)
larry.right(90)

curly.left(90)

moe.forward(200)
moe.left(90)

#run the race

#determine the winner

#announce the winner

#wait for the user to click before exiting
raceTrack.exitonclick()