import sys

from lib.ship import Ship
from lib.cell import Cell
import unittest

class CellTest(unittest.TestCase):

    def test_instantiate(self):
        cell_1 = Cell("B4")
        self.assertEqual(cell_1.coordinate, 'B4')
        self.assertEqual(cell_1.ship, None)
        self.assertEqual(cell_1.is_empty, True)

    def test_place_ship(self):
        cell_1 = Cell("B4")
        ship_1 = Ship("Cruiser", 3)
        cell_1.place_ship(ship_1)
        self.assertEqual(cell_1.ship, ship_1)
        self.assertEqual(cell_1.is_empty, False)

    def test_fired_upon(self):
        cell_1 = Cell("B4")
        ship_1 = Ship("Cruiser", 3)
        cell_1.place_ship(ship_1)
        self.assertEqual(cell_1.fired_upon, False)
        self.assertEqual(cell_1.ship.health, 3)
        cell_1.fire_upon()
        self.assertEqual(cell_1.fired_upon, True)
        self.assertEqual(cell_1.ship.health, 2)

    def test_render(self):
        cell_1 = Cell("B4")
        self.assertEqual(cell_1.render, '.')

        cell_1.fire_upon()
        self.assertEqual(cell_1.render, 'M')

        cell_2 = Cell("C2")
        ship_1 = Ship("Cruiser", 3)
        cell_2.place_ship(ship_1)

        self.assertEqual(cell_2.render, 'S')

        cell_2.fire_upon()
        self.assertEqual(cell_2.render, 'H')
        self.assertEqual(cell_2.ship.health, 2)

        cell_2.fire_upon()
        cell_2.fire_upon()
        self.assertEqual(cell_2.ship.health, 0)
        self.assertEqual(cell_2.render, 'X')
