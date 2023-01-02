class Cell:
  def __init__(self, coordinate):
    self.coordinate = coordinate
    self.is_empty = True
    self.ship = None
    self.fired_upon = False

  def place_ship(self, input_ship):
    self.ship = input_ship
    self.is_empty = False

  def fire_upon(self):
    if self.is_empty == False:
       self.ship.hit()
       self.fired_upon = True
