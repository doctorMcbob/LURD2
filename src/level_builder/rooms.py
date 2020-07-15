from pathlib import Path
import os

room_path = Path(os.path.dirname(os.path.abspath(__file__))) / "bin"

ROOMS = {}
for room in os.listdir(room_path):
    try:
        with open(room_path/room, "r") as f:
            ROOMS[room] = eval(f.read())
    except:
        continue

def apply_rooms(grid):
    pass
