# #collection date types
# list1 = [10,20,30,40,50]
# # these collection data types are used to store multiple values in a single variable.
# # types of CDT:
# # 1. lists
# # 2. tuples
# # 3. sets
# # 4. dictionary
# # Lists in python
# # Lists are collection data types which are used to store mutliple values in a variable
# # lists are ordered (the items have a fixed position ) and mutable(we can change, add or remove items from the list).list
# # example 
# list1 = [10,20,30,40,]#integer values
# fruits = ["apple","banana","mamgo"]#strings values
# list2 = [10.1,20.2,30.3,40.4,50.5]#float values
# list3 = [True,False,True,True]# Boolean values
# list4 =[10,20.5,"hello",True,"False"] # mutli datatype values.
# #output
# print(list4)
# #Accessing Element:
# #Accessing Elements are used retrive the list items or values stored at a position (index-indexs are starts from Zero)

# #example :0 1 2 3 4....n-1
# list1 =[10,20,30,40,50]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# #by negative values
# print (list1[-1])
# print (list1[-2])
# print (list1[-3])
# print (list1[-4])
# #slicing in lists
# # slicing is taking out of a part from the main list.
# #slicing will extracts the part or sublist using [start idx : end idx]
# #example:
# slc1 = ["prabhas","balayyaa","pspk","bob","bhai"] 
# print(slc1[:3])
# print(slc1[1:4])
# print(slc1[-3:])
# print(slc1[-4:])
# #Addind Elements in list :
# #we can add new values to list in different ways:
# # 1. Append:adds a  single value at the end of the list.
# kalkicast = ["prabhas", "kamal h", "amitha bhachan","deepka p","ssr"]
# print(kalkicast)
# kalkicast.append("Deesha patani")
# print(kalkicast)
# # 2.insert:adds single value at the perticular position using index
# kalkicast.insert(2,"Vijay D")
# print(kalkicast)
# # 3.Extending : adds mutliple values at once by combining the lists
# kalkicast .extend (["anudeep","mrunal T","bujji"])
# print(kalkicast)
# # example : add bhramanadham ,after the deepika p
# kalkicast = ["prabhas", "kamal h","amitha","deepika p","ssp"]
# kalkicast . append("deesha patani")
# kalkicast . insert(2,"vijay D")
# kalkicast .extend(["Anudeep","mrunal T","bujji"])
# print(kalkicast)
# #output = ["prabhas","kamal h","vijay D","amitha bhachan","Deepika p","ssr","Deesha patani", "anudeep","mrunal T","bujji",]
# kalkicast . insert(5,"bhramanandha")
# print(kalkicast)
# #Removing Elements in list
# #Removing the items in the list in different ways
# # 1. remove().Removes or deletes the first occurence of the specific items
# # 2. pop(): deletes the items from list at the perticular position
# # 3. clear(): Deletes the all items from the list
# #Removing Elements in list
# kalkicast = ["prabhas","kamal h","vijay D","amitha bhachan","Deepika p","ssr","Deesha patani", "anudeep","mrunal T","bujji",]
# kalkicast . remove("mrunal T")
# print(kalkicast)
# # 2. pop(): deletes the items from list from list at the perticular position
# kalkicast.pop(6)
# print(kalkicast)
# # 3. clear(): Deletes the all items from the list
# kalkicast.clear()
# print(kalkicast)


# # changing the Elements: lists are mutable, we can change the values after creating the lists using index
# kalkicast [1] = "sandeep R V"
# print(kalkicast)
# #MV GouDs
# # Mathematical operations in lists
# # 1. concatenation : jions the two 
# a = {1,2}
# b = [3,4]
# c = a+b
# print(c)
# #2. Repetition: Repeats the elements of list mutliple time
# a = [1,2]
# n = int(input("Enter the n value:"))
# b = a * n
# print(b)

# #date 09/09/2025
# #serching and checking:
# #we can check if an element or valule
# #in opertor:
# #it is a membership opertor,which returns the trues values if the elements exists in the lists.
# a = [2,4,6,8,10,12,14]
# if 2 in a:
#      print("yes item is present in the list ")
# # not i operator:
# # it is a membership operator, which returns the trues values if the elements exists in the lists.
# print(3 not in a)
# # index(): which gives the position of the first occurrence of an element or value.
# print(a.index(8)) #3
# # count(): which gives the number of elements in the lists.
# print(a.count(8))
# for i in range(10):
#    if i == 8:
#        cnt = cnt + 1
# print(cnt)

# # sorting [2,5,1,8]
# # it arranges elements either in ascending order (small to large) or descending order (large to small).
# st = [25,12,5,31,13,18,7,45,8,55,68]
# # AO = 5,7,8,12,13,18,25,31,45,55,68
# st.sort()
# print(st)
# # DO = 68,55,45,31,25,18,13,12,8,7,5
# st.reverse()
# print(st)    
# st = [25,12,5,31,18,7,45,8,55,68]
# st. reverse()#68,55,8,45,7,18,13,31,5,12,25
# st.sort()
# print(st) # Do = 68,55,45,31,25,18,13,12,8,7,5
# st1 = [25,8,4,7,10]#25,10,8,7,4
# st1.sort(reverse=True)

