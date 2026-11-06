a = input("Enter the characters: ")

a = "".join(dict.fromkeys(a))

upper = "".join(map(str.upper, a))

lower = "".join(map(str.lower, a))

print("After removing duplicates:", a)
print("Uppercase:", upper)
print("Lowercase:", lower)