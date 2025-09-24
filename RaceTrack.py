"""
Create and configures the race track and provides race track
functionality
"""
import turtle

#define the module variables
raceTrack = None

#create the race track/window where the race takes place
def createRaceTrack():
    global raceTrack
    raceTrack = turtle.Screen()
    raceTrack.bgcolor("lightgreen")
    return raceTrack


def closeRaceTrack():
    #wait for the user to click before exiting
   raceTrack.exitonclick()