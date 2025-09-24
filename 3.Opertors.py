#arithimatic opertor
a = 5
b = 8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#comparison or relational opertor
a = 6
b = 8
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)
#Logical opertors
#and
p = 5
q = 10
print(p>2 and q>5)
print(p>2 and q<5)
print(p<2 and q>5)
print(p<2 and q<5)
#or
p1 = 5
q1 = 10
print(p1>2 or q1>5)
print(p1>2 or q1<5)
print(p1<2 or q1>5)
print(p1<2 or q1<5)
#not
p2 = 5
q2 = 0
print(not(p2))
print(not(q2))
#Assigment opertors
a1 = 10
print(a1)
a1 += 1
print(a1)
a1 -= 1
print(a1)
a1 *= 2
print(a1)
a1 /= 2
print(a1)
a1  //= 2
print(a1)
#Bitwise opertor
x1 = 5
y1 = 3
print(x1 & y1)
print(x1 | y1 )
print(~x1 )
print(x1 ^ y1)
print(x1 << y1)
print(x1 >> y1)
x1 = 5
y1 = 10
print(x1 & y1)
print(x1 | y1)
print(~x1)
x1 = 50
y1 = 68
print(x1 & y1)
print(x1 | y1)
print(~x1)
print(x1 ^ y1)
print(x1 << y1)
print(x1 >> y1)
x1 = 6 
x2 = 8
print(x1 << x2)
print(x1 >> x2)
a = 8
b = 8
print(a << b)
print(a >> b)
print(a ^ b)
print(a | b)

#identity operator
x = [1,2,3,4]
y = x
z = [1,2,3,4]
print(x is y)
print(x is not y)
x = [1,2,3,4]
y = x
z = [1,2,3,4]
print(x is y)
print(x is z)
print(x is not z)
#membership operator
text = [1,2,3,4]
print =(4 in text)#True
print = (5 in text)#False
print(4 not in text)# False
print(5 not in text)# True
#date 09/09/2025
#serching and checking:
#we can check if an element or valule
#in opertor:
#it is a membership opertor,which returns the trues values if the elements exists in the lists.
a = [2,4,6,8,10,12,14]
if 2 in a:
     print("yes item is present in the list ")
# not i operator:
# it is a membership operator, which returns the trues values if the elements exists in the lists.
print(3 not in a)
# index(): which gives the position of the first occurrence of an element or value.
print(a.index(8)) #3
# count(): which gives the number of elements in the lists.
print(a.count(8))
for i in range(10):
   if i == 8:
       cnt = cnt + 1
print(cnt)

# sorting [2,5,1,8]
# it arranges elements either in ascending order (small to large) or descending order (large to small).
st = [25,12,5,31,13,18,7,45,8,55,68]
# AO = 5,7,8,12,13,18,25,31,45,55,68
st.sort()
print(st)
# DO = 68,55,45,31,25,18,13,12,8,7,5
st.reverse()
print(st)    
st = [25,12,5,31,18,7,45,8,55,68]
st. reverse()#68,55,8,45,7,18,13,31,5,12,25
st.sort()
print(st) # Do = 68,55,45,31,25,18,13,12,8,7,5
st1 = [25,8,4,7,10]#25,10,8,7,4
st1.sort(reverse=True)

#1  5  4  2  3
#R = 3 2 4 5 1 # AO = 1 2 3 4 5
# Ao = 1 2 3 4 5

# copying the list:
# copying creates a new list with the same elements, so changes in the new list do not affect the orginal list.
Frd1 = ["A","c","D","A","D","B","B","C","C","A","A"]
Frd2 = Frd1.copy()
Frd2[2] = "B"
print(Frd2)

#Built-in Functions with loops:
# python programming provides many ready-made functions to work with the items
st = [25,12,5,31,18,7,45,8,55,68]
# len(): Returns the the number of element.
print(len(st)) #11
# max(): Returns the maximum element from the list.
print(max(st))#68
# min(): Returns the minimum element from the list.
print(min(st)) #5
# sum(): Returns the total sum of all numeric elements.