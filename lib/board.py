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
    'B1' : Cell('B1'),
    'B2' : Cell('B2'),
    'B3' : Cell('B3'),
    'B4' : Cell('B4'),
    'C1' : Cell('C1'),
    'C2' : Cell('C2'),
    'C3' : Cell('C3'),
    'C4' : Cell('C4'),
    'D1' : Cell('D1'),
    'D2' : Cell('D2'),
    'D3' : Cell('D3'),
    'D4' : Cell('D4'),
    }
    return board

  def is_valid_coordinate(self, input_string):
      return input_string in self.cells

  def is_valid_placement(self, ship, input_list):
      if ship.length != len(input_list):
         return False
      elif self.check_consecutive_list(ship, input_list) == False:
         return False
      else:
         return True

  def check_consecutive_list(self, ship, input_list):
      horiz_input = []
      vert_input = []

      vert_boolean = False
      horiz_boolean = False

      for i in input_list:
          horiz_input.append(ord(i[0]))
          vert_input.append(int(i[1]))
      horiz_check = list(range(horiz_input[0], ship.length + horiz_input[0]))
      vert_check = list(range(vert_input[0], ship.length + vert_input[0]))

      if vert_check == vert_input:
        vert_boolean = True
      if horiz_check == horiz_input:
        horiz_boolean = True

      if (int(vert_boolean) + int(horiz_boolean)) == 1:
        return True
      else:
        return False
