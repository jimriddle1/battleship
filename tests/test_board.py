import sys
# import dict

from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board
import unittest

class ShipTest(unittest.TestCase):

    def test_instantiate(self):
        board = Board()
        self.assertEqual(len(board.cells.keys()), 16)
        self.assertEqual(board.cells["A1"].render(), ".")

    def test_valid_coordinate(self):
        board = Board()
        self.assertEqual(board.is_valid_coordinate("A1"), True)
        self.assertEqual(board.is_valid_coordinate("D4"), True)
        self.assertEqual(board.is_valid_coordinate("A5"), False)
        self.assertEqual(board.is_valid_coordinate("E1"), False)
        self.assertEqual(board.is_valid_coordinate("A22"), False)

    def test_valid_placement(self):
        board = Board()
        cruiser = Ship("Cruiser", 3)
        sub = Ship("Submarine", 2)

        self.assertEqual(board.is_valid_placement(cruiser, ["A1", "A2"]), False)
        self.assertEqual(board.is_valid_placement(sub, ["B1", "B2", "B3"]), False)

        self.assertEqual(board.is_valid_placement(cruiser, ["A1", "A3", "A4"]), False)
        self.assertEqual(board.is_valid_placement(sub, ["A1", "C1"]), False)
        self.assertEqual(board.is_valid_placement(cruiser, ["A3", "A2", "A1"]), False)
        self.assertEqual(board.is_valid_placement(sub, ["C1", "B1"]), False)

        self.assertEqual(board.is_valid_placement(cruiser, ["A1", "B2", "C3"]), False)
        self.assertEqual(board.is_valid_placement(sub, ["C2", "D3"]), False)

        self.assertEqual(board.is_valid_placement(cruiser, ["A1", "A2", "A3"]), True)
        self.assertEqual(board.is_valid_placement(sub, ["B2", "C2"]), True)

    def test_placing_ships(self):
        board = Board()
        cruiser = Ship("Cruiser", 3)

        board.place(cruiser, ["A1", "A2", "A3"])
        cell_1 = board.cells["A1"]
        cell_2 = board.cells["A2"]
        cell_3 = board.cells["A3"]

        self.assertEqual(cell_1.ship, cruiser)
        self.assertEqual(cell_2.ship, cruiser)
        self.assertEqual(cell_3.ship, cruiser)

        self.assertEqual(cell_1.ship, cell_2.ship)

    def test_overlapping_ships(self):
        board = Board()
        cruiser = Ship("Cruiser", 3)
        sub = Ship("Submarine", 2)

        board.place(cruiser, ["A1", "A2", "A3"])
        self.assertEqual(board.is_valid_placement(sub, ["A1", "B1"]), False)

    def test_rendering_board(self):
        board = Board()
        cruiser = Ship("Cruiser", 3)

        board.place(cruiser, ["A1", "A2", "A3"])
        self.assertEqual(board.render(), "  1 2 3 4 \nA . . . . \nB . . . . \nC . . . . \nD . . . . \n")
        self.assertEqual(board.render(True), "  1 2 3 4 \nA S S S . \nB . . . . \nC . . . . \nD . . . . \n")
