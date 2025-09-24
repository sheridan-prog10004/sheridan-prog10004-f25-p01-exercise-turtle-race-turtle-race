"""
Coordinates the program and interacts with the user. Runs the main program statements
"""
import RaceTrack
import Race

raceTrack = RaceTrack.createRaceTrack()

Race.registerRacers()
Race.positionRacers()
Race.runRace()
Race.determineWinner()

RaceTrack.closeRaceTrack()