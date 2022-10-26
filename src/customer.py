from src.coffee_shop import CoffeeShop


class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = 0
        # energy level max is 15

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink, coffee_shop):
        self.decrease_wallet(drink.price)
        coffee_shop.increase_till(drink.price)

    def increase_energy(self, drink):
        self.energy += drink.caffeine_level
