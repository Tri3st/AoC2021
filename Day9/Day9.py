from Day9.Grid import Grid

data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

file_data = ""
with open("Day9/Day9.txt", "r") as dfile:
  for line in dfile:
    file_data += line

def part1():
  grid = Grid(100, 100)
  grid.add_data(file_data)
  print(grid)
  print(grid.nr_of_lowpoints)
  print(grid.risklevel)