from lib.cell import Cell
from lib.ship import Ship
from lib.board import Board
import math
import random

class Game:
  def __init__(self):
    self.player_board = Board()
    self.computer_board = Board()

  def start_game(self):
    print ("Welcome to BATTLESHIP\nEnter p to play. Enter q to quit.")
    input_1 = input()
    if input_1 == "q":
      print("Thanks for Playing!")
      return True
    elif input_1 == "p":
      self.setup_game()
      # self.take_turn()
    else:
      print("Please Enter a Valid Character\n\n")
      self.start_game()

  def setup_game(self):
    print("I (the computer) will now place my two boats on my side of the board\n\n")
    self.place_computer_boats()

    self.place_player_cruiser()
    self.place_player_sub()

  def place_player_cruiser(self):
    print("Now tell me where you want to place the Cruiser (3 Coordinates)")
    cruiser_coordinates = input().split()
    ship = Ship("Cruiser", 3)

    if self.player_board.is_valid_placement(ship, cruiser_coordinates) == True:
      self.player_board.place(ship, cruiser_coordinates)
    else:
      print("Please enter valid Coordinates\n")
      self.place_player_cruiser()

  def place_player_sub(self):
    print("Now tell me where you want to place the Sub (2 Coordinates)")
    cruiser_coordinates = input().split()
    ship = Ship("Sub", 2)

    if self.player_board.is_valid_placement(ship, cruiser_coordinates) == True:
      self.player_board.place(ship, cruiser_coordinates)
    else:
      print("Please enter valid Coordinates\n")
      self.place_player_sub()


  def place_computer_boats(self):
    coordinate_list = []
    cruiser_cord = random.choice(list(self.computer_board.cells))
    computer_cruiser = Ship("Cruiser", 3)
    self.increment_and_place(computer_cruiser, cruiser_cord)
    computer_sub = Ship("Sub", 2)
    self.increment_and_place(computer_sub, cruiser_cord)

  def increment_and_place(self, ship, start_cord):
    output_list = []
    coin_flip = random.randint(0,1)

    if coin_flip == 0:
      output_list.append(start_cord)
      for i in range(1, ship.length):
        next_cord = list(start_cord)
        next_cord[1] = str(int(start_cord[1]) + 1)
        next_cord = ''.join(next_cord)
        output_list.append(next_cord)
        start_cord = next_cord
    else:
      output_list.append(start_cord)
      for i in range(1, ship.length):
        next_cord = list(start_cord)
        next_cord[0] = chr(ord(start_cord[0]) + 1)
        next_cord = ''.join(next_cord)
        output_list.append(next_cord)
        start_cord = next_cord

    if self.computer_board.is_valid_placement(ship, output_list) == True:
      self.computer_board.place(ship, output_list)
      return output_list
    else:
      self.increment_and_place(ship, random.choice(list(self.computer_board.cells)))
