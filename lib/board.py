from lib.cell import Cell
from lib.ship import Ship

class Board:
  def __init__(self):
    self.cells = self.generate_board()


  def generate_board(self):
    board = {
    'A1' : Cell('A1'),
    'A2' : Cell('A2'),
    'A3' : Cell('A3'),
    'A4' : Cell('A4'),
    'B1' : Cell('A1'),
    'B2' : Cell('A2'),
    'B3' : Cell('A3'),
    'B4' : Cell('A4'),
    'C1' : Cell('A1'),
    'C2' : Cell('A2'),
    'C3' : Cell('A3'),
    'C4' : Cell('A4'),
    'D1' : Cell('A1'),
    'D2' : Cell('A2'),
    'D3' : Cell('A3'),
    'D4' : Cell('A4'),
    }
    return board
