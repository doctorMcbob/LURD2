#lurd.py
"""
Here we go

Roguelike, use token system for graphics
"""

import pygame
from pygame.locals import *

from src.locals import *
from src.utils import expect_key, get, update_lit
from src.tokens import tokens as tk
import src.drawing as dr
from src.level_builder import builder
from src import player

import sys

debug = "-d" in sys.argv
W, H = (32 * 32, 32 * 20)

SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("love hate and programming")

DUNGEON = builder.build(SCREEN, limit=3, debug=debug)
LIT = [set() for floor in DUNGEON]
SCREEN.fill(BLACK)
tk.draw_sentance(SCREEN, "Done.", (0, 0), PW=3)

FLOOR = 0
PW = 4
while FLOOR <= 15:
    """
    Exploration demo
    """
    update_lit(DUNGEON[FLOOR], [player.PLAYER["POS"]], LIT[FLOOR])
    dr.draw_floor(SCREEN, DUNGEON[FLOOR], player.PLAYER,
                  lit=LIT[FLOOR], PW=PW)
    inp = expect_key()
    if inp == K_UP:  player.move(DUNGEON[FLOOR], 0)
    if inp == K_RIGHT: player.move(DUNGEON[FLOOR], 1)
    if inp == K_DOWN: player.move(DUNGEON[FLOOR], 2)
    if inp == K_LEFT: player.move(DUNGEON[FLOOR], 3)
    if inp == K_SPACE:
        stack = get(DUNGEON[FLOOR], player.PLAYER["POS"])
        if "upstairs" in stack:
            FLOOR += 1
        elif "downstairs" in stack:
            FLOOR -= 1
