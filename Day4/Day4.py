from Day4.Day4_bingo import BingoCard


# data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
# 8  2 23  4 24
# 21  9 14 16  7
# 6 10  3 18  5
# 1 12 20 15 19

# 3 15  0  2 22
# 9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
# 2  0 12  3  7"""

# data = data.split("\n")
data = []

with open("Day4/Day4.txt","r") as data_file:
  for line in data_file:
    data.append(line.strip())

bingo_sequence = data[0].split(",")


def part1():
  """
  part 1 of the Bingo numbers problem. Day 4 of Advent of Code
  """
  cards = []

  for i in range(99):
    card = BingoCard()
    for j in range(5):
      row = data[2 + j + (i * 6)].strip().split(" ")
      row2 = [int(x) for x in row if x != '']
      card.add_row(j, row2)
    cards.append(card)


  BINGO = False
  index2 = 0

  
  while True:
    num1 = bingo_sequence[index2]
    for i in range(99):
      cards[i].mark_number(num1)
      if cards[i].bingo():
        BINGO = True
        print("BINGO ON CARD %d in round %d !!" % (i, index2))
        print("Card score is %d" % cards[i].calc_score())
        print("Winning number was %s" % bingo_sequence[index2])
        print("So the ASNWER is %d" % (int(bingo_sequence[index2]) * cards[i].calc_score()))
        print(cards[i])
      
    index2 += 1
    if BINGO or index2 >= len(bingo_sequence):
      break


def part2():
  """
  part 2 of the Bingo numbers problem. Day 4 of Advent of Code
  """
  win_list = [0 for _ in range(99)]
  cards2 = []
  LAST_BINGO = False

  for i in range(99):
    card = BingoCard()
    for j in range(5):
      row = data[2 + j + (i * 6)].strip().split(" ")
      row2 = [int(x) for x in row if x != '']
      card.add_row(j, row2)
    cards2.append(card)
  
  index = 0
  while True:
      num1 = bingo_sequence[index]
      for i in range(99):
        cards2[i].mark_number(num1)
        if cards2[i].bingo():
          win_list[i] = 1
          if win_list.count(0) == 0:
            LAST_BINGO = True
            print("LAST BINGO ON CARD %d in round %d !!" % (i, index))
            print("Card score is %d" % cards2[i].calc_score())
            print("Winning number was %s" % bingo_sequence[index])
            print("So the ASNWER is %d" % (int(bingo_sequence[index]) * cards2[i].calc_score()))
        
      index += 1
      if LAST_BINGO or index >= len(win_list):
        break

  
