def max_unique(d):
    max_value = -1
    max_key = None

    for key, value in d.items():
        if list(d.values()).count(value) == 1:
            if value > max_value:
                max_value = value 
                max_key = key

    return max_key

d = eval(input("Enter a Element:"))

print("Key having maximam unique value:", max_unique(d))