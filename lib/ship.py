class Ship:
  def __init__(self, name, length):
    self.name = name
    self.length = length
    self.health = length
    self.sunk = False

  def hit(self):
    self.health = self.health - 1
    if self.health == 0:
       self.sunk = True
