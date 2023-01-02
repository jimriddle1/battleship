class Cell:
  def __init__(self, coordinate):
    self.coordinate = coordinate
    self.empty = True
    self.ship = None
  #
  # def hit(self):
  #   self.health = self.health - 1
  #   if self.health == 0:
  #      self.sunk = True
