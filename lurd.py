#lurd.py
"""
Here we go

Roguelike, use token system for graphics
"""

import pygame
from pygame.locals import *

from src.locals import *
from src.tokens import tokens as tk
import src.drawing as dr
from src.level_builder import builder

PW = 32
W, H = (PW * 32, PW * 20)

def expect_key(expectlist=[]):
    while True:
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT: quit()
            if e.type == KEYDOWN:
                if expectlist:
                    if e.key in expectlist: return e.key
                else: return e.key


SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("love hate and programming")

DUNGEON = builder.build(SCREEN)
SCREEN.fill(BLACK)
tk.draw_sentance(SCREEN, "Done.", (0, 0), PW=3)

FLOOR = 0
PW = 2
while __name__ == """__main__""":
    dr.draw_floor(SCREEN, DUNGEON[FLOOR], PW=PW)
    inp = expect_key()
    if inp == K_LEFT: FLOOR -= 1
    elif inp == K_RIGHT: FLOOR += 1
    if inp == K_UP: PW -= 1
    if inp == K_DOWN: PW += 1
