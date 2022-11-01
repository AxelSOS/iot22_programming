
class Player:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_ai(cls, logic_file=None):
        # Gör massa saker
        return cls("CPU")


if __name__ == '__main__':
    main_player = Player("Player 1")
    computer_player = Player.from_ai()
