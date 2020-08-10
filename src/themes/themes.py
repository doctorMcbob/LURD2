from src.locals import *

THEME_MAP = {
    "DEFAULT": {
        "ROOMS": ["*"],
        "COLORS": TILE_COLORS,
        "ENEMIES": {
            "COMMON": ["rat", "snake"],
            "RARE": ["skeleton", "bandit"],
            "BOSS": ["banditking", "gravekeep"],
        },
        "ITEMKEYWORDS" : {
            "plain": "ATK +1"
        },
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
        },
        "ITEMKEYWORDS" : {
            "stolen": "ATK +2,DEF +1",
            "heavy": "DEF +3",
            "smoggy": "ATK +1,HP +2",
            "flimsy": "ATK +1",
            "menacing": "ATK +2,DEF +1",
            "lawless": "HP +4",
            "red": "DEF +2,HP +1",
            "absolutely fucking bonkers": "ATK +4,DEF +2,HP +2",
        },
    },
    "GRAVEYARD": {
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
        },
        "ITEMKEYWORDS" : {
            "rotten": "ATK +1",
            "haunted": "ATK +1,DEF +1",
            "grim": "HP +2,DEF +1",
            "lifeless": "ATK +4,DEF -1",
            "eerie": "HP +3,DEF +1",
            "forgotten": "ATK +2,HP +2",
            "spooky": "ATK +1,HP +3",
            "deathly": "ATK +3",
        },
    },
    "PIRATEKEEP": {
        "ROOMS": [
            "shipd", "shipu", "boat", "boatside",
            "lilboatup", "lilboatd"
        ],
        "COLORS": {
            "floor": (LIGHTBLUE, CYAN),
            "stone": (DARKBLUE, BLUE),
            "wall": (DARKBROWN, BROWN),
            "door": (BROWN, DARKBROWN),
        },
        "ENEMIES": {
            "COMMON": ["skallywag", "rat"],
            "RARE": ["pirate", "skull"],
            "BOSS": ["pirateking"],
        },
        "ITEMKEYWORDS" : {
            "busted": "ATK +3",
            "drunken": "DEF +2,HP +2",
            "shipwreaked": "ATK +2,DEF+1",
            "swarvy": "DEF +3",
            "swashbuckling": "ATK +1,DEF +2,HP +1",
            "limey": "ATK +1,DEF +1",
            "salty": "DEF +2,HP +2",
            "landlubbing": "DEF +4",
        },
    },
}
