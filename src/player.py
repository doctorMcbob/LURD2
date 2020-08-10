from src.locals import *
from src.utils import get, apply_direction, log
from src import items

PLAYER_TEMPLATE = {
    "POS": (4, 4),
    "LVL": 0,
    "EXP": 0,
    "HP": 50,
    "HPMAX": 50,
    "ATK": 5,
    "DEF": 5,
    "SPEED": 1,
    "WEAPON": None,
    "ARMOR": None,
    "INV": [],
    "CURRENCY": {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0,
    },
    "token": "face",
    "colors": (BLACK, DARKGREEN)
}

PLAYER = PLAYER_TEMPLATE.copy()

def move(G, d, player=PLAYER):
    grid = G["DUNGEON"][G["FLOOR"]]
    enemylist = G["ACTORS"][G["FLOOR"]]
    itemlist = G["ITEMS"][G["FLOOR"]]
    move_slot = apply_direction(player["POS"], d)
    if any([n < 0 for n in move_slot]): return False
    try:
        if any([thing in TANGIBLES for thing in get(grid, move_slot)]):
            return False
    except IndexError: return False
    for enemy in enemylist:
        if move_slot == enemy["POS"]:
            attack(player, G, enemy)
            return True

    for item in itemlist:
        if move_slot == item["POS"]:
            items.get(player, item, G)

    player["POS"] = move_slot
    return True

def attack(player, G, enemy):
    enemy["HP"] -= max(1, player["ATK"] - enemy["DEF"])
    log(G,
        "You strike the "+enemy["name"]+" ("+str(enemy["HP"])+")"
    )
