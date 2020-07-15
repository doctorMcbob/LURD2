from random import randint, choice

import pygame
from src.tokens import tokens as tk

from src.utils import distance, solvable
from src.drawing import loading_screen_update, draw_floor
from src.level_builder.rooms import apply_rooms

def fresh_floor(W, H, ent=False, ext=False):
    floor = []
    for y in range(H):
        floor.append([])
        for x in range(W):
            floor[-1].append([])
            if (x, y) == ent: floor[-1][-1].append("downstairs")
            elif (x, y) == ext: floor[-1][-1].append("upstairs")
            else: floor[-1][-1].append("floor")
    return floor


def pathfinder(grid, ent, ext, debug_surf=False):
    """
    fill the grid with stone until it isn't solvable anymore
    then undo the last stones placed
    repeat until the whole grid is accounted for

    optomized by applying more stone while the number of slots is larger
    """
    slots = [(x, y) for x in range(len(grid[0])) for y in range(len(grid))]
    slots.remove(ent); slots.remove(ext)
    while slots:
        new = []
        for _ in range((len(slots) // 50) + 1):
            x, y = choice(slots)
            grid[y][x].append("stone")
            slots.remove((x, y))
            new.append((x, y))
        check, touched = solvable(grid, ent, ext)
        if not check:
            for (x, y) in new:
                grid[y][x].pop()
        else:
            for x, y in slots:
                if (x, y) not in touched:
                    grid[y][x].append("stone")
                    slots.remove((x, y))
        if debug_surf:
            draw_floor(debug_surf, grid)
            tk.draw_sentance(debug_surf, "len slots: " + str(len(slots)), (0, 32*15))
            pygame.display.update()


def carve(grid):
    pass


def build(screen, limit=15):
    """
    > actually writing docstrings

    so im thinking each floor will be a 2d array
    each cell in the 2d array will be a stack of strings
    the strings must have a token representation
    """
    loading_screen_update(screen, 0)
    floors = []
    items = []
    actors = []
    ext = (5, 5)
    for i in range(limit):
        loading_screen_update(screen, int((i / limit) * 100))

        W, H = (i*2)+randint(10, 20) , (i*2)+randint(10, 20)
        W, H = max(W, ext[0] + 2), max(H, ext[1] + 2)
        ent = ext
        while distance(ent, ext) < max(W , H) // 2:
            ext = randint(2, W - 2), randint(2, H - 2)
        
        items.append([])
        actors.append([])

        floor = fresh_floor(W, H, ent=ent, ext=ext)
        apply_rooms(floor)
        pathfinder(floor, ent, ext)
        carve(floor)
        
        floors.append(floor)
    return floors
