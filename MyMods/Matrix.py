"""" Matrix Class = for use with matrixes or grids.
use dimj -> dimensions rows
    dimi -> dimensions columns """


class Matrix:
  """
     Matrix class. makes a matrix with dimi colums and dimj rows
  """
  def __init__(self, dimj, dimi):
    self.dimj = dimj
    self.dimi = dimi
    self.grid = [[0 for i in range(dimi)] for j in range(dimj)]
    self.lowpoints = []
    self.risklevel = 0

  def __str__(self):
    """
       Returns a string representation of the matrix
    """
    t = ""
    for j in range(self.dimj):
      for i in range(self.dimi):
        t += str(self.grid[j][i])
      t += "\n"
    return t