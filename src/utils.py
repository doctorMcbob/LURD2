import pygame
from pygame.locals import *

from src.locals import *

def push(grid, pos, what): grid[pos[1]][pos[0]].append(what)
def get(grid, pos): return grid[pos[1]][pos[0]]
def getdim(grid): return len(grid[0]), len(grid)

def allof(grid, piece):
    for y, line in enumerate(grid):
        for x, slot in enumerate(line):
            if piece in slot: yield (x, y)

def getsub(grid, pos, dim):
    return [line[pos[0]:pos[0]+dim[0]] for line in grid[pos[1]:pos[1]+dim[1]]]

def boardisequal(b1, b2):
    if len(b1) != len(b2): return False
    if len(b1[0]) != len(b2[0]): return False
    for y, line in enumerate(b1):
        for x, slot in enumerate(line):
            if slot[-1] != get(b2, (x, y))[-1]: return False
    return True

def findsub(grid, sub):
    dim = getdim(sub)
    checklist = allof(grid, get(sub, (0, 0))[-1])
    ret = []
    for pos in checklist:
        try:
            if boardisequal(getsub(grid, pos, dim), sub):
                ret.append(pos)
        except IndexError: continue
    return ret

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
            slot = get(grid, (x, y))
            token = slot[-1] if slot else "empty"
            if token not in TANGIBLES:
                if ((x, y) not in checklist and
                    (x, y) not in marked):
                    checklist = [(x, y)] + checklist
        marked.append((X, Y))
    return ext in marked, marked + checklist

def insert_grid(dest, ins, pos):
    """
    both dest and ins are 2d arrays, assumes they are rectangular

    each cell in 2d array is a stack, so for each cell it 
    stacks the ins on top of the dest
    """
    X, Y = pos
    for y, line in enumerate(ins):
        for x, slot in enumerate(line):
            if "empty" in slot: slot.remove("empty")
            p = get(dest, (X+x, Y+y))
            p += slot

def check_rect_empty(grid, pos, dim):
    X, Y = pos
    W, H = dim
    for y in range(H):
        for x in range(W):
            if get(grid, (X+x, Y+y)): return False
    return True

def apply_direction(pos, d):
    # URDL syntax
    if d == 0: return pos[0], pos[1]-1
    if d == 1: return pos[0]+1, pos[1]
    if d == 2: return pos[0], pos[1]+1
    if d == 3: return pos[0]-1, pos[1]

def insight(grid, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = distance(p1, p2)
    for n in range(d):
        #pathfind from p1 to p2
        x = (x1 + x2) // d
        y = (y1 + y2) // d
        print(x * n, y * n)
        if any([item in TANGIBLES
                for item in get(grid, (x, y))]):
            return False
    return True

def update_lit(grid, lights, lit):
    for y, line in enumerate(grid):
        for x, stack in enumerate(line):
            if (x, y) in lit:
                continue
            else:
                if any([insight(grid, light, (x, y)) for light in lights]):
                    lit.add((x, y))
