def square(n):
    for i in range(n):
        for j in range(n):
            if(i == 0) or (j == 0) or (j == n-1) or (i == n-1):
                print("_", end=" ")
            else:
                print("*", end=" ")
        print()

k = int(input())
square(k)