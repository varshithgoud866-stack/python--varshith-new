file = open("students.txt","r")
content = file.read()
print(content)
file.close()
# types of Read:
# 1. read() =>
# 2. readline() =>
file = open("student.txt","r")
content = file.read()
print(content)
file. close()
# 2. redline() =>
file = open("student.txt","r")
content = file.readline() # 1st line
content1 = file.readline() #2nd line
content2 = file.readline() #3rd line
print(content)
print(content1)
print(content2)
file.close()
# 3. readlines() =>

file = open("student.txt","w")
# Write, writelines
file.write("Hello c++\n")
file.write("Hello Python\n")
lines = ["Hello Nandhan\n","Hello Anurag\n","Hello World\n","Hello Python\n"]
file.writelines(lines)
file.close()

file = open("student.txt","a")
# Write, Writelines
file.write("Hello c++\n")
text = b"Hello Nandhan"
file.close()
