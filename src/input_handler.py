import pygame
from pygame.locals import *
from src import player
from src.utils import get

def expect_key(expectlist=[]):
    while True:
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT: quit()
            if e.type == KEYDOWN:
                if expectlist:
                    if e.key in expectlist: return e.key
                else: return e.key

DIRECTION_MAP = {
    K_UP: 0,
    K_RIGHT: 1,
    K_DOWN: 2,
    K_LEFT: 3,
}

KEY_MAP = {
    "stairs": K_SPACE,
}

def players_turn(G):
    inp = expect_key()
    if inp in DIRECTION_MAP:
        player.move(G, DIRECTION_MAP[inp])
    if inp == KEY_MAP["stairs"]:
        stack = get(
            G["DUNGEON"][G["FLOOR"]],
            player.PLAYER["POS"])
        if "upstairs" in stack: G["FLOOR"] += 1
        elif "downstairs" in stack: G["FLOOR"] -= 1
