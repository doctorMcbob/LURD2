"""
items.py, hoping to randomly generate equptable items
potions will come later
"""
from random import choice
from src.locals import *
from src.utils import log
from src.themes import themes
from copy import deepcopy
THEME_MAP = themes.THEME_MAP

ITEM_TEMPLATE = {
    "NAME": None,
    "POS": None,
    "TRAITS": [],

    "colors": None,
    "token": None,

}

KEYWORD_COLOR_MAP = {
    "plain": (BLACK, WHITE),
    "stolen": (GREEN, DARKYELLOW),
    "heavy": (DARKBLUE, DARKGRAY),
    "smoggy": (DARKPURPLE, DARKGREEN),
    "flimsy": (BLACK, LIGHTBROWN),
    "menacing": (DARKRED, LIGHTRED),
    "lawless": (DARKYELLOW, DARKGRAY),
    "red": (RED, RED),
    "absolutely fucking bonkers": (CYAN, LIGHTPURPLE),
    "rotten": (DARKGREEN, GREEN),
    "haunted": (DARKBLUE, DARKGREEN),
    "grim": (DARKBLUE, LIGHTGRAY),
    "lifeless": (BLACK, BLACK),
    "eerie": (LIGHTGRAY, LIGHTCYAN),
    "forgotten": (DARKBROWN, WHITE),
    "spooky": (DARKCYAN, LIGHTRED),
    "deathly": (BLACK, DARKRED),
    "busted": (LIGHTRED, LIGHTYELLOW),
    "drunken": (DARKCYAN, CYAN),
    "shipwreaked": (DARKBLUE, LIGHTBLUE),
    "swarvy": (GREEN, DARKBLUE),
    "swashbuckling": (DARKBROWN, LIGHTYELLOW),
    "limey": (DARKCYAN, LIGHTGREEN),
    "salty": (LIGHTGRAY, WHITE),
    "landlubbing": (DARKBROWN, LIGHTBLUE),
}

def make_sword(theme, pos):
    theme = THEME_MAP[theme]
    sword = deepcopy(ITEM_TEMPLATE)
    sword["POS"] = pos
    sword["token"] = "sword"
    keyword = choice(list(theme["ITEMKEYWORDS"].keys()))
    sword["colors"] = KEYWORD_COLOR_MAP[keyword]
    sword["MODS"] = theme["ITEMKEYWORDS"][keyword].split(",")
    sword["MODS"].append("ATK +2")
    sword["NAME"] = "The " + keyword + " sword"
    sword["TRAITS"].append("EQUIPTABLE")
    sword["TRAITS"].append("WEAPON")
    return sword

def make_shield(theme, pos):
    theme = THEME_MAP[theme]
    shield = deepcopy(ITEM_TEMPLATE)
    shield["POS"] = pos
    shield["token"] = "shield"
    keyword = choice(list(theme["ITEMKEYWORDS"].keys()))
    shield["colors"] = KEYWORD_COLOR_MAP[keyword]
    shield["MODS"] = theme["ITEMKEYWORDS"][keyword].split(",")
    shield["MODS"].append("DEF +2")
    shield["NAME"] = "The " + keyword + " shield"
    shield["TRAITS"].append("EQUIPTABLE")
    shield["TRAITS"].append("ARMOR")
    return shield

def get(player, item, G):
    G["ITEMS"][G["FLOOR"]].remove(item)
    if "CURRENCY" in item["TRAITS"]:
        player["CURRENCY"][item["NAME"]] += 1
    else:
        player["INV"].append(item)
    log(G, "Got " + item["NAME"])

def dequipt(player, slot, G):
    item = player[slot]
    player[slot] = None
    player["INV"].append(item)
    for mod in item["MODS"]:
        stat, alt = mod.split()
        if stat == "HP": stat = "HPMAX"
        if alt[0] == "+": player[stat] -= int(alt[1:])
        if alt[0] == "-": player[stat] += int(alt[1:])

    log(G, "Unequipted " + item["NAME"])
    
def equipt(player, item, G):
    if "EQUIPTABLE" not in item["TRAITS"]:
        log(G, "Thats not equiptable")
    if item not in player["INV"]:
        log(G, "Cant equipt item you dont have")
        return

    if "ARMOR" in item["TRAITS"]: slot = "ARMOR"
    if "WEAPON" in item["TRAITS"]: slot = "WEAPON"

    if player[slot]:
        dequipt(player, slot, G)
            
    player["INV"].remove(item)
    player[slot] = item
    for mod in item["MODS"]:
        stat, alt = mod.split()
        if stat == "HP": stat = "HPMAX"
        if alt[0] == "+": player[stat] += int(alt[1:])
        if alt[0] == "-": player[stat] -= int(alt[1:])

    log(G, "Equipted " + item["NAME"])
    log(G, ", ".join(item["MODS"]))
    
