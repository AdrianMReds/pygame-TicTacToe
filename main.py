import pygame as pg
import time
import sys

#Character to store x or o
xo = 'x'

#To check if someone won
winner = None

#If the game is a draw
draw = None

#Game window measurements
width = 400
height = 400

white = (255, 255, 255)

line_color = (0, 0, 0)

board = [ [None]*3, [None]*3, [None]*3]