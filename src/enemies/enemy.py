from src.enemies.brains import *
from src.locals import *

ENEMIES = {
    "snake": {
        "name": "snake",
        "token": "snake",
        "colors": (RED, GREEN),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 5,
        "HP": 4,
        "ATK": 2,
        "DEF": 2,
        "SPEED": 1,
        
        "DROP": None,
    },
    "rat": {
        "name": "rat",
        "token": "rat",
        "colors": (RED, BROWN),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 5,
        "HP": 6,
        "ATK": 2,
        "DEF": 1,
        "SPEED": 1,
        
        "DROP": None,
    },
    "skeleton": {
        "name": "skeleton",
        "token": "skeleton",
        "colors": (DARKRED, GRAY),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 10,
        "HP": 15,
        "ATK": 3,
        "DEF": 3,
        "SPEED": 1,
        
        "DROP": None,
    },
    "bandit": {
        "name": "bandit",
        "token": "bandit",
        "colors": (RED, YELLOW),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 20,
        "HP": 20,
        "ATK": 6,
        "DEF": 4,
        "SPEED": 1,
        
        "DROP": None,
    },

}

def attack(enemy, player):
    player["HP"] -= max(1, enemy["ATK"] - player["DEF"])
    print(enemy["name"] + " hits you!")
    print(player["HP"])
    
def make_enemy(name, pos):
    nme = ENEMIES[name].copy()
    nme["POS"] = pos
    return nme

def update_enemies(G, player):
    grid = G["DUNGEON"][G["FLOOR"]]
    enemylist = G["ACTORS"][G["FLOOR"]]
    deadlist = []
    for enemy in enemylist:
        if enemy["HP"] <= 0: deadlist.append(enemy)
        elif enemy["active"]:
            enemy["update function"](grid, enemy, player)
    for enemy in deadlist:
        enemylist.remove(enemy)
