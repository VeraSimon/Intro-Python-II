class Item:
    def __init__(self, name, description, loot_type):
        self.name = name
        self.description = description
        self.loot_type = loot_type

    def __str__(self):
        return f'{self.name} ({self.description})'
