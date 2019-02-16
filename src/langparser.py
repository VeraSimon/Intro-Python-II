import re


class LangParser:
    def __init__(self, player):
        self.player = player
        self.dic = {
            "i": self.player.inventory_list,  # inventory
            "inventory": self.player.inventory_list,  # inventory
            "description": self.room_desc,  # describes the current room
            "h": self.game_help,  # help
            "help": self.game_help,  # help
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
            self.player.move(cnt_input + "_to")
        elif re.match("g", cnt_input) or re.match("grab", cnt_input) or re.match("take", cnt_input):
            item = cnt_input.split(' ')
            if len(item) == 2:
                self.player.on_take(item[1])
        elif re.match("d", cnt_input) or re.match("drop", cnt_input):
            item = cnt_input.split(' ')
            if len(item) == 2:
                self.player.on_drop(item[1])
        elif cnt_input in self.dic:
            return self.dic[cnt_input]()
        else:
            print("I don't understand that...\n")

    def room_desc(self):
        # Just a drop-through to let the player get the room info without the accompanying "I don't understand that..."
        print("\n")

    def game_help(self):
        for k, v in self.help.items():
            print(f"{k}: {v}")

    def quit_game(self):
        quit()
