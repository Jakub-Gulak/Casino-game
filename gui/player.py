import random


class Player:
    def __init__(self):
        self.name = ""
        self.money = random.randint(100, 1000)

    def set_name(self, name):
        self.name = name

    def get_money(self):
        return self.money

    def set_money(self, amount):
        self.money = amount


player = Player()
