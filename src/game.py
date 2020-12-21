import pygame
from pygame.locals import *

from src.locals import *
from src.input_handler import players_turn, expect_key
from src.utils import update_lit
from src.tokens import tokens as tk
import src.drawing as dr
from src.level_builder import builder
from src import player
from src.enemies import enemy


W, H = (32 * 32, 32 * 20)

SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("The Temple of LURD")
surf = pygame.Surface((32, 32))
surf.fill((1, 255, 1))
tk.draw_token(surf, "face", (0, 0), col1=BLACK, col2=DARKGREEN, PW=2)
surf.set_colorkey((1, 255, 1))
pygame.display.set_icon(surf)

def game_wrapper():
    LIMIT = 15
    DEBUG = False
    selected = 0
    while True:
        dr.draw_setup_menu(
            SCREEN, W, H,
            LIMIT=LIMIT, DEBUG=DEBUG, selected=selected
        )
        inp = expect_key()
        if inp == K_DOWN:
            selected = (selected + 1) % 4
        if inp == K_UP:
            selected = (selected - 1) % 4

        if inp == K_LEFT:
            if selected == 0:
                LIMIT = max(0, LIMIT - 1)
            if selected == 1:
                DEBUG = not DEBUG

        if inp == K_RIGHT:
            if selected == 0:
                LIMIT = max(0, LIMIT + 1)
            if selected == 1:
                DEBUG = not DEBUG
        
        if inp == K_RETURN and selected == 2:
            G = setup_game(LIMIT, DEBUG)
            if run_game(G):
                dr.draw_victory_screen(SCREEN, W, H)
            else:
                dr.draw_death_screen(SCREEN, W, H)

            expect_key([K_RETURN])
        
        if inp == K_RETURN and selected == 3:
            return


def setup_game(limit, debug):
    G = {}
    D, I, A, T = builder.build(SCREEN, limit=limit, debug=debug)
    G["DUNGEON"] = D
    G["ITEMS"] = I
    G["ACTORS"] = A
    G["THEMES"] = T
    G["LIT"] = [set() for floor in G["DUNGEON"]]
    G["FLOOR"] = 0
    G["PW"] = 4

    G["LOG"] = []
    
    SCREEN.fill(BLACK)
    tk.draw_sentance(SCREEN, "Done.", (0, 0), PW=3)
    return G
    
def run_game(G):
    while player.PLAYER["HP"] > 0:
        update_lit(G["DUNGEON"][G["FLOOR"]],
                   [player.PLAYER["POS"]],
                   G["LIT"][G["FLOOR"]])
        dr.draw_floor(SCREEN, G, player.PLAYER)
        dr.draw_HUD(SCREEN, G, player.PLAYER)
        dr.draw_log(SCREEN, (0, H-(16*4)), G)
        pygame.display.update()
        players_turn(G, SCREEN)
        if G["FLOOR"] >= len(G["DUNGEON"]): return True
        enemy.update_enemies(G, player.PLAYER)
    return False
