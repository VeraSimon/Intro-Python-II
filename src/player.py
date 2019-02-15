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
            item_col = "a " + self.items[0].name
        elif len(self.items) > 1:
            i_names = list(map(lambda nm: nm.name, self.items))
            item_col = 'a ' + 'and '.join(i_names)
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

    def inventory_list(self):
        if len(self.items) > 0:
            for item in self.items:
                print(f"{item.name} ({item.description})")
        else:
            print("You are not carrying anything.\n")
