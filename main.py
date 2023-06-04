import time
import mapGeneration
import logging
from constants import *
import pygame
import numpy as np
from pygame.locals import *

seed = -1

seed_of_the_day = True


level = logging.WARN
logging.basicConfig(format='%(levelname)s - %(name)s - %(message)s', level=level)
map = mapGeneration.generate_map(seed, seed_of_the_day)
logger = logging.getLogger("MAIN")

print(map)




pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)



def draw_grid(screen, grid):
    pygame.draw.rect(screen, (0,0,0), [MARGIN, MARGIN, DIMENTIONS[1]*SQUAREWIDTH,DIMENTIONS[0]*SQUAREHEIGHT], width=5)
    for i, x in enumerate(grid):
        for i2, y in enumerate(x):
            if y == 1: 
                pygame.draw.rect(screen, (0,0,0), [[MARGIN+(i2*SQUAREWIDTH),MARGIN+(i*SQUAREHEIGHT)],
                                                   [SQUAREWIDTH,SQUAREHEIGHT]])


running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    draw_grid(screen, map)
    pygame.display.update()
    
    
    