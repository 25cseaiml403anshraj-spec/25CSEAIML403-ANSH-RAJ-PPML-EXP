def merge_dict(d1 , d2):
    d1.update(d2)
    return d1

dict1 = eval(input("Enter First Element"))
dict2 = eval(input("Enter Second Element"))

result = merge_dict(dict1 , dict2)

print("Merged Dictonaries:", result)