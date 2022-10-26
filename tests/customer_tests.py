import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Charlie", 50, 25)

    def test_customer_has_name(self):
        self.assertEqual("Charlie", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(25, self.customer.age)

    def test_customer_has_energy(self):
        self.assertEqual(0,self.customer.energy)

    def test_customer_can_buy_drink(self):
        coffee_shop = CoffeeShop("Caffin8", 500)
        coffee_shop.increase_till(2.50)
        self.customer.decrease_wallet(2.50)
        self.assertEqual(502.50, coffee_shop.till)
        self.assertEqual(47.50, self.customer.wallet)

    def test_customer_buy_drink(self):
        coffee_shop = CoffeeShop("Caffin8", 500)
        drink = Drink("Mocha", 2.50, 3)
        self.customer.buy_drink(drink, coffee_shop)
        self.assertEqual(502.50, coffee_shop.till)
        self.assertEqual(47.50, self.customer.wallet)

    def test_energy_level_increases(self):
        drink = Drink("Mocha", 2.50, 3)
        self.customer.increase_energy(drink)
        self.assertEqual(3, self.customer.energy)

    def test_food_decreases_energy(self):
        drink = Drink("Long Black", 2.50, 6)
        food = Food("Fajitas", 6.50, 5)
        self.customer.increase_energy(drink)
        self.customer.decrease_energy(food)
        self.assertEqual(1, self.customer.energy)

    def test_food_decreases_energy_never_less_than_zero(self):
        food = Food("Fajitas", 6.50, 5)
        self.customer.decrease_energy(food)
        self.assertEqual(0, self.customer.energy)

