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

    def move(self):
        pass
