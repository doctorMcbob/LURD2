from random import randint, choice
from pathlib import Path
import os

from src.utils import insert_grid, check_rect_empty
from src.drawing import debug_floor
from src.themes import themes

room_path = Path(os.path.dirname(os.path.abspath(__file__))) / "bin"

ROOMS = {}
for room in os.listdir(room_path):
    try:
        with open(room_path/room, "r") as f:
            ROOMS[room] = eval(f.read())
    except:
        continue


def try_to_place_room(grid, roomlist, attempts=20):
    gW, gH = len(grid[0]), len(grid)
    if not roomlist: return False
    for _ in range(attempts):
        room = ROOMS[choice(roomlist)].copy()
        rW, rH = len(room[0]), len(room)
        if (gW-rW < 0 or gH-rH < 0): continue
        x, y = randint(0, gW-rW), randint(0, gH-rH)
        if check_rect_empty(grid, (x, y), (rW, rH)):
            insert_grid(grid, room, (x, y))
            return True
    return False
    
def apply_rooms(grid, THEME="DEFAULT", debug_surf=False):
    roomlist = themes.THEME_MAP[THEME]["ROOMS"]
    if "*" in roomlist: roomlist = list(ROOMS.keys())
    while try_to_place_room(grid, roomlist):
        if debug_surf:
            debug_floor(debug_surf, grid)
    
