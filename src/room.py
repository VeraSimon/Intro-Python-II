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
