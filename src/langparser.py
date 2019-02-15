class LangParser:
    def __init__(self, player):
        # TODO: Map each entry in the dic to actions
        self.player = player
        self.dic = {
            "n": "Moves north",  # north
            "e": "Moves east",  # east
            "s": "Moves south",  # south
            "w": "Moves west",  # west
            "g": "",  # grab
            "grab": "",  # grab
            "take": "",  # grab
            "d": "",  # drop
            "drop": "",  # drop
            "i": "",  # inventory
            "inventory": "",  # inventory
            "description": "",  # describes the current room
            "h": "",  # help
            "help": "",  # help
            "q": self.quit_game,  # quit
            "quit": self.quit_game  # quit
        }

        self.help = {
            "n": "Moves north if possible",
            "e": "Moves east if possible",
            "s": "Moves south if possible",
            "w": "Moves west if possible",
            "g": "Pick up an item",
            "grab": "Pick up an item",
            "take": "Pick up an item",
            "d": "Drop an item",
            "drop": "Drop an item",
            "i": "Show your inventory",
            "inventory": "Show your inventory",
            "description": "Describes the current room",
            "h": "Shows the help",
            "help": "Shows the help",
            "q": "Quits the game",
            "quit": "Quits the game"
        }

    def control_parse(self):
        cnt_input = input("What would you like to do? ")
        if cnt_input == "n" or cnt_input == "e" or cnt_input == "s" or cnt_input == "w":
            self.move(cnt_input + " to")
        elif cnt_input == "g" or cnt_input == "grab" or cnt_input == "take":
            pass
        elif cnt_input == "d" or cnt_input == "drop":
            pass
        elif cnt_input in self.dic:
            return self.dic[cnt_input]()
        else:
            print("I don't understand that...\n")

    def move(self, direction):
        cur_room = self.player.room
        if hasattr(cur_room, direction):
            self.player.room = cur_room[direction]

    def quit_game(self):
        quit()
