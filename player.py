import random


class Player:
    def __init__(self):
        self.score = 0
        self.weapon = int()

    def set_weapon(self, x):
        self.weapon = x

    def set_random_weapon(self):
        self.weapon = random.randint(0, 2)

    def get_weapon(self):
        return self.weapon

    def get_weapon_name(self):
        weapon = ('Rock', 'Paper', 'Scissors')
        return weapon[self.weapon]

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score
