import sys
# import dict

from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board
from lib.game import Game
import unittest

class GameTest(unittest.TestCase):

    def test_instantiate(self):
        game = Game()
        self.assertEqual(type(game.player_board), type(Board()))
        self.assertEqual(type(game.computer_board), type(Board()))

    # def test_start_game(self):
    #     game = Game()
    #     game.start_game()

    def test_place_computer_boats(self):
        game = Game()
        game.place_computer_boats()
        self.assertEqual(game.computer_board.render(True).count('S'), 5)
