import pygame
from pygame.locals import *
from src import drawing as dr
from src import player
from src import items
from src.utils import get, log

def expect_key(expectlist=[]):
    while True:
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT: quit()
            if e.type == KEYDOWN:
                if expectlist:
                    if e.key in expectlist: return e.key
                else: return e.key

KEYBOARD_MAP = {
    K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e",
    K_f: "f", K_g: "g", K_h: "h", K_i: "i", K_j: "j",
    K_k: "k", K_l: "l", K_m: "m", K_n: "n", K_o: "o",
    K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t",
    K_u: "u", K_v: "v", K_w: "w", K_x: "x", K_y: "y",
    K_z: "z", 
    K_0: "0", K_1: "1", K_2: "2", K_3: "3", K_4: "4",
    K_5: "5", K_6: "6", K_7: "7", K_8: "8", K_9: "9",
}
                
DIRECTION_MAP = {
    K_UP: 0,
    K_RIGHT: 1,
    K_DOWN: 2,
    K_LEFT: 3,
}

KEY_MAP = {
    "stairs": K_SPACE,
    "INV": K_i,
    "equipt": K_e,
}

def players_turn(G, SCREEN):
    inp = expect_key()
    if inp in DIRECTION_MAP:
        player.move(G, DIRECTION_MAP[inp])

    if inp == KEY_MAP["stairs"]:
        stack = get(
            G["DUNGEON"][G["FLOOR"]],
            player.PLAYER["POS"])
        if "upstairs" in stack: G["FLOOR"] += 1
        elif "downstairs" in stack: G["FLOOR"] -= 1

    if inp == KEY_MAP["equipt"]: # TODO: make this better, choose from menu and everything
        idx = "0123456789abcdefghijklmnopqrstuvwxyz"
        dr.draw_INV(SCREEN, (0, 0), player.PLAYER, search="EQUIPTABLE")
        key = expect_key(KEYBOARD_MAP.keys())
        i = idx.index(KEYBOARD_MAP[key])
        if i < len(player.PLAYER["INV"]):
            item = player.PLAYER["INV"][i]
            items.equipt(player.PLAYER, item, G)
        else:
            log(G, "That didn't work.")
        
    if inp == KEY_MAP["INV"]:
        dr.draw_INV(SCREEN, (0, 0), player.PLAYER)
        players_turn(G, SCREEN)
