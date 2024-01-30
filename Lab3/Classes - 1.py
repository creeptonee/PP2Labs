#ex1 get_string
class String:
  def __init__(self):
    self.name = ""

  def getString(self):
    self.name = input()
  def printString(self):
      print(self.name.upper())

name = String()
name.getString()
name.printString()


#ex2 Area

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self):
        k = int(input())
        Shape.__init__(self)
        self.length = k
    def area(self):
        return self.length * self.length
    
Variable = Square()
print(Variable.area())

#ex3 Rectangle's area

class Rectangle():
    def __init__(self, length, width):
        length = int(input())
        width = int(input())
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

Variable = Rectangle()
print(Variable.area())


#ex4 Point class
from ipaddress import summarize_address_range
from math import *
from math import sqrt
class Point:
    def __init__(self):
        x = int(input())
        y = int(input())
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self):
        new_x = self.x + self.x
        new_y = self.y + self.y
        self.x = new_x
        self.y = new_y

    def dist(self):
        other_x = int(input())
        other_y = int(input())
        self.other_x = other_x
        self.other_y = other_y
        distance = sqrt((self.x - other_x)**2 + (self.y - other_y)**2)
        return distance
variable = Point()
variable.show()
print(variable.move())
variable.dist()


#ex5 Bank account

class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self):
        deposit = int(input())
        self.balance += deposit
        print("The deposit in the amount of:", deposit," ", "added to balance" )
        print("The new balance = ", self.balance)

    def withdraw(self):
        newsum = int(input())
        if newsum <= self.balance:
            self.balance = self.balance - newsum
        else:
            print("The transaction can not be proceed, your sum is more than balance")

k = Account(owner = "Nurtas")
k.deposit()
k.withdraw()


#ex6 Prime numbers filter
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = list(map(int, input().split()))
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)



