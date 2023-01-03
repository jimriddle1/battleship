import sys
# import dict

from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board
from lib.game import Game
import unittest

class GameTest(unittest.TestCase):

    def test_instantiate(self):
        board_1 = Board()
        game = Game(board_1)
        self.assertEqual(game.board, board_1)
