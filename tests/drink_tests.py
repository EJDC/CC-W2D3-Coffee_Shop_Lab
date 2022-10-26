import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mocha", 2.50, 3)

    def test_drink_has_name(self):
        self.assertEqual("Mocha", self.drink.name)

    def test_dringk_has_caffeine_level(self):
        self.assertEqual(3, self.drink.caffeine_level)

    def test_drink_has_price(self):
        self.assertEqual(2.50, self.drink.price)