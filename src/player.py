from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, room):
        self.items = []
        self.name = name
        self.room = room

    def __str__(self):
        item_col = ""
        if len(self.items) == 1:
            item_col = "a " + self.items
        elif len(self.items) > 1:
            item_col = ', '.join(self.items)
        else:
            item_col = "nothing"

        return(f'You currently have {item_col}.\n')

    def move(self, direction):
        # print(f"dir: {direction}")
        # new_room = self.room[direction]
        # print(f"new room: {new_room}")
        if hasattr(self.room, direction):
            self.room = self.room[direction]
            print("\n")
        else:
            print("There's nowhere to go in that direction...\n")
