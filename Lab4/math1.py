#ex1
import math
deg = float(input("Input degree: "))
rad = math.radians(deg)
print(rad)

#ex2
a = float(input("Height: "))
base1 = float(input("Base 1"))
base2 = float(input("Base 2"))
area = 0.5 * (base1 + base2) * a
print("Expected Output:", area)

#ex3
import math

num_sides = int(input())
side_length = float(input())
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("Area", area)

#ex4
l = float(input("Length of base: "))
h = float(input("Height: "))
A = l * h
print("Area is: ", A)
