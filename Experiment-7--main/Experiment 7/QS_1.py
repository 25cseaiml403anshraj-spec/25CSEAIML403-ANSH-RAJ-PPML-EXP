a = list(map(int, input("Enter the numbers: ").split()))

b = list(map(lambda x: x * 3, a))

print("Original List:", a)
print("Tripled List:", b)