# #1  5  4  2  3
# #R = 3 2 4 5 1 # AO = 1 2 3 4 5
# # Ao = 1 2 3 4 5

# # copying the list:
# # copying creates a new list with the same elements, so changes in the new list do not affect the orginal list.
# Frd1 = ["A","c","D","A","D","B","B","C","C","A","A"]
# Frd2 = Frd1.copy()
# Frd2[2] = "B"
# print(Frd2)

# #Built-in Functions with loops:
# # python programming provides many ready-made functions to work with the items
# st = [25,12,5,31,18,7,45,8,55,68]
# # len(): Returns the the number of element.
# print(len(st)) #11
# # max(): Returns the maximum element from the list.
# print(max(st))#68
# # min(): Returns the minimum element from the list.
# print(min(st)) #5
# # sum(): Returns the total sum of all numeric elements.
# print(Sum(st)) # 287
# a = "hello world to the python programming"
# b = a.split()
# print(b)
# #Multipli values using input data to the list
# a = input("enter the mutliple values:") # 10 20 30 40 50
# print(a)
# a = input("enter the mutliple values:").split() # 10 20 30 40 50
# print(a) # ['10','20','30','40','50']
# # list1 = [10,20,30,40,50] #integer values
# a = list( map(int, input("enter the mutliple values:").split())) # 10 20 30 40 50
# print(a) # ['10','20','30','40','50']
# a =  (map(int,input("enter the mutliple values:")).split()) # 10 20 30 40 50
# print(a) # ['10','20','30','40','50']
# a.sort()
# print(a) #[10,20,30,40,50]# integer values

# b = input("enter the mutliple values:").split() # 10 20 30 40 50
# print(b) #['10','20','30','40','50'] #string values

# #Traversing a list:
# # Accesssing the elements using a loop
# car = ["thar","jaguer","Audi","bmw"]
# # index 0        1       2      3
# for car in cars:
#      print("cars=",car)

# # Using index with for  loop:
# a = len(cars) #4
# for i in range(0,a):
#      print("cars", i,cars[i])
# #adding elements using for loop:
# #10-09-2025
# #list1 = 
# list1 = []
# n = int(input("enter the number of list values:"))
# for i in range(0,n): # i 0 1 
#     a = input("Enter the list values: ")  
#     list1.append(a)
# print(list1)
# #give the input values to the lists from 0 to 10

 
# # sum of list items = 10 20 30 40 50 without using sum().
# list1 = [10,20,30,40,50]
# sum = 0 # 100
# for i in list1: # 10 20 30 40 50
#     sum = sum +  i # 150
# print(sum)

# # sum of list items = 10 20 30 40 50 without using sum().
# list1 = [10,20,30,40,50]
# sum = 1 # 100
# for i in list1: # 10 20 30 40 50
#     sum = sum *  i # 150
# print(sum)

# print(sum)
#convert ["p","y","t","h","o","n"] to python
list1 = ["y","t","h","o","n"]
word = "p"
for i in list1:# y t h o n
    word = word + i
print(word)

# Find the maximum and minimum number from list without using max() and min().
list1 = [7,18,12,31,45,17,10,23,229,227] #Max = 229 # Min = 7
list1. sort()
# [7,10,12,17,18,23,31,45,227,229]
#  0  1  2  3  4  5  6  7  8   9
print(list1)
print("Maximum of list :",list1[9])
print("Manimum of list :",list1[0])

# Find the maximum and minimum number from list without using max() and min().
list1 = [52,7,18,12,31,45,17,10,23,229,227]
max1 = list1[0] # 229
min1 = list1[0] # 7
for num in list1: #[52,7,18,12,31,45,17,10,23,229,227]
    if num > max1:
        max1 = num
    if num < min1:
        min1 = num

print(max1)
print(min1)

# searching for an element in a list
Names = ["Mallareddy","Revanth reddy", "Modi", "Rahul gandhi"]
searching_name = input("enter the name to be found: ")  #modi # kcr
found = False
for i in Names:
    if searching_name == i:
        found = True

if found:
    print("yes")
else:
    print("No")

# Count even and odd numbers
numbers = [7,10,12,17,18,23,31,45,227,229]

eve_cnt = 0
odd_cnt = 0

for i in range(len(number)):
    if number[i]%2 == 0:
        evn_cnt += 1
    else:
        odd_cnt +=1
print("Number of even numbers are:",evn_cnt)
print("Number of odd number are:",odd_cnt)
# Reversing a list without reverse
list1 =[7,10,12,17,18,23,31,45,227,229] # 1 = 10
#ind  =0   1  2  3  4  5  6  7  8   9
l = len(list1)
r_list = []
for i in range(1-1,-1,-1):
    r_list.append(list[i])
print(r_list)

# Removing all negative numbers using loop
numbers = [-56,-9,2,-8,-30,45,23,-19,72,-55,-18,7,0]
postive_list =[]
for i in range(len(numbers)):
    if numbers[i] >= 0:
        postive_list.append(numbers[i])
print(postive_list)

# Multiply each element in the list
numbers =  [-56,-9,2,-8,-30,45,23,-19,72,-55,-18,7,0]
m = int(input("Enter the number to be mutliplied:"))
After_mutliplication = []
for i in numbers:
      After_mutliplication.append(i*m)
print(After_mutliplication)

