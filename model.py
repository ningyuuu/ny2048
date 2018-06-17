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
    change = False
    reversals = self.get_reversals(dir)
    traversals = self.get_traversals(reversals)

    # TODO: ensure that doubling does not happen twice in a
    # single cell, i.e. 2 2 4 0 going left should be 4 4 0 0
    # and not 8 0 0 0

    merges = []

    for row in traversals[0]:
      for col in traversals[1]:
        if self.state.is_filled(row, col):
          new_change = self.state.move(row, col, dir, merges)
          change = change or new_change
          # print((row, col))
    return change

  def make_move(self, dir):
    if self.play(dir):
      self.spawn_random()

  def spawn_random(self):
    row, col = self.state.get_random_empty_cell()
    num = 2 if random.random() < 0.9 else 4
    self.state.fill(row, col, num)

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

    # print(row)
    # print(col)

    return (row, col)


def print_state(x):
  [print(r) for r in x.state.state]
  print()

# x = Model()
# printr(x.state.state)
# x.play(1)
# printr(x.state.state)

x = Model()
print("Make a move: 0: up | 1: down | 2: left | 3: right")
print_state(x)

while (True):
  move = int(input())
  x.make_move(move)
  print_state(x)