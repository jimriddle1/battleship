import sys

from lib.ship import Ship
from lib.cell import Cell
import unittest

class CellTest(unittest.TestCase):
    # def setUp(self):
    #     self.ship = Ship("Cruiser", 3)

    def test_instantiate(self):
        cell_1 = Cell("B4")
        # breakpoint()
        self.assertEqual(cell_1.coordinate, 'B4')
        self.assertEqual(cell_1.ship, None)
        self.assertEqual(cell_1.empty, True)
