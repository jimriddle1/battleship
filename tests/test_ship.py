import sys

from lib.ship import Ship
import unittest

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

    def test_shinks_ship(self):
        ship_1 = Ship("Cruiser", 2)
        self.assertEqual(ship_1.health, 2)
        self.assertEqual(ship_1.sunk, False)
        ship_1.hit()
        self.assertEqual(ship_1.sunk, False)
        ship_1.hit()
        self.assertEqual(ship_1.sunk, True)
