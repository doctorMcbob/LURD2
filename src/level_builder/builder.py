from random import randint

from src.utils import distance
from src.drawing import loading_screen_update

def fresh_floor(W, H, ent=False, ext=False):
    floor = []
    for y in range(H):
        floor.append([])
        for x in range(W):
            floor[-1].append([])
            if (x, y) == ent: floor[-1][-1].append("downstairs")
            elif (x, y) == ext: floor[-1][-1].append("upstairs")
            else: floor[-1][-1].append("stone")
    return floor

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
        floors.append(floor)
    return floors
