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
    if self.is_empty == True:
       self.fired_upon = True
    if self.is_empty == False:
       self.ship.hit()
       self.fired_upon = True

  def render(self, input_boolean = False):
    if input_boolean and (self.is_empty == False):
      return "S"
    elif self.is_empty and self.fired_upon:
      return "M"
    elif (self.is_empty == False) and self.fired_upon:
      if self.ship.health <= 0:
        return "X"
      return "H"
    else:
      return "."
