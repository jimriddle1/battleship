import sys

from lib.ship import Ship
import unittest

NUMBER_1 = 3.0
NUMBER_2 = 2.0
FAILURE = 'incorrect value'


class ShipTest(unittest.TestCase):
    # def setUp(self):
    #     self.ship = Ship("Cruiser", 3)

    def test_instantiate(self):
        ship_1 = Ship("Cruiser", 3)
        self.assertEqual(ship_1.name, "Cruiser")
        self.assertEqual(ship_1.length, 3)
        self.assertEqual(ship_1.health, 3)
        self.assertEqual(ship_1.sunk, False)

    def test_take_hits(self):
        ship_1 = Ship("Cruiser", 3)
        self.assertEqual(ship_1.health, 3)
        ship_1.hit()
        self.assertEqual(ship_1.health, 2)
