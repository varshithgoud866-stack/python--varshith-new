  # Arrays in python:
  # An Array is collection of elements of the same datatype stored in a continuous memory location.
  # Arrays are used to store mutlipl values in a single variable.
  # why Arrays?
 # Easy to manage multiple values.
# Allows Faster operations like searching and sorting.
# Useful in mathematica and scientific problems.
# Array VS Lists:
#Importing the arry module.
import array as arr

# Creating an array:
Numbers = arr.array('i',[1,2,3,4,5])
print(type(Numbers))

# i = integer
# f = float
# u = String

# Accessing Array Elements.
print(Numbers[0]) #1
print(Numbers[3]) #4
print(Numbers[-1]) #5

# Addind an element in arry:
# append():
Numbers.append(7)
print(Numbers)
# insert():
Numbers.insert(2,6)
print(Numbers)
# extend():
Numbers. extend([8,9])
print(Numbers)

# Deleting an element:
# remove():
# pop():

# Looping through Arrays:
for i in Numbers:
    print(i)
# Basic Operations on arrays:
# len ():
# max():
# min ():
# sum():
