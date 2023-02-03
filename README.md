# Alien Invasion Game Project
This small project implements an simple alien invasion game. 

## Description
The Alien Invasion game is a 2D game in which you play as a spaceship tasked with shooting down a fleet of invading aliens over a number of increasingly difficult levels. 

The player has the ability to move left, right and fire bullets to destroy the invading ships. You begin the game with 4 lives, and progress through levels each time you destroy the full alien fleet. 

Each level, the speed of the player, aliens and bullets increase, but so does the point value for destroying an alien ship. 

The game ends when the player runs out of lives, either by colliding with an alien, or letting the fleet reach the bottom of the play area.

## Requirements to run
- Python 3.11
- pygame 2.1.3.dev8
  - Can be installed using `pip install pygame --pre`

This was tested using the versions above, but it may run on previous python and pygame versions.

The game can then be run using `python alien_invasion.py` 
