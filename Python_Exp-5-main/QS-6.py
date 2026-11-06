def combine_set(a, b):
    c = a.union(b)
    return c


a = eval(input("Enter first set: "))
b = eval(input("Enter second set: "))

c = combine_set(a, b)

print("New set =", c)