# Functions:
# A function is a block of code that performs a 











# calling a Function:
# Calling a Function means telling python to run the code inside a function by using it's name folloed by parantheses().
# if the function needs input (parameter), We provide values(argument) inside the parantheses.
# When we call a function , python jumps to the function, excutes it's code , and then comes back to continue the program.
def greet (name, branch): # function name
    print("Hello World1") #
greet("varsith","CSM") # calling a function.
# Passing Parameters & Arguments.
# parameters: A Variable declared inside the function definition.tt'sacts like an empty contaier wating to receive a value.
#Argument: The actual value we pass into the function when calling
# example:
def greet(name) :
    print("Hello",name)
greet("Nandhan")
#  same task without function.
name = "Nandhan"# here name is input variable (parameter), and
# "Nandha" is value to the parameter (Argument.)
print("Hello",name)

# Types of function arguments:
# A. Positional Arguments:
# When we pass Arguments in the same order as the function parameter,
# here the order(position) is very important.
def greet(rollno,name): # step 2 values store
    print("Hello",name,"your rollno is ",rollno) # step3: excte the line
greet("M6","varshith") # step1 : function calling

# B. keyword Aeguments:
# when we pass values or Arguments by writting the parameter(variable = value),they are called as Arguments.
def greet(rollno, name):
    print("Hello", name,"your rollno is",rollno)
greet(name= "varshith",rollno="M6")

# Default Arguments:
# when a parameter has defauit value(assigning the value in parameter) in the function definition, it becomes a default argument.
def greet(name= "Student"):
    print("Hello",name)
greet()
greet(name="varshith")

# D. Varible-Length Arguments:
# sometimes we dot't know how many arguments will be passed to a function.
# python provides two special ways handle this:
#1. *args:(Varible-Length Arguments):
# Collects mutliple values into a tuple.
# L =10,20,30,40,50
def sum1(*List1):
    sum2= 0
    for i in range(len(List1)):
        sum2 = sum2 + List1[i]
    print(sum2) # 150
    print(type(List1))
sum1(10,20,30,40,50) #150
# 2. **kwargs:(keywoed varible_Length Arguments)
# Collects multiple Key=value pair into a dictionary.
def details(**info):
    for i,j in info.items():
        print(i,":",j)
details(Name="varshith",Rollno="M6",Branch="CSM")

# scope of the variable:
# scope of the variable:
#The scope of a variable means the part of the program where 
# examples:
x = 10 # Global variable 
def var1():
    y = 5 # Local variable
    print("inside var1 function",x)
var1()

print("outside function",x)

# Lambda function:
def sqe(a):
    print(a*a) #25
sqe(5)

squ = lambda x:x*x
print(squ(5)) #25