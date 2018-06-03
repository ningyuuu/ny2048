import random
from state import State

class Model:
  def __init__(self):
    self.state = State()
    self.populate()
    self.populate()

  def populate(self):
    value = 2 if random.uniform(0, 1) < 0.9 else 4
    row, col = self.state.get_random_empty_cell()
    if (row != None) & (col != None):
      self.state.fill(row, col, value)

  def play(self, dir):
    # [0, 1, 2, 3] = [up, down, left, right]
    reversals = self.get_reversals(dir)
    traversals = self.get_traversals(reversals)

    for row in traversals[0]:
      for col in traversals[1]:
        if self.state.is_filled(row, col):
          self.state.move(row, col, dir)
          # print((row, col))


  def get_reversals(self, dir):
    # code adapted from gabrielecirulli/2048
    # we do reversals because when we search for movements
    # we always search from the "last" piece in each direction
    # -> A B C D search D, C, B, A
    reversals = [
      [False, False],
      [True, False],
      [False, False],
      [False, True]
    ]
    return reversals[dir]

  def get_traversals(self, reversals):
    row = [0, 1, 2, 3]
    col = [0, 1, 2, 3]

    # hence, for down and right, we need reversals 
    # on row and col respectively
    if (reversals[0]):
      row = row[::-1]
    if (reversals[1]):
      col = col[::-1]

    return (row, col)


def printr(state):
  [print(r) for r in state]

# x = Model()
# printr(x.state.state)
# x.play(1)
# printr(x.state.state)

x = Model()
printr(x.state.state)
x.play(2)
printr(x.state.state)
x.play(3)
printr(x.state.state)