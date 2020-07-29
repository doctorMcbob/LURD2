from random import randint

from src.enemies import enemy
from src.utils import *
from src.locals import *

def rand_strike(grid, this, player):
    if insight(grid, this["POS"], player["POS"]):
        x1, y1 = this["POS"]
        x2, y2 = player["POS"]
        line = get_line(x1, y1, x2, y2)
        new = line[line.index(this["POS"]) + 1]
        if new == player["POS"]:
            enemy.attack(this, player)
        else:
            this["POS"] = new
    else:
        random(grid, this, player)
    
def random(grid, this, player):
    d = randint(0, 3)
    new = apply_direction(this["POS"], d)
    if check_slot(grid, new, TANGIBLES): return
    if new == player["POS"]:
        enemy.attack(this, player)
    else:
        this["POS"] = new
