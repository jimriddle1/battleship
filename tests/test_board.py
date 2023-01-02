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
        self.assertEqual(board_1.cells["A1"].render(), ".")

    def test_valid_coordinate(self):
        board_1 = Board()
        self.assertEqual(board_1.is_valid_coordinate("A1"), True)
        self.assertEqual(board_1.is_valid_coordinate("D4"), True)
        self.assertEqual(board_1.is_valid_coordinate("A5"), False)
        self.assertEqual(board_1.is_valid_coordinate("E1"), False)
        self.assertEqual(board_1.is_valid_coordinate("A22"), False)
