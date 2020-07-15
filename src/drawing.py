import pygame

from src.locals import *
from src.tokens import tokens as tk

def loading_screen_update(dest, percentage):
    dest.fill(BLACK)
    string = "Loading... " + str(percentage) + "%"
    tk.draw_sentance(dest, string, (0, 0), PW=3)
    for e in pygame.event.get():
        if e.type == pygame.locals.QUIT: quit()
    pygame.display.update()

def draw_floor(dest, floor, scroll=False, PW=1):
    dest.fill(BLACK)
    for y, row in enumerate(floor):
        for x, stack in enumerate(row):
            col1, col2 = TILE_COLORS[stack[-1]] if stack[-1] in TILE_COLORS else (BLACK, WHITE)
            tk.draw_token(
                dest, stack[-1], (x*(PW*16), y*(PW*16)), col1=col1, col2=col2, PW=PW)
    pygame.display.update()
