import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase): 
    
    def setUp(self):
        #  Coffee Shop = Name, Price
        self.coffee_shop = CoffeeShop("Caffin8", 500)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Caffin8", self.coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(500, self.coffee_shop.till)

    def test_coffee_shop_increases_till(self):
        self.coffee_shop.increase_till(2)
        self.assertEqual(502, self.coffee_shop.till)

    def test_sell_if_customer_old_enough(self):
        customer = Customer("Charlie", 50, 25)
        self.coffee_shop.check_age(customer)
        self.assertEqual(True, self.coffee_shop.check_age(customer))

    def test_sell_if_customer_exactly_old_enough(self):
        customer = Customer("Sophie", 50, 16)
        self.coffee_shop.check_age(customer)
        self.assertEqual(True, self.coffee_shop.check_age(customer))

    def test_sell_if_customer_not_old_enough(self):
        customer = Customer("Sam", 50, 14)
        self.coffee_shop.check_age(customer)
        self.assertEqual(False, self.coffee_shop.check_age(customer))
    
    def test_customer_energy_level_ok(self):
        customer = Customer("Sam", 50, 14)
        self.coffee_shop.check_energy(customer)
        self.assertEqual("Drink served", self.coffee_shop.check_energy(customer))

    def test_customer_energy_level_too_high(self):
        customer = Customer("Sam", 50, 14)
        drink = Drink("Coffee Bomb", 3.00, 16)
        customer.increase_energy(drink)
        self.coffee_shop.check_energy(customer)
        self.assertEqual("Service refused", self.coffee_shop.check_energy(customer))