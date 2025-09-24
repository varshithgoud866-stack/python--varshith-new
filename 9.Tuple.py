#Tuple is a collection datatype, which is used to store the multiple values in a single variable.
# Tuple is a ordered,Immutble, Also allows the duplicate values,and can  store mixed data types in values.

# example :
coordinates =("x","y")
my_tuple = (10,20,30)
print(my_tuple)
print(type(my_tuple))

# Creating a Tuple:
# Empty tuple
Et = ()
# tuple with string:
N = (1,2,3,4,5,6)
# Tuple with strings:
s = ("A","B","C","a","b","c")
# Tuple with 


# Tuple with single element:
a = 10 # Int
print(type(a))
b = [10] # list
c = (10) # Tuple
print(type(c))

# Accessing Elements:
# Tuple uses index values to access an element.
A = (10,20,30,40)
#i    0  1  2  3
#-i   -4 -3 -2 -1
print(A[0]) # 10
print(A[1]) # 20
print(A[2]) # 30
print(A[3]) # 40
print(A[-1]) # 40
print(A[-2]) # 30
print(A[-3]) # 20
print(A[-4]) # 10
 #Slicing the tuple:
 # Extracts part of the tuple using start index and end index
 # ([start index: end index])
 # In tuple it will print before the end index value.
A = (10,20,30,40)
#i   0  1  2  3
#-i  -4 -3 -2 -1
print(A[1:3]) # 20 30 40
print(A[:2]) # 10  20
print(A[-3:-1]) # 20 30

# # changing the values:
# # Tuples are immutable, so we cannot change the values.
# A[1] = 50
# print(A)# TypeError: 'tuplr'object does not support item assignment
# # append():
# A.append(50)
# print(A)

# Length:
# max:
# min:
# sum:

# Length:
A = (10,20,30,40)
print(len(A))

#max:
A = (10,20,30,40)
print(max(A))

# min:
A = (10,20,30,40)
print(min(A))

#sum:
A = (10,20,30,40)
print(sum(A))

# Concatination
# Repetation

# Searching and checking:
# in operator:
# not in operator:
# index():
# Count():
# in
A = (10,20,30,40)
print(20 in A)
print(60 in A)
print(20 not in A)

#index():
A = (10,20,30,40)
print(A.index(30))
print(A.index(10))

# Count
A = (10,20,30,40)
print(A.Count(40))

# sorting and Reversing:
# Iterating tuple using for loop:
