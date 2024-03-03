#!/usr/bin/python3

# Creating empty list
my_list = []

# Appending 10,20,30,40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at index 2 in the list
my_list.insert(1, 15)

# Extending my_list with another list with 50,60,70 elements
my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop()

# Sorting my list in ascending order
my_list.sort()

# Finding index of value 30 in my_list
index = my_list.index(30)

# Printing the index of value 30
print("Index of value 30:", index)

# Printing the final list after all modifications.
print("The final list is:", my_list)
