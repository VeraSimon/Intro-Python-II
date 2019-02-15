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
            print("You have the following items:")
            for item in self.items:
                print(f"{item.name} ({item.description})")
            print("\n")
        else:
            print("You are not carrying anything.\n")

    def on_take(self, item):
        index = -1
        for i, val in enumerate(self.room.items):
            if val.name == item:
                index = i
                self.items.append(val)
        if index > -1:
            self.room.items.pop(i)
        else:
            print(f"There's no {item} around here...\n")

    def on_drop(self, item):
        index = -1
        for i, val in enumerate(self.items):
            if val.name == item:
                index = i
                self.room.items.append(val)
        if index > -1:
            self.items.pop(i)
        else:
            print(f"There's no {item} in your inventory...\n")
