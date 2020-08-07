# The Temple of L U R D
A roguelike made with Python and Pygame by me :) Wesley Wooten

#### What is LURD?
This is a direct sequal to [another roguelike I made](https://github.com/doctorMcbob/Rougelike)

L U R D stands for Left Up Right Down. In the original LURD these were the commands to move around. After implementing Pygame graphics, these commands got replaces with the arrow keys, but I liked the name so I kept it.

## How do I add to the game?
There are two scripts you will need to know about,

`src/tokens/builder.py` is a token drawing system.

`roombuilder.py` is a room building system.

I will go over how to use these programs later in the README.

There is a concept of Themes, each floor has a theme, you can find these at `src/themes/themes.py`

Themes have "ROOMS", "COLORS", and three tiers of "ENEMIES" (common, rare, boss). ROOMS are the names of rooms, saved with the roombuilder application. COLORS override the default colors, so you can customize the feeling of your theme. ENEMIES have to be built in `src/enemies/enemy.py`. common enemies and rare enemies are chosen randomly and each floor has one boss enemy.

### USING THE TOKEN BUILDER
`python src/tokens/builder.py`

tokens are 16 by 16. Each pixel in the token can be either 0, 1, or 2. 0 (default (1, 255, 1)) will be transperant, the other two colors will be decided in the theme.
tokens are saved as a list of integers, in `src/tokens/bin`

#### Keys
 - Arrow Keys  :  Move cursor
 - Space Bar   :  Change Pixel Value
 - Enter       :  Save (will ask for filename)
 - Backspace   :  Load (will ask for filename)

### USING THE ROOMBUILDER
`python roombuilder.py`

This one is a little more complex, you draw the room, save it as any filename, and that filename is how you load it in the theme.
You need to set your keys within the application, you can set any token to any key on your keyboard. For example, you can set the token "wall" to the W key, then when you press W you will place that token into the room.

Cells in the room are a stack, You can place a FLOOR token, and then put a ALTER token on top of that for example. 

rooms are saved to `src/level_builder/bin`

#### Keys
 - Shift and ...
	- Arrow Key        :  Change room size (width, height)
	- Enter            :  Save (will ask for filename)
	- Backspace        :  Load (will ask for filename)
	- (any other key)  :  Set key to any token (will ask for token name)
 - Arrow Keys         :  Move cursor
 - Backspace          :  Remove token from stack
 - (any set key)      :  Token set to that key

## Installation
Developed for Python 3

You will need Pygame
`pip3 install pygame`

run the game with
`python lurd.py`