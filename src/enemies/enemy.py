from src.enemies.brains import *
from src.locals import *
from src.utils import log

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
    "banditking": {
        "name": "bandit king",
        "token": "banditking",
        "colors": (LIGHTRED, DARKYELLOW),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 40,
        "HP": 30,
        "ATK": 7,
        "DEF": 3,
        "SPEED": 1,

        "DROP": None,
    },
    "gravekeep": {
        "name": "grave keeper",
        "token": "gravekeep",
        "colors": (DARKGRAY, DARKRED),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 40,
        "HP": 30,
        "ATK": 7,
        "DEF": 3,
        "SPEED": 1,

        "DROP": None,
    },
    "pirate": {
        "name": "pirate",
        "token": "pirate",
        "colors": (DARKRED, LIGHTBROWN),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 15,
        "HP": 14,
        "ATK": 8,
        "DEF": 4,
        "SPEED": 1,
        
        "DROP": None,
    },
    "pirateking": {
        "name": "pirate king",
        "token": "pirateking",
        "colors": (BLACK, LIGHTRED),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 40,
        "HP": 15,
        "ATK": 9,
        "DEF": 3,
        "SPEED": 1,
        
        "DROP": None,
    },
    "skallywag": {
        "name": "skallywag",
        "token": "skallywag",
        "colors": (BLACK, LIGHTBROWN),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 6,
        "HP": 5,
        "ATK": 4,
        "DEF": 1,
        "SPEED": 1,
        
        "DROP": None,
    },
    "skull": {
        "name": "skull effigy",
        "token": "skull",
        "colors": (BLACK, WHITE),
        "POS": None,
        "update function": rand_strike,
        "active": True,

        "EXP": 15,
        "HP": 10,
        "ATK": 1,
        "DEF": 4,
        "SPEED": 1,
        
        "DROP": None,
    },

}

def attack(enemy, G, player):
    player["HP"] -= max(1, enemy["ATK"] - player["DEF"])
    log(G,
        "The "+enemy["name"]+" strikes you"
    )
    
def make_enemy(name, pos):
    nme = ENEMIES[name].copy()
    nme["POS"] = pos
    return nme

def update_enemies(G, player):
    enemylist = G["ACTORS"][G["FLOOR"]]
    deadlist = []
    for enemy in enemylist:
        if enemy["HP"] <= 0: deadlist.append(enemy)
        elif enemy["active"]:
            enemy["update function"](G, enemy, player)
    for enemy in deadlist:
        enemylist.remove(enemy)
