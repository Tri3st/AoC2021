def part1():
  data_l = []
  with open("Day3.txt","r") as data_file:
    for line in data_file:
      data_l.append(line.strip())

  print(data_l)

  # data = """00100
  # 11110
  # 10110
  # 10111
  # 10101
  # 01111
  # 00111
  # 11100
  # 10000
  # 11001
  # 00010
  # 01010"""

  # data_list = data.split("\n")
  # data_l = [x.lstrip() for x in data_list]
  data_l2 = data_l


  def get_ones(position):
    count = 0
    for item in data_l:
      if int(item[position]) == 1:
        count += 1
    return count
  
  def get_zeroes(position):
    count = 0
    for item in data_l:
      if int(item[position]) == 0:
        count += 1
    return count

  def add_nums(bin, position):
    tresult = []
    for item in data_l:
      if int(item[position]) == bin:
        tresult.append(item)
    return tresult
  
  
  x_pos = 0
  result = []
  # oxygen genarator rating
  while len(data_l) > 1:
    if get_ones(x_pos) >= len(data_l)/2:
      result.extend(add_nums(1,x_pos))
    else:
      result.extend(add_nums(0,x_pos))
    data_l = list(result)
    result = []
    x_pos += 1

  print("The result of the Oxygen Generator Rating is %d .." % int(data_l[0],2))
  oxygenrat = int(data_l[0],2)

  result = []
  x_pos = 0
  data_l = data_l2
  while len(data_l) > 1:
    if get_zeroes(x_pos) <= len(data_l)/2:
      result.extend(add_nums(0,x_pos))
    else:
      result.extend(add_nums(1,x_pos))
    data_l = list(result)
    result = []
    x_pos += 1

  print("The result of the CO2 Scrubber Rating is %d .." % int(data_l[0],2))
  co2scrubrat = int(data_l[0],2)

  print("OxyGenRat = %d\nCO2ScrubRat = %d\nProduct = %d" % (oxygenrat, co2scrubrat, oxygenrat * co2scrubrat))