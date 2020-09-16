## Lists, both lectures 1 and 2

# I have 3 lists declared below, play around with the following
# functions, methods, slices or other ones you like on them
# len(), min(), max(), append(), insert(), extend(), remove(), pop()
# reverse()
# Note: Some methods/functions above are covered in lecture 1
# while others are covered in lecture 2

my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10, 15]
# indices   0  1  2  3  4   5    6  7   8   9
my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
my_new_list = ["art", "econ"]
print(f"Ints: {my_list}")
print(f"Strings: {my_strings_list}")
print("Sorting....")
my_list.sort() # this is a method - sorts in-place
sorted_list = sorted(my_list) # this is a function
print(sorted_list)
print(f"New list: {my_list}")

print("Finding info.......")
print("physics" in my_strings_list)
print(my_strings_list.index("elec engr"))
print(len(my_list))
print(min(my_list))
print(dir(my_list))
print(my_list.count(15))

print("Add/remove........")
my_list.append(25)
print(my_list)
my_list.insert(4, 24)
print(my_list)
# my_strings_list.append(my_new_list)
# print(my_strings_list)
my_strings_list.extend(my_new_list)
print(my_strings_list)
my_strings_list.remove('comp sci')
print(my_strings_list)
a = my_strings_list.pop(0)
print(my_strings_list)
print(a)

print("Sublists......")
# my_list[-1] = 1000
# print(my_list[::-1])
# my_list.reverse()
print(my_list)

for item in my_list:
     print(item)





# Write your function or method code here

# print("My altered lists...")
# print(my_list)
# print(my_strings_list)
# print(my_new_list)
