import pygame
from pygame import Surface, Rect
from pygame.locals import *

from src.tokens import tokens as tk
from src.locals import *

from pathlib import Path
import os
import sys

pygame.init()

PW = 32
X, Y = 0, 0

SCREEN = pygame.display.set_mode((PW*16, PW*20))
pygame.display.set_caption("Room Builder")
HEL16 = pygame.font.SysFont("Helvetica", 16)

path = Path(os.path.dirname(os.path.abspath(__file__))) / "src/level_builder/bin"
name = sys.argv[-1]

room = None
def load(name):
    global room, W, H
    try:
        with open(path/name, "r") as f:
            room = eval(f.read())
        W, H = len(room[0]), len(room)
    except IOError:
        pass

def save(name):
    if not name: return
    with open(path/name, "w") as f:
        f.write(repr(room))

if name in os.listdir(path):
    load(name)

if room:
    W, H = len(room[0]), len(room)
else:
    W, H = 6, 6
    room = []
    for y in range(H):
        room.append([])
        for x in range(W):
            room[-1].append(["empty"])

ALPHABET_KEY_MAP = {
    K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e",
    K_f: "f", K_g: "g", K_h: "h", K_i: "i", K_j: "j",
    K_k: "k", K_l: "l", K_m: "m", K_n: "n", K_o: "o",
    K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t",
    K_u: "u", K_v: "v", K_w: "w", K_x: "x", K_y: "y",
    K_z: "z", K_SPACE: " ", K_UNDERSCORE: "_",
    K_0: "0", K_1: "1", K_2: "2", K_3: "3", K_4: "4",
    K_5: "5", K_6: "6", K_7: "7", K_8: "8", K_9: "9",
    K_PLUS: "+", K_MINUS: "-", K_COLON: ":",
    K_SLASH: "/"
}

KEYS = {}

def expect_key(expected=[]):
    while True:
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT: quit()
            if e.type == KEYDOWN:
                if expected:
                    if e.key in expected:
                        return e.key
                else:
                    return e.key

def get_text_input(pos):
    string = ''
    while True:
        surf = Surface((128, 16))
        surf.fill((230, 230, 230))
        surf.blit(HEL16.render(string, 0, (0, 0, 0)), (0, 0))
        SCREEN.blit(surf, pos)
        pygame.display.update()

        inp = expect_key()
        if inp == K_ESCAPE: return False
        if inp == K_BACKSPACE: string = string[:-1]
        if inp == K_RETURN: return string
        
        if pygame.key.get_mods() & KMOD_SHIFT:
            if inp in ALPHABET_KEY_MAP:
                string = string + ALPHABET_KEY_MAP[inp].upper()
        elif inp in ALPHABET_KEY_MAP:
            string = string + ALPHABET_KEY_MAP[inp]

def draw_cursor():
    pygame.draw.line(SCREEN, (255, 0, 0),
                     (PW*X, PW*Y),
                     (PW*X+PW, PW*Y+PW))

def draw_room():
    for y, line in enumerate(room):
        for x, slot in enumerate(line):
            for token in slot:
                col1, col2 = TILE_COLORS[token]
                tk.draw_token(SCREEN, token, (PW*x, PW*y),
                              col1=col1, col2=col2, PW=PW//16)

def draw_HUD():
    HUD = Surface((PW * 16, PW * 4))
    HUD.fill((150, 150, 150))
    for i, key in enumerate(KEYS.keys()):
        text = ALPHABET_KEY_MAP[key] if key in ALPHABET_KEY_MAP else key
        HUD.blit(HEL16.render(str(text) + " : " + KEYS[key], 0, (0, 0, 0)), (PW*8, i*16))
    SCREEN.blit(HUD, (0, PW*16))

    current = room[Y][X]
    for i, token in enumerate(current):
        col1, col2 = TILE_COLORS[token]
        tk.draw_token(SCREEN, token, (i*16, PW*16),
                      col1=col1, col2=col2, PW=1)

def put(name):
    room[Y][X].append(name)

def assign(key, name):
    KEYS[key] = name

while True:
    SCREEN.fill((80, 80, 80))
    draw_room()
    draw_cursor()
    draw_HUD()
    pygame.display.update()
    inp = expect_key()

    if pygame.key.get_mods() & KMOD_SHIFT:
        if inp == K_RIGHT:
            W += 1
            X = W - 1
            for line in room: line.append(["empty"])
        elif inp == K_LEFT:
            W -= 1
            X = W - 1
            for line in room: line.pop()
        elif inp == K_UP:
            H += 1
            Y = H - 1
            room.append([])
            for _ in range(W): room[-1].append(["empty"])
        elif inp == K_DOWN:
            H -= 1
            Y = H - 1
            room.pop()
        elif inp == K_RETURN:
            SCREEN.blit(HEL16.render("Save: ", 0, (0, 0, 0)), (0, 16*39))
            save(get_text_input((64, 16*39)))
        elif inp == K_BACKSPACE:
            SCREEN.blit(HEL16.render("Load: ", 0, (0, 0, 0)), (0, 16*39))
            load(get_text_input((64, 16*39)))
        elif inp not in [K_LSHIFT, K_RSHIFT, K_LEFT,
                         K_RIGHT, K_UP, K_DOWN,
                         K_RETURN, K_BACKSPACE]:
            key = ALPHABET_KEY_MAP[inp] if inp in ALPHABET_KEY_MAP else inp
            SCREEN.blit(HEL16.render("set key " + str(key) + ": ", 0, (0, 0, 0)), (0, 16*39))
            assign(inp, get_text_input((128, 16*39)))
    else:
        if inp == K_RIGHT: X = (X + 1) % W
        elif inp == K_LEFT: X = (X - 1) % W
        elif inp == K_UP: Y = (Y - 1) % H
        elif inp == K_DOWN: Y = (Y + 1) % H
        elif inp == K_BACKSPACE:
            if len(room[Y][X]) > 1: room[Y][X].pop()
        elif inp in KEYS: put(KEYS[inp])
    
