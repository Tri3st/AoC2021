"""Class Segment"""

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdgf",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
  }
lengths = {
    2: 1, 
    3: 7, 
    4: 4, 
    5: [ 2, 3, 5, 6 ],
    6: [ 0, 6, 9 ],
    7: 8,
  }

class Segment:
  
  def __init__(self, input):
    self.all = "abcdefg"
    self.seg = [".aaaa.",
                "b....c",
                "b....c",
                ".dddd.",
                "e....f",
                "e....f",
                ".gggg."]
    self.input = input
    for i in self.input:
      self.all = self.all.replace(i, "")    
    new_seg = []
    for s in self.seg:
      for c in self.all:
        s = s.replace(c, ".")
      new_seg.append(s)
    self.seg = new_seg

  def __str__(self):
    st = ""
    for s in self.seg:
      st += s + "\n"
    return st
    
  def calculate(self, input: list):
    x = { "a": "", "b": "", "c": "",
          "d": "", "e": "", "f": "", 
         "g": "", "cf": "", "bd": ""}
    input2 = input[0].split(" ")
    for i1 in input2:
      if len(i1) == 2:
        x["cf"] = i1
      if len(i1) == 3:
        x_acf = i1
        x["a"] = x_acf.replace(x["cf"], "")
      if len(i1) == 4:
          x_bcdf = i1
          x["bd"] = x_bcdf.replace(x["cf"], "")


    print(x)
      
    