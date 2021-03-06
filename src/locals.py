# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (30, 30, 30)
GRAY = (100, 100, 100)
LIGHTGRAY = (180, 180, 180)
RED = (255, 0, 0)
DARKRED = (128, 0, 0)
LIGHTRED = (255, 64, 64)
GREEN = (0, 255, 0)
DARKGREEN = (0, 128, 0)
LIGHTGREEN = (64, 255, 64)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 128)
LIGHTBLUE = (64, 64, 255)
YELLOW = (255, 255, 0)
DARKYELLOW = (128, 128, 0)
LIGHTYELLOW = (255, 255, 40)
CYAN = (0, 255, 255)
DARKCYAN = (0, 128, 128)
LIGHTCYAN = (64, 255, 255)
PURPLE = (255, 0, 255)
DARKPURPLE = (128, 0, 128)
LIGHTPURPLE = (255, 64, 255)
BROWN = (165, 42, 42)
DARKBROWN = (100, 30, 30)
LIGHTBROWN = (180, 64, 64)

TANGIBLES = [
    "stone", "wall", "grave",
]

# Default, themes override 
TILE_COLORS = {
    "stone": (GRAY, BLACK),
    "upstairs": (DARKYELLOW, CYAN),
    "downstairs": (DARKYELLOW, CYAN),
    "floor": (LIGHTGRAY, BLACK),
    "wall": (DARKBLUE, DARKPURPLE),
    "empty": (LIGHTGRAY, BLACK),
    "door": (LIGHTBLUE, BROWN),
    "alter": (BLUE, CYAN),
    "grave": (GRAY, WHITE),
    "boards": (BROWN, LIGHTGRAY),

    "enemyspawn": (RED, BLACK),
    "itemspawn": (GREEN, BLACK),
}
