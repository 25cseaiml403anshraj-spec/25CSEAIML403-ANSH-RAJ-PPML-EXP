n = int(input("Enter the order of matrix: "))

a = []

print("Enter the elements:")

for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    a.append(row)

print("Original Matrix:")

for i in range(n):
    print(a[i])

print("Transpose Matrix:")

for j in range(n):
    for i in range(n):
        print(a[i][j], end=" ")
    print()
