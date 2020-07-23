from src.locals import *
from src.utils import get, apply_direction

PLAYER_TEMPLATE = {
    "POS": (4, 4),
    "LVL": 0,
    "EXP": 0,
    "HP": 50,
    "ATK": 5,
    "DEF": 5,
    "SPEED": 1,
    "WEAPON": None,
    "ARMOR": None,
    "INV": [],
    "token": "face",
    "colors": (BLACK, DARKGREEN)
}

PLAYER = PLAYER_TEMPLATE.copy()

def move(grid, d, player=PLAYER):
    move_slot = apply_direction(player["POS"], d)
    if any([n < 0 for n in move_slot]): return False
    try:
        if any([thing in TANGIBLES for thing in get(grid, move_slot)]):
            return False
    except IndexError: return False
    player["POS"] = move_slot
    return True
