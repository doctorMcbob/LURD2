import pygame
from pygame.locals import *

from src.locals import *

def expect_key(expectlist=[]):
    while True:
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT: quit()
            if e.type == KEYDOWN:
                if expectlist:
                    if e.key in expectlist: return e.key
                else: return e.key


def distance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def solvable(grid, ent, ext):
    checklist = [ent]
    marked = []
    while checklist and ext not in marked:
        X, Y = checklist.pop()
        for x, y in [(X+1, Y), (X-1, Y), (X, Y+1), (X, Y-1)]:
            if (x < 0 or x > len(grid[0])-1 or
                y < 0 or y > len(grid)-1): continue
            token = grid[y][x][-1]
            if token not in TANGIBLES:
                if ((x, y) not in checklist and
                    (x, y) not in marked):
                    checklist = [(x, y)] + checklist
        marked.append((X, Y))
    return ext in marked, marked + checklist
