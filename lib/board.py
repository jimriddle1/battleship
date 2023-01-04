from lib.cell import Cell
from lib.ship import Ship
import math

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

  def place(self, input_ship, location_list):
      for i in location_list:
          self.cells[i].place_ship(input_ship)

  def is_valid_coordinate(self, input_string):
      return input_string in self.cells

  def is_valid_placement(self, ship, input_list):
      # breakpoint()
      for i in input_list:
         if self.is_valid_coordinate(i) == False:
             return False
      if ship.length != len(input_list):
         return False
      elif self.check_consecutive_list(ship, input_list) == False:
         return False
      elif self.check_overlapping(input_list) == False:
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

  def check_overlapping(self, input_list):
      for i in input_list:
          if self.cells[i].is_empty == False:
              return False

      return True

  def render(self, input_boolean = False):
      output_string = "  1 2 3 4 \nA q r s t \nB v w x y \nC z . . . \nD . . . . \n"
      listed_string = list(output_string)
      listed_string[13] = self.cells["A1"].render(input_boolean)
      listed_string[15] = self.cells["A2"].render(input_boolean)
      listed_string[17] = self.cells["A3"].render(input_boolean)
      listed_string[19] = self.cells["A4"].render(input_boolean)
      listed_string[24] = self.cells["B1"].render(input_boolean)
      listed_string[26] = self.cells["B2"].render(input_boolean)
      listed_string[28] = self.cells["B3"].render(input_boolean)
      listed_string[30] = self.cells["B4"].render(input_boolean)
      listed_string[35] = self.cells["C1"].render(input_boolean)
      listed_string[37] = self.cells["C2"].render(input_boolean)
      listed_string[39] = self.cells["C3"].render(input_boolean)
      listed_string[41] = self.cells["C4"].render(input_boolean)
      listed_string[46] = self.cells["D1"].render(input_boolean)
      listed_string[48] = self.cells["D2"].render(input_boolean)
      listed_string[50] = self.cells["D3"].render(input_boolean)
      listed_string[52] = self.cells["D4"].render(input_boolean)
      return "".join(listed_string)
