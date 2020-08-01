from src.locals import *

THEME_MAP = {
    "DEFAULT": {
        "ROOMS": ["*"],
        "COLORS": TILE_COLORS,
        "ENEMIES": {
            "COMMON": ["rat", "snake"],
            "RARE": ["skeleton", "bandit"],
            "BOSS": ["banditking", "gravekeep"],
        }
    },
    "BANDITCAVE": {
        "ROOMS": ["splitplus", "revsplitplus", "jail",
                  "itemroom", "itemplus", "gaurded",
                  "crossway", "crossway"],
        "COLORS": {
            "stone": (DARKBROWN, BLACK),
            "floor": (GRAY, BLACK),
            "wall": (DARKRED, BROWN),
            "door": (RED, LIGHTRED),
        },
        "ENEMIES": {
            "COMMON": ["rat"],
            "RARE": ["bandit"],
            "BOSS": ["banditking"],
        }
    },
    "GRAVEYARD" : {
        "ROOMS": [
            "gravesitesmall", "gravesitemed", "gravesitelarge",
            "cathedral", "itemroom", "shed", "diagb", "diagf"
        ],
        "COLORS": {
            "floor": (LIGHTBROWN, LIGHTBROWN),
            "stone": (DARKGREEN, DARKBROWN),
            "wall": (DARKBROWN, BROWN),
            "door": (BROWN, DARKBROWN),
        },
        "ENEMIES": {
            "COMMON": ["snake"],
            "RARE": ["skeleton"],
            "BOSS": ["gravekeep"],
        }
    },
    
}
