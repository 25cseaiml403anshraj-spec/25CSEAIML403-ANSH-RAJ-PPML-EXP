def operations(a, b):
    print("Union =", a.union(b))
    print("Intersection =", a.intersection(b))
    print("A - B =", a.difference(b))
    print("B - A =", b.difference(a))
    print("Symmetric Difference =", a.symmetric_difference(b))


a = eval(input("Enter first set: "))
b = eval(input("Enter second set: "))

operations(a, b)