"""Field Class"""

class Field:

  def __init__(self, dim: int):
    self.dimension = dim
    self.field = [[ 0 for x in range(self.dimension)] for y in range(self.dimension)]

  def add_line(self, line):
    for point in line:
      self.field[point[0]][point[1]] += 1

  def return_2_or_more(self):
    count = 0
    for i in range(self.dimension):
      for j in range(self.dimension):
        if self.field[j][i] >= 2:
          count += 1
    return count

  def __str__(self):
    st = ""
    for y in range(self.dimension):
      for x in range(self.dimension):
        st += "%d" % self.field[x][y]
      st += "\n"
    return st