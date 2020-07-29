#lurd.py
"""
Here we go

Roguelike, use token system for graphics
"""
from src.game import setup_game, run_game

import sys

DEBUG = "-d" in sys.argv
LIMIT = 15
if "-l" in sys.argv:
    try:
        LIMIT = int(sys.argv[sys.argv.index("-l") + 1])
    except: pass

if __name__ == """__main__""":
    G = setup_game(LIMIT, DEBUG)
    if run_game(G):
        print("You did it!")
    else:
        print("You are dead.")

