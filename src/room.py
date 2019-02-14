# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []  # list of items
        self.n_to = {}
        self.e_to = {}
        self.s_to = {}
        self.w_to = {}

    def __str__(self):
        item_col = ""
        if len(self.items) == 1:
            item_col = "a " + self.items
        elif len(self.items) > 1:
            item_col = ', '.join(self.items)
        else:
            item_col = "nothing"

        return(f'You have entered the {self.title}.\n{self.description}\n\nThere is {item_col} in here.')
