import sys
# import dict

from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board
import unittest

class ShipTest(unittest.TestCase):

    def test_instantiate(self):
        board_1 = Board()
        self.assertEqual(len(board_1.cells.keys()), 16)
        self.assertEqual(board_1.cells["A1"].render, ".")
        # self.assertEqual(ship_1.length, 3)
        # self.assertEqual(ship_1.health, 3)
        # self.assertEqual(ship_1.sunk, False)
