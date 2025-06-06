# Introduction to Lists

"""
A list is a collection of similar or different types of data items.
"""

# Creating a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list of 10 integers
numbers = [] #empty list
numbers = [1, 2, 3, 4, 2, 3, 4, 4, 4] #list of duplicate integers
items = [1, 2, "N", "Go", 3.1453] #list of different items

# Features of a list
"""
1. List can have duplicate items.
2. Items in a list are mutable.
3. Lists can store items of various types
"""

# Accessing Elements in a list
"""
1. Accessing Elements of a single-dimensional list
2. Negative indexing
3. Accessing Elements of a multi-dimensional list
4. Homework problem
"""
#  Accessing Elements of a single-dimensional list
"""A single-dimensional list is a list where elements are listed one after the other.
- Each element is allotted a unique number called index.
"""
my_list = [5, 10, 15, 20]
print(my_list[0])
print(my_list[2])

# Negattive Indexing
my_list = [5, 10, 15, 20]
print(my_list[::-1])

# Accessing Elements of a multi-dimensional list
my_list2 = [[1, 2, 3], "Neso", [4, 5, 6]]
print(my_list2[0][0])

#  Homework problem
my_list3 = [[1, 2, 3], [["a", "b", "c"], 5, 6]]
print(my_list3[1][0][1])

# Adding Elements to a List
"""
1. Adding elements to a list
2. append() method
3. insert() method
4. extend() method
"""
# append() method
languages = ["C", "cpp", "Java"]
languages.append("python")
languages.append("ruby")
languages.append("javascript")
languages.append("rust")
languages.append(["php", "html", "css"])


# insert() method
languages = ["C", "cpp", "Java"]
languages.insert(0, "python")
print(languages)

# extend() method
languages = ["C", "cpp", "Java"]
more_languages = ["python", "javascript"]

# languages.extend(more_languages)
# print(languages) 


# # input() method in python
# name = input("What is your name?")
# print(name)

# number = int(input("Enter a number: "))
# print(number * 2)

# # Input a list using loops
# n = int(input("Enter the number of elements: "))
# numbers = []
# for i in range(n):
#     x = int(input())
#     numbers.append(x)
# print(numbers)

# Input a list using split() method in python
# sentence = "I am John"
# print(sentence.split())
# numbers = input("Enter a list of numbers: ").split(",")
# numbers_list = []
# for num in numbers:
#     numbers_list.append(int(num))
# print(numbers_list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# list[2] = "Foster"
# print(list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# list[2:4] = ["Michael", "Foster", "Emma"]
# print(list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# list.insert(2, "Michael")
# print(list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# list.remove(1)

# print(list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# list.pop(1)
# print(list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# del list[0]
# print(list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# del list
# print(list)

# list = ["Rob", "Jennifer", 1, 2, "Bob"]
# list.clear()
# print(list)

# Introduction to list comprehension
# names = ["John", "James", "Emmy", "Michael", "Jimmy"]
# copy_names = [name for name in names]
# print(copy_names)


# animals = ["lion", "tiger", "monkey", "elephant", "frog"]
# filtered_animals = [animal.title() for animal in animals]
# print(filtered_animals)

# 1. a
# 2. c
# 3. b
# 4. d
# 5. a
# 6. c
# 7. d
# 8. a
# 9. d
# 10. b

import array as arr

print(len(arr.array('i',[1,2,3])))