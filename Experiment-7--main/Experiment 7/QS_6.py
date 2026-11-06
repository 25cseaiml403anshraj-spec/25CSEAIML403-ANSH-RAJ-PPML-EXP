a = list(map(int, input("Enter the numbers: ").split()))

positive = sum(map(lambda x: x > 0, a))
negative = sum(map(lambda x: x < 0, a))
zero = sum(map(lambda x: x == 0, a))

total = len(a)

print("Ratio of positive numbers:", positive / total)
print("Ratio of negative numbers:", negative / total)
print("Ratio of zeroes:", zero / total)