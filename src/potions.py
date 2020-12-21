"""
potion color decides stat / modifier 

potion keyword decides action
"""
from src.locals import *

COLORS = {
    RED: "",
    BLUE: "",
    GREEN: "",
    YELLOW: "",
    CYAN: "",
    PURPLE: "",
    BROWN: "",
}

KEYWORDS = {
    "": ""
}

def apply_potion(POTION, character):
    color_mods = COLORS[POTION["COLORS"][1]]
    keyword = POTION["KEYWORD"]
    
