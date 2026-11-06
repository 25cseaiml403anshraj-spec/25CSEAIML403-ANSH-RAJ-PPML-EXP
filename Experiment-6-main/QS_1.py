a = []

print("Enter 9 elements:")

for i in range(3):
    row = []
    for j in range(3):
        x = int(input())
        row.append(x)
    a.append(row)

b = []

for x in range(1, 10):
    for i in range(3):
        for j in range(3):
            if a[i][j] == x:
                b.append(x)

print("Original Matrix:")

for i in range(3):
    print(a[i])

print("Grouped Matrix:")

for i in range(0, 9, 3):
    print(b[i:i+3])