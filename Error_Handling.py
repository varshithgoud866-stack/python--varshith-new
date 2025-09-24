# Error Handling:
# -> Errors are mistakes in program that stop it form working correctly.
# -> Exception is  a special type of error that occurs while the program is running.
# -> Python provides ways to handle exceptions so that the program doesn't crash suddenly.
# Types of error:
# 1. compile-time Error: (syntax Error)
# Errors that happen when the code is not written corectly(wrong syntax)
# 2. Logical Error:
# Errors when the program runs but gives wrong output because the logic is wrong.
# 3. Runtime Error: (Exceptions)
# Errors happens when the program is running.

# Types of exception in python:
# 1. ZeroDivisionError
# 2. ValueError
# 3. IndexError
# 4. KeyError
# 5. TypeError
# 6.FileNotFoundError
# 7. NameError

# 1 . ZeroDivisionError:
# it is an exception which divides a number by zero.
try:
    a = int(input("Enter the numerator:"))
    b = int(input("Enter the Dinominator"))
    c = a%b
    print(c)
except ZeroDivisionError:
    print("The values given is invalid because dinominato should not be zero")

try:
    i = 3
    n = int(input("Enter the n value:")) #
    if i%n==0:
        print("yes, number not is multiple of,n")
    else:
        print("No, number not is multiple of,n")
except ZeroDivisionError:
    print("Error: Division by zero is not possible" )
# ValueError:
# it's an exception that gives as invalid value given.
try:
    rollno = int(input("Enter ypur rollNo"))
except ValueError:
    print("Error: Given value is not in the interger datatype.")
 # IndexError:
try:
    list = [10,20,30] # 0 1 2 
    n = int(input("Enter the index value:"))
    print(list[n])
except IndexError:
    print("Error: the Given index value is not form   list.")

# KeyError:
try:
    Dict  = {"name":"nandhan","RollNo":"L6"}
    print(Dict["age"])
except KeyError:
    print("Error: the given key is not form the list")

# TypeError:
try:
    List  = [10,20,30]
    Sum = List + 5
    print(Sum)
except TypeEreor:
    print("Invalid type operation.")

# NameError:
try:
    print(Mult)
except NameError:
    print("Variable not declared")

# FileNotFoundError:
try:
    file = open("detail,txt","r")
    print(file.read())
except:
    print("File is not found in the system.")
finally:
    print("Program is excuted")  