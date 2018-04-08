class Circle(object):
  def __init__(self):
    self.type = "circle"
  
  def print_type(self):
    print(self.type)


class Square(object):
  def __init__(self):
    self.type = "square"
    
  def print_type(self):
    print(self.type)


class ShapeFactory(object):
  def make_type(self, type):
    obj = None
    if type == "circle":
      obj = Circle()
    elif type == "square":
      obj = Square()
    return obj


def client():
  factory = ShapeFactory()
  circle_obj = factory.make_type("circle")
  circle_obj.print_type()
  
  square_obj = factory.make_type("square")
  square_obj.print_type()
  
client()
