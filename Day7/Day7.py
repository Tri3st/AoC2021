import sys

fuel = {}
crabbies = []

with open("Day7/Day7.txt", "r") as  crabs_file:
  for line in crabs_file:
      cc = line
  cc = cc.split(",")
  crabbies = [int(x) for x in cc]


def part1():
  
  crabs = [16,1,2,0,4,2,7,1,2,14]

  for i in crabbies:
    if i not in fuel.keys():
      sum = 0
      for x in crabbies:
        q = abs(x - i)
        sum += q
      t1 = { i : sum }
      print(t1)
    
      fuel.update(t1)

  min = sys.maxsize
  min_index = -1
  for k,v in fuel.items():
    if v < min:
      min = v
      min_index = k
  print("k : %d \nv : %d" % (min_index, min))


def part2():
  crabs = [16,1,2,0,4,2,7,1,2,14]

  min = sys.maxsize
  min_index = -1
  
  for cr in range(max(crabbies)+1):
    if cr not in fuel.keys():
      sum = 0
      for x in crabbies:
        dist = abs(x - cr)
        q1 = (dist**2 + dist)//2
        print(q1)
        sum += q1
      t1 = { cr : sum }
      if sum < min:
        min = sum
        min_index = cr
      
      print(t1)
      fuel.update(t1)
    
  print("k : %d\nv : %d" % (min_index, min))
