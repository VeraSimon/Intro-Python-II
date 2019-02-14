class LangParser:
    def __init__(self):
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
            "quit": self.quit_game()  # quit
        }

    def control_parse(self):
        cnt_input = input("What would you like to do?")
        if self.dic[cnt_input]:
            self.dic[cnt_input]
        else:
            print("I don't understand that...")
        return

    def quit_game(self):
        quit()
