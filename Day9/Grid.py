from MyMods.Matrix import Matrix
"""Class Grid"""

class Grid(Matrix):
  """
     initialize the grid. inherited from matrix class. dimi = colums, dimj = rows
  """
  def __init__(self, dimj, dimi):
    super().__init__(dimj, dimi)
    self.lowpoints = []
    self.nr_of_lowpoints = 0
    self.risklevel = 0
    

  def add_data(self, data):
    lines = data.split("\n")
    for j in range(self.dimj):
      for i in range(self.dimi):
        self.grid[j][i] = int(lines[j][i])
    self.find_lowpoints()


  def find_lowpoints(self):
    for j in range(self.dimj):
      for i in range(self.dimi):
        if self.is_lowpoint(self.grid[j][i], j, i):
          self.lowpoints.append((j, i))
          self.nr_of_lowpoints = len(self.lowpoints)
          self.risklevel += self.grid[j][i] + 1

  def is_lowpoint(self,x, j, i):
      if j != self.dimj - 1 and self.grid[j + 1][i] <= x:
        return False
      if i != self.dimi - 1 and self.grid[j][i + 1] <= x:
        return False
      if j != 0 and self.grid[j - 1][i] <= x:
        return False
      if i != 0 and self.grid[j][i - 1] <= x:
        return False
      else: 
        return True
  
  def __str__(self):
    return super().__str__()
