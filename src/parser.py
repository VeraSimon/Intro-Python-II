class Parser:
    def __init__(self, command):
        # TODO: Map each entry in the dic to actions
        self.dic = {
            "n": "",  # north
            "e": "",  # east
            "s": "",  # south
            "w": "",  # west
            "g": "",  # grab
            "grab": "",  # grab
            "take": "",  # grab
            "d": "",  # drop
            "drop": "",  # drop
            "i": "",  # inventory
            "inventory": "",  # inventory
            "h": "",  # help
            "help": "",  # help
            "q": "",  # quit
            "quit": ""  # quit
        }
