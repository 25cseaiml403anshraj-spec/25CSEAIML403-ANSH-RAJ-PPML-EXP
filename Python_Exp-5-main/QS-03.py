d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Original dictionary:", d)

new_d = {}

for key in d:
    if d[key] not in new_d.values():
        new_d[key] = d[key]

print("Dictionary after removing duplicate values:", new_d)