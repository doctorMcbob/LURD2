from random import randint, choice
from pathlib import Path
import os

from src.utils import insert_grid, check_rect_empty

room_path = Path(os.path.dirname(os.path.abspath(__file__))) / "bin"

ROOMS = {}
for room in os.listdir(room_path):
    try:
        with open(room_path/room, "r") as f:
            ROOMS[room] = eval(f.read())
    except:
        continue


def try_to_place_room(grid, room, attempts=5):
    gW, gH = len(grid[0]), len(grid)
    rW, rH = len(room[0]), len(room)
    for _ in range(attempts):
        x, y = randint(0, gW-rW), randint(0, gH-rH)
        if check_rect_empty(grid, (x, y), (rW, rH)):
            insert_grid(grid, room, (x, y))
            return True
    return False
    
def apply_rooms(grid):
    room = choice(list(ROOMS.keys()))
    while try_to_place_room(grid, ROOMS[room].copy()):
        room = choice(list(ROOMS.keys()))

    
