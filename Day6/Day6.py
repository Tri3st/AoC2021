

def part1():
  
  fishies = [3, 4, 3, 1, 2]
  ffishies = []
  ff2 = []
  
  with open("Day6/Day6.txt", "r") as fishies_file:
    for line in fishies_file:
      ffishies = line
  ffishies = ffishies.split(",")
  ff2 = [int(x) for x in ffishies]
  
  def next_day(fishies):
    new_fishies = []
    extra = 0
    for x in fishies:
      if x == 0:
        extra += 1
        new_fishies.append(6)
      else:
        new_fishies.append(x-1)
    for _ in range(extra):
      new_fishies.append(8)
    return new_fishies

  for i in range(256):
    ff2 = next_day(ff2)
    print("day %d .." % i)
  print(len(ff2))
  
