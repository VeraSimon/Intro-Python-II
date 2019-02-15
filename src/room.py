# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []  # list of items

    def __str__(self):
        item_col = ""
        if len(self.items) == 1:
            item_col = "a " + self.items
        elif len(self.items) > 1:
            item_col = ', '.join(self.items)
        else:
            item_col = "nothing"

        return(f'You have entered the {self.title}. {self.description}\nThere is {item_col} in here.\n')

    def __getitem__(self, direction):
        if direction == "n_to":
            return self.n_to
        elif direction == "e_to":
            return self.e_to
        elif direction == "s_to":
            return self.s_to
        elif direction == "w_to":
            return self.w_to
        else:
            return (self.title, self.description)
