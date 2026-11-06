a = []

print("Enter 9 elements:")

for i in range(3):
    row = []
    for j in range(3):
        x = int(input())
        row.append(x)
    a.append(row)

print("\nMatrix:")

for i in range(3):
    print(a[i])

print("\nSum of each row:")

for i in range(3):
    sum = 0
    for j in range(3):
        sum = sum + a[i][j]
    print("Row", i + 1, "=", sum)

print("\nSum of each column:")

for j in range(3):
    sum = 0
    for i in range(3):
        sum = sum + a[i][j]
    print("Column", j + 1, "=", sum)