"""Bingo Card Class"""

class BingoCard:
  def __init__(self):
    self.card = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    self.win = False

  def add_row(self, row_nr, row):
    for i in range(5):
      self.card[row_nr][i] = int(row[i])

  def bingo(self):
    return self.win
  
  def check_win(self):
    hor_win = False
    vert_win = False
    for i in range(5):
      if self.count_X_hor(i) == 5:
        hor_win = True
      if self.count_X_vert(i) == 5:
        vert_win = True
    if hor_win or vert_win:
      self.win = True
   
  def count_X_hor(self, row):
    count = 0
    for i in range(5):
      if self.card[row][i] == 'X':
        count += 1
    return count

  def count_X_vert(self, col):
    count = 0
    for i in range(5):
      if self.card[i][col] == 'X':
        count += 1
    return count

  def add_card(self, card):
    for index, row in enumerate(card):
      self.add_row(index,row)

  def mark_number(self, num):
    for index, row in enumerate(self.card):
      for index2, item in enumerate(row):
        if item == int(num):
          self.card[index][index2] = 'X'
    self.check_win()

  def calc_score(self):
    sum = 0
    if self.win:
      for row in self.card:
        for x in row:
          if x != 'X':
            sum += int(x)
      return sum
    else:
      return -1

  def __str__(self):
    temp_str = ""
    for item in self.card:
      temp_str += "%02s %02s %02s %02s %02s%s" % (item[0], item[1], item[2], item[3], item[4], "\n")
    return temp_str