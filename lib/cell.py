class Cell:
  def __init__(self, coordinate):
    self.coordinate = coordinate
    self.is_empty = True
    self.ship = None
    self.fired_upon = False
    self.render = "."

  def place_ship(self, input_ship):
    self.ship = input_ship
    self.is_empty = False
    self.render = "S"

  def fire_upon(self):
    if self.is_empty == True:
       self.render = "M"
    if self.is_empty == False:
       self.ship.hit()
       self.fired_upon = True
       self.render = "H"
       if self.ship.health <= 0:
          self.render = "X"
