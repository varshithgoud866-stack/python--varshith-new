#Dictionary:
# dictionary is a in-buili datatype,which is used to store multipl values in a single varaible
# Dictionary stores the data in the form of key-values pairs.
# Each key is unique and works as an index to access its corresponding value.
# keys are immutable(can't be changed once created), while values can be anything(mutable).
# Dictionary are : Ordered(From python 3.7+ version), Mutable, Do not allows the dupicate keys
# Syntax:
My_dict = {
    "Key1":"Value1",
    "Key2":"Value2",
    "Key3":"Value3",
    "Key4":"Value4"
}
print(My_dict)
# characteristics of Dictionary:
# Key-value pairs:
# Every entry of Dictionary's element is a  pair:Keys and values.
# { "name":"nandha"}
# unique keys:
#example:
A = {"n":"varshith","n1":"goud"}
print(A) # "n1" : varshith

#Keys can be (valid keys): integer,float,string
my_dict  = {
 1:"Value1",
 10.2: "Value2",
 "Key3": "Value3",
"Key4":"Value4",
}

#  Crrating Dictinary:
#  Normal Dictinary:
BioData = {
    "Name": "Nandhan",
    "Roll.No":"5L6",
    "Branch": "CSE AI&ML",
    "Place": "Kamareddy"
}
# Dictionary using Constructor:
# BioData1 = dict(Name="Nandhan",Roll_No="5L6"),
# Branch="CSE AI&ML",  Place="Kamareddy")
# # Empty Dictionary:
E_D ={}

# Accessing the DIstionary:
# -> To access an element we can use key names inside the square brackets [] or we can use get () method
BioData = {
    "Name": "Nandhan",
    "Roll.No":"5L6",
    "Branch": "CSE AI&ML",
    "Place": "Kamareddy"
 }
# #square brackets []
# print(BioData["varshith"]); # varshith
# print(BioData["Roll.No"]) # 5L6
# print(BioData[" Branch"]) # CsE AI&ML
# print(BioData["PLace"]) # Kamareddy
# print(BioData["age"]) # Keyerror (because the "age is")

# using get () method:

print(BioData.get("Name")) # Anurag
print(BioData.get("Roll.No")) 
print(BioData.get("Branch")) 
print(BioData.get("Place")) 
print(BioData.get("age")) 

# Adding and Updating Dictionary:
# Adding: You can Insert a new Key - value pari in to a dictionary.
# Updating: You can update or change the values using exsisted Keys in the dictionary.
BioData = {
    "Name":"Anurag",
    "Roll.No":"5L5",
    "Branch": "CSE AI&ML",
    "Place":"Kamareddy"
}

BioData["age"] = 24 #adding the new key and values
print(BioData)
BioData["Place"] ="Hyderabad" # changing or updating the exsisted Key 's value.
print(BioData)

# Removing in Dictionary:
# Python gives mutliple ways to delete items from a dictionary.
# POP(),popitem(),clear(), Del(delete)
BioData = {
 "Name":"SaiRam",
 "Roll.No":"5L5",
 "Branch": "CSE AI&ML",
 "Place":"Kamareddy",
 "Role":"charminar_model",
}
#POP(): Removes the key value
BioData. pop("Roll.No")
print(BioData)
# popitem(): Remove the last inserted item from the dictionary.
BioData.popitem()
print(BioData)
# del (delete): Deletes the Key from dictionry.
del BioData["Branch"]
print (BioData)
# clear(): Removes every item from dictionary.
BioData.clear()
print (BioData)


# Dictionary methods:
# Methods allow you to access dictionary data easily.
# Key(),values(), items()
BioData = {
     "Name":"saiRam",
    "Roll.No":"5L5",
    "Branch": "CSE AI&ML",
    "Place":"Kamareddy",
    "Role": "Software Developer"
}
# Keys(): It prints only the key of dictionary
print(BioData.keys())
# Values(): It prints only the values of dictionary
print(BioData.values())
# items(): it prints oniy the keys and valued of dictionart
print(BioData. items())

# updating update(): update the muliple values
BioData.update({"Role":"Web Developer","place":"hyderabad"})
print(BioData)

#Loops for Dictionary :

L = [10,20,30,40,50]

for i in range(0,5):
    print(L[i])
BioData = {
    "Name": "SaiRam",
    "Roll.No":"F9",
    "Rolle":"Softwere Developer",
    "place": "hyd"
}
# Loops to iterate the keys (dy defauli the Dictinary's will stores the keys value.):
for i in BioData:
    print(i)
for i in BioData.keys():
    print(i)
# Loops to iterate the keys using keys() method:
for i in BioData. keys():
    print(i)
#Loops to iterate the values using values() method:
for i in BioData. values():
    print(i)
#Loops to iterate the items using items() method:
for i in BioData. items():
    print(i)
     

 # Nested Tuple:
T = (10,(20,30),(40,50))
print(T[2][0])
print(T[1][0])

# Nested Dictionary
Students = {
"S1" : {"Name":"Nandhan", "RollNo":"L6"}, 
"S2" :{"Name":"Aurag", "RollNo":"L7"},
"S3" : {"Name":"Mani", "RollNo":"L8"}
}
print(Students["S1"]["Name"])
print(Students["S2"]["Name"])
print(Students["S3"]["Name"])
print(Students["S4"]["Name"])