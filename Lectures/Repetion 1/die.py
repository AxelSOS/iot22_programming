import random


class Die:
    def __init__(self, value=None):
        self.value = value

    def roll(self):
        self.value = random.randint(1, 6)


if __name__ == '__main__':
    d1 = Die(5)
    print(d1.value)

    d2 = Die()
    print(d2.value)
    d2.roll()
    print(d2.value)
