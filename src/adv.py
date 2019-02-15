from langparser import LangParser
from room import Room
from player import Player
from item import Item

# Declare the items!

items = {
    'potion': Item("potion", "A murky liquid sealed in a vial with a cork.", "edible"),
    'dagger': Item("dagger", "A small double-edged weapon with nice balance.", "weapon"),
    'chainmail': Item("chainmail", "A piece of chest armour made by connecting many small rings together.", "armour"),
    'key': Item("key", "It's a bit rusty, but its got to open something, right?", "quest"),
    'lantern': Item("lantern", "If you found a flint and steel, this would definitely help seeing your way around.", "light"),
    'flint': Item("flint", "You could probably light something on fire with this with a little practice.", "junk")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", [items['lantern']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['dagger']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['flint']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['potion'], items['key']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input(f"Welcome to the land of Nod, adventurer. What is your name?\n>")
adventurer = Player(name, room["outside"])
print(f'\nWelcome to the Dungeon of Dread, {adventurer.name}!')

# Initialize the language parser
lnp = LangParser(adventurer)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print(Room(adventurer.room.title,
               adventurer.room.description, adventurer.room.items))
    lnp.control_parse()
