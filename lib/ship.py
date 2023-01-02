class Ship:
  def __init__(self, name, length):
    self.name = name
    self.length = length
    self.health = length
    self.sunk = False

cruiser = Ship("Cruiser", 3)

print(cruiser.name)
print(cruiser.sunk)

# breakpoint()

cruiser.sunk = True

print(cruiser.sunk)
