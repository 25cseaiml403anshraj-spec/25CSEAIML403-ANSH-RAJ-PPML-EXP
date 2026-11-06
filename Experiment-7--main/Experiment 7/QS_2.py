a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

result = list(map(lambda x, y, z: x + y + z, a, b, c))

print("First List:", a)
print("Second List:", b)
print("Third List:", c)
print("Sum List:", result)