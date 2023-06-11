import time
import mapGeneration
import logging
from constants import *
import pygame
import numpy as np
from pygame.locals import *
from node import *

seed = -1

seed_of_the_day = False


level = logging.WARNING
logging.basicConfig(format='%(levelname)s - %(name)s - %(message)s', level=level)
map, nodes = mapGeneration.generate_map(seed, seed_of_the_day)
logger = logging.getLogger("MAIN")

print(map)




pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)



def draw_grid(screen, grid):
    pygame.draw.rect(screen, (255,255,255), [MARGIN, MARGIN, DIMENTIONS[1]*SQUAREWIDTH,DIMENTIONS[0]*SQUAREHEIGHT])
    for i, x in enumerate(grid):
        for i2, y in enumerate(x):
            if y == WALL: 
                pygame.draw.rect(screen, (0,0,0), [[MARGIN+(i2*SQUAREWIDTH),MARGIN+(i*SQUAREHEIGHT)],
                                                   [SQUAREWIDTH,SQUAREHEIGHT]])
            if y == NODE:
                pygame.draw.circle(screen, (255,0,0), [MARGIN+(i2*SQUAREWIDTH)+SQUAREWIDTH/2,MARGIN+(i*SQUAREHEIGHT)+SQUAREHEIGHT/2], SQUAREWIDTH/3)

def draw_nodes(screen, nodes:list[Node]):
    for i, n in enumerate(nodes):
        x, y = n.pos
        pygame.draw.circle(screen, (255,0,0), [MARGIN+(y*SQUAREWIDTH)+SQUAREWIDTH/2,MARGIN+(x*SQUAREHEIGHT)+SQUAREHEIGHT/2], SQUAREWIDTH/3)

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_q:
                logger.log(logging.DEBUG, "QUIT")
                running = False
    draw_grid(screen, map)
    draw_nodes(screen, nodes)
    pygame.display.update()
    
    
    