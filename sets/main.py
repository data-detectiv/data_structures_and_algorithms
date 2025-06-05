# numbers = [1,1,2,3,4]
# first = set(numbers)
# second = {1,5}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# dinner_table = utensils | dishes
dinner_table = utensils.union(dishes)


# utensils.add("napkin")
# utensils.remove("fork")
# utensils.update(dishes)
# utensils.clear()
# for x in dinner_table:
#     print(x)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))

# Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b","c"}
s = set(["a", "b","c"])

print("Normal Set")
print(s)

# A frozen set
fs = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(fs)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# fs.add("h")
# print(fs)