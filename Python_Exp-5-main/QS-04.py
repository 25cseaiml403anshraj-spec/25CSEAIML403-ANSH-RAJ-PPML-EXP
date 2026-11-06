s = set()

n = int(input("Enter number of elements: "))

for i in range(n):
    x = input("Enter element: ")
    s.add(x)

new_s = set()

for i in s:
    new_s.add(i)

print("Original set:", s)
print("New set:", new_s) 