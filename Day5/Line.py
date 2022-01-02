class Line:

  def __init__(self, x1, y1, x2, y2):
    """
    Draw a line from x1, y1 to x2, y2
    """
    self.x1 = int(x1)
    self.x2 = int(x2)
    self.y1 = int(y1)
    self.y2 = int(y2)
    self.line = []
    self.draw_line()

  def draw_line(self):
    x_d = 0
    y_d = 0
    x_f = 0
    y_f = 0
    if self.y1 < self.y2:
      y_f = 1
    elif self.y1 > self.y2:
      y_f = -1
    else:
      x_d = abs(self.x2 - self.x1) + 1  
      y_f = 0
    if self.x1 < self.x2:
      x_d = abs(self.x2 - self.x1) + 1
      x_f = 1
    elif self.x1 > self.x2:
      x_d = abs(self.x2 - self.x1) + 1
      x_f = -1
    else:
      x_d = abs(self.y2 - self.y1) + 1
      x_f = 0

    for i in range(x_d):
      pointx = self.x1 + i * x_f
      pointy = self.y1 + i * y_f

      point = (pointx, pointy)
      self.line.append(point)

  def get_coords(self):
    return self.line

  def __str__(self):
    return "(%s,%s) -> (%s,%s)" % (self.x1, self.y1, self.x2, self.y2)

