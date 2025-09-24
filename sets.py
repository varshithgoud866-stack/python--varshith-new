# Sets:
# Set is a collection datatype which is used to stored mutliple values in a single varaible.
#Sets are unordered, unindexed, mutable, and they do not allow duplicate values.
# They are useflu when you want to store unique elements and performs the mathematical operationsl like union, intersction, and differenc.
# Syntax:
# My_set + {element1,element2,element3}


# Cheracteristics of Sets:
#Unordered:
#example: {1,2,3} and {3,2,1} are considered the same set.
# unindexed: You cannot access set elements by the index like lists or tuples. set[1]
#like lists or tuples. set[1]
a = {1,2,3}
print(a[1])
# Unique values only: Duplicacate values are automatically removed from the set
a = {1,2,3,3,2,1,1,1,2}
print(a) # output {1,2,3}

# Creatin a set:
s1 = {1,2,3}
s2 = {10,12.5, "Hello",True}
# Empty set:
s3 = {}
s3 = set()
print(type(s31)) # Set

# Accessing sets:
#we cannot directly access an element using index but
# We cccess an element using loops.
A = {"rajinikant","Snake king", "Upender"}
for role in a:
    print(role)
# Adding an element in sets:
S = {12,18,20}
S . update([34,29]) # adds the mutiple values in the set
print(s)# {12,18,20,25,34,29,25}
# Deleting the elements in set:
# remove(): Removes the element, but it gives an error if the  value is not found in the set
S.remove(26)
print(s) # {12,18,20,34,29}
#discard(): Removes the element, but it given no error if the value is not found in the srt
S = {12,18,20,25,34,29}
S . discard(26)
print(S) # {12,18,20,25,34,29,25}
S.pop()
print(S)
# clear(): Removes the every element from the set.
S = {12,18,20,25,34,29,25}
S.clear()
print(S)

# Mathematical Opertions in set:
# Union "U"="|": prints all unique values or elements from the bot sets.
A = {1,2,3,}
B = {4,5,6}
print(A| B) # {1,2,3,4,5,6}
# Intersection "n" = "&" : prints the common elements from the set







#13/09/2025
# Symmetric difference "^":
# removes the common elements from the lists but prints only the first sets values.
A = {1,2,3,4}
B = {3,4,5,6}
print(A ^ b) # {1,2,3,5,6}

# Mathematical Opertions using function :
A = {1,2,3,4}
B = {3,4,5,6}
# Union
print(A.union(B)) # {1,2,3,4,5,6}
#Intersection
print(A.intersection(B)) # {3,4})
# Difference
print(A.difference(B))# {1,2}
# Symmetric difference
print(A.symmetric_differece(B)) # {1,2,5,6}

# len():
S = {10,15,82,92,22}
print(len(S)) # 5
# MAX ():
S = {10,15,82,92,22}
print(MAX(S)) # 96
# MIN():
S = {10,15,82,92,22}
print(MIN(S)) #10 
#SUM():
S = {10,15,82,92,22}
print(SUM(S)) # 225
