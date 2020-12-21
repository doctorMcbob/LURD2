import pygame
from pygame import Surface

from src.locals import *
from src.tokens import tokens as tk
from src.utils import get, insight, color_darken
from src.themes import themes

def draw_setup_menu(dest, W, H, LIMIT=15, DEBUG=False, selected=0):
    MENU = Surface((W, H))
    MENU.fill(BLACK)
    tk.draw_sentance(
        MENU, "The Temple of LURD 2", (32, 32),
        PW=3,
    )
    tk.draw_sentance(
        MENU, "a RogueLike by Wesley :)", (96, 128),
        PW=2
    )
    tk.draw_sentance(
        MENU, "Floors :", (128, 256),
        PW=2
    )
    tk.draw_sentance(
        MENU, str(LIMIT), (576, 256),
        col2=[LIGHTGREEN, WHITE, WHITE, WHITE][selected], PW=2
    )
    tk.draw_sentance(
        MENU, "Debug mode :", (128, 320),
        PW=2
    )
    tk.draw_sentance(
        MENU, str(DEBUG), (576, 320),
        col2= [WHITE, LIGHTGREEN , WHITE, WHITE][selected], PW=2
    )
    tk.draw_sentance(
        MENU, "Begin", (576, 384),
        col2= [WHITE, WHITE, LIGHTGREEN, WHITE][selected], PW=2
    )
    tk.draw_sentance(
        MENU, "Exit", (576, 448),
        col2= [WHITE, WHITE, WHITE, LIGHTGREEN][selected], PW=2
    )
    dest.blit(MENU, (0, 0))


def draw_victory_screen(dest, W, H):
    VICTORY = Surface((W, H))
    tk.draw_sentance(
        VICTORY, "You did it", (64, 64), PW=3
    )
    tk.draw_sentance(
        VICTORY, "You escaped the Temple of LURD", (96, 128), PW=1
    )
    tk.draw_token(
        VICTORY, "face", (96, 192), col2=GREEN, PW=5
    )
    dest.blit(VICTORY, (0, 0))


def draw_death_screen(dest, W, H):
    DEATH = Surface((W, H))
    tk.draw_sentance(
        DEATH, "You died", (64, 64), PW=3
    )
    tk.draw_sentance(
        DEATH, "The Temple of LURD claims another life", (96, 128), PW=1
    )
    dest.blit(DEATH, (0, 0))

    
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


def draw_HUD(dest, G, player):
    PLAYER_INFO = Surface((1024, 64))
    PLAYER_INFO.fill((1, 255, 1))
    # Health Bar
    HP = player["HP"]
    MAX = player["HPMAX"]
    teenth = MAX / 16
    string = str(HP) + "/" + str(MAX)
    for n in range(16):
        col = RED if n * teenth <= HP else LIGHTGRAY
        if n < len(string):
            if string[n] in tk.CHARACTER_MAP:
                token = tk.CHARACTER_MAP[string[n]]
            else:
                token = string[n] 
            tk.draw_token(
                PLAYER_INFO, token,
                (n * 32, 0),
                col1=col, col2=BLACK, PW=2)
        else:
            tk.draw_token(
                PLAYER_INFO, "base",
                (n * 32, 0),
                col1=col, col2=BLACK, PW=2)
    string = "LEVEL: " + str(player["LVL"])
    tk.draw_sentance(PLAYER_INFO, string, (0, 32),
                     col1=(1, 255, 1), col2=WHITE, PW=1)
    string = "EXP: " + str(player["EXP"])
    tk.draw_sentance(PLAYER_INFO, string, (0, 48),
                     col1=(1, 255, 1), col2=WHITE, PW=1)
    string = "ATTACK: " + str(player["ATK"])
    tk.draw_sentance(PLAYER_INFO, string, (192, 32),
                     col1=(1, 255, 1), col2=WHITE, PW=1)
    string = "DEFENCE: " + str(player["DEF"])
    tk.draw_sentance(PLAYER_INFO, string, (192, 48),
                     col1=(1, 255, 1), col2=WHITE, PW=1)
    if player["WEAPON"]:
        string = "WEAPON: " + player["WEAPON"]["NAME"]
    else:
        string = "WEAPON: None"
    tk.draw_sentance(PLAYER_INFO, string, (512, 0),
                     col1=(1, 255, 1), col2=WHITE, PW=1)
    if player["ARMOR"]:
        string = "ARMOR: " + player["ARMOR"]["NAME"]
    else:
        string = "ARMOR: None"
    tk.draw_sentance(PLAYER_INFO, string, (512, 16),
                     col1=(1, 255, 1), col2=WHITE, PW=1)
    string = "FLOOR: " + str(G["FLOOR"])
    tk.draw_sentance(PLAYER_INFO, string, (512, 32),
                     col1=(1, 255, 1), col2=WHITE, PW=1)
    string = G["THEMES"][G["FLOOR"]]
    tk.draw_sentance(PLAYER_INFO, string, (512, 48),
                     col1=(1, 255, 1), col2=WHITE, PW=1)

    PLAYER_INFO.set_colorkey((1, 255, 1))
    dest.blit(PLAYER_INFO, (0, 0))

def draw_log(dest, pos, G, num_entries=4):
    LOG = Surface((512, num_entries * 16))
    LOG.fill((1, 255, 1))
    for i, entry in enumerate(G["LOG"][0 - num_entries:]):
        tk.draw_sentance(
            LOG, entry, (0, i*16),
            col1=(1, 255, 1), col2=WHITE, PW=1
        )
    LOG.set_colorkey((1, 255, 1))
    dest.blit(LOG, pos)

def draw_INV(dest, pos, player, search=None):
    INV = Surface((512, len(player["INV"]) * 16))
    INV.fill(GRAY)
    idx = "0123456789abcdefghijklmnopqrstuvwxyz"
    for i, item in enumerate(player["INV"]):
        if search in item["TRAITS"]:
            col2 = LIGHTGREEN
        else: col2 = WHITE
        
        tk.draw_sentance(
            INV, idx[i] + ": " + item["NAME"], (0, i*16),
            col1=GRAY, col2=col2, PW=1
        )
    dest.blit(INV, pos)
