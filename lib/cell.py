class Cell:
  def __init__(self, coordinate):
    self.coordinate = coordinate
    self.is_empty = True
    self.ship = None

  def place_ship(self, input_ship):
    self.ship = input_ship
    self.is_empty = False
