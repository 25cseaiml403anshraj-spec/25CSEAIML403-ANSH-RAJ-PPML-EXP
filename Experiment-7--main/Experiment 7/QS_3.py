a = [2, 3, 4, 5]

index = range(len(a))

result = list(map(lambda x, i: x ** i, a, index))

print("Original List:", a)
print(" List:", result) 