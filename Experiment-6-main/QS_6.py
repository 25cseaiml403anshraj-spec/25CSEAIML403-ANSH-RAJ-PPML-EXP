a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

c = list(filter(lambda x: x in b, a))

print("First array:", a)
print("Second array:", b)
print("Intersection:", c)