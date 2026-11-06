
a = [10, 20, 30, 40, 50]

x = int(input("Enter a value to search: "))

result = list(filter(lambda n: n == x, a))

if result:
    print("Value is present in the list")
else:
    print("Value is not present in the list")
