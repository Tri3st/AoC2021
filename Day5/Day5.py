import re
from Day5.Field import Field
from Day5.Line import Line

data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

def part1():
  f1 = Field(10)

  pattern = re.compile(r"(\d+),(\d+)\s+->\s+(\d+),(\d+)")
  xdata = re.findall(pattern, data)

  for d in xdata:
    f1.add_line(Line(d[0], d[1], d[2], d[3]).get_coords())

  # print(f1)
  # print("2 or more : %d" % f1.return_2_or_more())




def part2():
  data = []
  field = Field(1000)

  pattern = re.compile(r"(\d+),(\d+)\s+->\s+(\d+),(\d+)")
  

  with open("Day5/Day5.txt","r") as dfile:
    for line in dfile:
      data.append(line)
      
  for x in data:
    xdata = re.findall(pattern, x)
    xd = xdata[0]
    field.add_line(Line(xd[0], xd[1], xd[2], xd[3]).get_coords())
  print(field.return_2_or_more())