
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")

    next = lambda x, y: x + y
    c = next(a, b)

    a = b
    b = c
