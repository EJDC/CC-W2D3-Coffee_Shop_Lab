class CoffeeShop:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        if customer.age >= 16:
            return True
        else:
            return False

    def check_energy(self, customer):
        if customer.energy <= 15:
            return "Drink served"
        else:
            return "Service refused"
        