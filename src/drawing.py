import pygame

from src.locals import *
from src.tokens import tokens as tk
from src.utils import get, insight, color_darken
from src.themes import themes

def loading_screen_update(dest, percentage):
    dest.fill(BLACK)
    string = "Loading... " + str(percentage) + "%"
    tk.draw_sentance(dest, string, (0, 0), PW=3)
    for e in pygame.event.get():
        if e.type == pygame.locals.QUIT: quit()
    pygame.display.update()


def debug_floor(dest, floor):
    dest.fill(BLACK)
    for y, line in enumerate(floor):
        for x, stack in enumerate(line):
            if not stack: continue
            col1, col2 = TILE_COLORS[stack[-1]]
            tk.draw_token(
                    dest, stack[-1], (x*16, y*16),
                    col1=col1, col2=col2, PW=1
                )
    pygame.display.update()


def draw_floor(dest, G, player):
    floor = G["DUNGEON"][G["FLOOR"]]
    theme = G["THEMES"][G["FLOOR"]]
    items = G["ITEMS"][G["FLOOR"]]
    actors = G["ACTORS"][G["FLOOR"]]
    lit = G["LIT"][G["FLOOR"]]
    PW = G["PW"]
    
    dest.fill(BLACK)
    W, H = dest.get_size()
    cx, cy = player["POS"]
    offset = (PW*8)
    
    for y, line in enumerate(floor):
        for x, stack in enumerate(line):
            if not stack: continue
            if lit != False and (x, y) not in lit: continue
            for token in stack:
                if token in themes.THEME_MAP[theme]["COLORS"]:
                    col1, col2 = themes.THEME_MAP[theme]["COLORS"][token]
                else:
                    col1, col2 = TILE_COLORS[token]
                if not insight(floor, player["POS"], (x, y)):
                    col1 = color_darken(col1, 75)
                    col2 = color_darken(col2, 75)
                X, Y = ((x-cx)*(PW*16), (y-cy)*(PW*16))
                if (0 <= (W // 2 + X) <= W) and (0 <= (H // 2 + Y) <= H): 
                    tk.draw_token(
                        dest, token, (W // 2 + X - offset, H // 2 + Y - offset),
                        col1=col1, col2=col2, PW=PW
                    )


    for thing in items + actors:
        if not insight(floor, player["POS"], thing["POS"]):
            continue
        X, Y = ((thing["POS"][0]-cx)*(PW*16), (thing["POS"][1]-cy)*(PW*16))
        col1, col2 = thing["colors"]
        tk.draw_token(
            dest, thing["token"],
            (W // 2 + X - offset, H // 2 + Y - offset),
            col1=col1, col2=col2,
            PW=PW
        )
    tk.draw_token(
        dest, player["token"],
        (W // 2 - offset, H // 2 - offset),
        col1=player["colors"][0], col2=player["colors"][1],
        PW=PW
    )
                
    pygame.display.update()
            
