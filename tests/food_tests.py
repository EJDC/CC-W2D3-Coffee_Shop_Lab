import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        # food = name, price, rejuvenation level
        self.food = Food("Fajitas", 6.50, 5)

    def test_food_has_name(self):
        self.assertEqual("Fajitas", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(6.50, self.food.price)
        
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food.rejuvenation_level)

