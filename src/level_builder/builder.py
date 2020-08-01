from random import randint, choice

import pygame

from src.tokens import tokens as tk
from src.utils import *
from src.drawing import loading_screen_update, debug_floor
from src.level_builder.rooms import apply_rooms
from src.enemies import enemy
from src.themes import themes

STARTINGFLOOR = []
for y in range(10):
    STARTINGFLOOR.append([])
    for x in range(10):
        if (x, y) == (6, 6):
            STARTINGFLOOR[-1].append(["upstairs"])
        elif x in [0, 9] or y in [0, 9]:
            STARTINGFLOOR[-1].append(["stone"])
        else:
            STARTINGFLOOR[-1].append(["floor"])

def fresh_floor(W, H, ent=False, ext=False):
    floor = []
    for y in range(H):
        floor.append([])
        for x in range(W):
            floor[-1].append([])
            if (x, y) == ent: floor[-1][-1].append("downstairs")
            elif (x, y) == ext: floor[-1][-1].append("upstairs")
    return floor


def pathfinder(grid, ent, ext, debug_surf=False):
    """
    fill the grid with stone until it isn't solvable anymore
    then undo the last stones placed
    repeat until the whole grid is accounted for

    optomized by applying more stone while the number of slots is larger
    """
    slots = list(filter(
        lambda pos: not grid[pos[1]][pos[0]],
        [(x, y)
         for x in range(len(grid[0]))
         for y in range(len(grid))]
    ))
    while slots:
        new = []
        for _ in range((len(slots) // 10) + 1):
            x, y = choice(slots)
            grid[y][x].append("stone")
            slots.remove((x, y))
            new.append((x, y))
        check, touched = solvable(grid, ent, ext)
        if not check:
            for (x, y) in new:
                grid[y][x].pop()
                grid[y][x].append("floor")
        else:
            for x, y in slots:
                if (x, y) not in touched:
                    grid[y][x].append("stone")
                    slots.remove((x, y))
        if debug_surf:
            debug_floor(debug_surf, grid)
            tk.draw_sentance(debug_surf, "len slots: " + str(len(slots)), (0, 32*15))
            pygame.display.update()


def carve(grid, limit=2, debug_surf=False):
    sub = []
    for _ in range(limit):
        sub.append([])
        for _ in range(limit):
            sub[-1].append(["stone"])
    blocks = findsub(grid, sub)
    while blocks:
        block = getsub(grid, choice(blocks), (limit, limit))
        for _ in range( randint(((limit**2)//3)*2 - 1, ((limit**2)//3)*2 + 1) ):
            slot = get(block, choice(list(allof(block, "stone"))))
            slot.pop()
            slot.append("floor")
        blocks = findsub(grid, sub)
        if debug_surf:
            debug_floor(debug_surf, grid)


def populate(grid, items, actors, theme="DEFAULT"):
    # dummy
    common = themes.THEME_MAP[theme]["ENEMIES"]["COMMON"]
    rare = themes.THEME_MAP[theme]["ENEMIES"]["RARE"]
    boss = themes.THEME_MAP[theme]["ENEMIES"]["BOSS"]
    slots = list(allof(grid, "enemyspawn"))
    if slots:
        slot = choice(slots)
        slots.remove(slot)
        get(grid, slot).remove("enemyspawn")
        actors.append(enemy.make_enemy(choice(boss), slot))
    while slots:
        slot = choice(slots)
        slots.remove(slot)
        get(grid, slot).remove("enemyspawn")
        roll = randint(0, 100)
        if roll > 30: enemyname = choice(common)
        else: enemyname = choice(rare)
        actors.append(enemy.make_enemy(enemyname, slot))

def build(screen, startingfloor=STARTINGFLOOR, limit=15, debug=False):
    """
    > actually writing docstrings

    so im thinking each floor will be a 2d array
    each cell in the 2d array will be a stack of strings
    the strings must have a token representation
    """
    if debug: debug = screen
    loading_screen_update(screen, 0)
    floors = [STARTINGFLOOR]
    items = [[]]
    actors = [[]]
    levelthemes = ["DEFAULT"]
    ext = (5, 5)
    themelist = list(themes.THEME_MAP.keys())
    themelist.remove("DEFAULT")
    for i in range(limit+1):
        loading_screen_update(screen, int((i / (limit+1)) * 100))

        W, H = (i*3)+randint(25, 30) , (i*3)+randint(25, 30)
        W, H = max(W, ext[0] + 2), max(H, ext[1] + 2)
        ent = ext
        while distance(ent, ext) < (max(W , H) // 3) * 2:
            ext = randint(2, W - 2), randint(2, H - 2)
        
        items.append([])
        actors.append([])

        theme = choice(themelist)

        levelthemes.append(theme)
        
        floor = fresh_floor(W, H, ent=ent, ext=ext)
        tk.draw_sentance(screen, "Making rooms...", (0, 48), PW=1)
        pygame.display.update()
        apply_rooms(floor, THEME=theme, debug_surf=debug)
        tk.draw_sentance(screen, "Pathfinding...", (0, 48+16), PW=1)
        pygame.display.update()
        pathfinder(floor, ent, ext, debug_surf=debug)
        tk.draw_sentance(screen, "Carving...", (0, 48+32), PW=1)
        pygame.display.update()
        carve(floor, debug_surf=debug)

        frame = []
        for y in range(H + 2):
            frame.append([])
            for x in range(W + 2):
                if x in [0, W + 1] or y in [0, H + 1]:
                    frame[-1].append(["stone"])
                else:
                    frame[-1].append([])

        insert_grid(frame, floor, (1, 1))
        tk.draw_sentance(screen, "Populating...", (0, 48+48), PW=1)
        pygame.display.update()
        populate(frame, items[-1], actors[-1], theme=theme)
        floors.append(frame)
    return floors, items, actors, levelthemes
