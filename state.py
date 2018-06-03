import random

class State:
  def __init__(self):
    self.state = [
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]
    ]
    self.lost = False

  def get_empty_cells(self):
    cells = []

    for row in [0, 1, 2, 3]:
      for col in [0, 1, 2, 3]:
        if self.state[row][col] == 0:
          cells.append((row, col))

    return cells

  def get_random_empty_cell(self):
    cells = self.get_empty_cells()

    if len(cells) == 0:
      self.lost = True
      return (None, None)

    return random.choice(cells)

  def fill(self, row, col, value):
    self.state[row][col] = value

  def is_filled(self, row, col):
    return self.state[row][col] != 0

  def move(self, row, col, dir):
    # dir: [0, 1, 2, 3] = [up, down, left, right]
    move_col = 0
    move_row = 0
    if (dir == 0):
      move_row = 1
    elif (dir == 1):
      move_row = -1
    elif (dir == 2):
      move_col = -1
    elif (dir == 3):
      move_col = 1

    new_row = row
    new_col = col

    while ((new_col + move_col >= 0) and
           (new_col + move_col <= 3) and
           (new_row + move_row >= 0) and
           (new_row + move_row <= 3) and
           (self.state[new_row + move_row][new_col + move_col] == 0)):
      new_col += move_col
      new_row += move_row

    if ((new_col + move_col >= 0) and
        (new_col + move_col <= 3) and
        (new_row + move_row >= 0) and 
        (new_row + move_row <= 3) and
        (self.state[new_row + move_row][new_col + move_col] == self.state[row][col])):
      self.state[new_row + move_row][new_col + move_col] *= 2
    else:
      self.state[new_row][new_col] = self.state[row][col]
    
    if (new_row != row) | (new_col != col):
      self.state[row][col] = 0
