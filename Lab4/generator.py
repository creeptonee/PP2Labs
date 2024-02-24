#ex1
def generator(N):
    for i in range(1, N + 1):
        yield i ** 2


N = int(input())

squares = generator(N)
print(N, ":")
for k in squares:
    print(k)


#ex2
def even_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

N = int(input())

even_numbers = even_generator(N)

print(N, ":", end=" ")
for num in even_numbers:
    print(num, end="")
    if num != N and num != N - 1 and num % 2 == 0:
        print(",", end=" ")
print()

#ex3
def cmon(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())

print(n, ":")
for num in cmon(n):
    print(num)

#ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

print("from", a, "to", b, ":")
for square in squares(a, b):
    print(square)

#ex5
def count(n):
    while n >= 0:
       yield n
       n -= 1

n = int(input())

print("from", n, "to 0:")
for num in count(n):
    print(num)


