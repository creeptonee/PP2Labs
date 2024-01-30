#ex1
class String:
  def __init__(myString, name):
    myString.name = name

  def getString(abc):
    abc.name = input()
  def printString(upper):
      print(upper.name.upper())


#ex2

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    

#ex3

class Rectangle(Person):
    def __init__(self, length, width):
        super.__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
