#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
print("hello world")


# In[2]:


#2
a=int(input("enter the value of A"))
b=int(input("enter the value of B"))
a+b


# In[3]:


#3
a=5
b=6
a,b=b,a
print("a=",a,"b=",b)


# In[4]:


#4
a=int(input("enter the year"))
if(a%400==0)and(a%100==0):
    print("leap year")
elif(a%4==0)and(a%100!=0):
    print("leap year")
else:
    print("not leap")


# In[1]:


#5
a=int(input("enter the number"))
if a==0:
    print("0")
elif a>0:
    print("positive")
else:
    print("negative")


# In[2]:


#6
a=float(input("enter kilometer"))
b=a*0.621371
print("mile is",b)


# In[3]:


#7
a=int(input("start value"))
b=int(input("end value"))
for i in range(a,b):
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if(c==1):
        print(i)


# In[8]:


#8
n1=0
n2=1
print(n1)
for x in range(1,10,1):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum


# In[ ]:


#9
y=int(input("enter the sum for n th term"))
sum=0
for x in range(1,y+1,1):
    sum+=x
print("sum of n terms",sum)


# In[17]:


#10
n=int(input("enter the number"))#153
a=n//100 #1
b=n%100 #53
c=b//10 #5
e=n%10 #3
f=((a**3)+(c**3)+(e**3))
if n==f:
    print("the given number is amstrong number")
else:
    print("the given number is  not amstrong number")


# In[20]:


#11
a=int(input("Enter the value of a"))
sum=0
for i in range(0,a+1):
    sum+=i
    print(sum)


# In[22]:


#12
#*
#**
#***
#****
#*****
n=6
for i in range(1,n):
    print("*"*i)




# In[24]:


#13
name="vijaysiva"
n=int(input("enter the number"))
b=name[n+1:]
print(b)



# In[26]:


#14
list=[45,43,45,67,50]
for i in range(n):
    if i%5==0:
        print(i)
    


# In[1]:


#15
rows =6
for i in range(rows):
    
    for j in range(i):
    
        print(i, end=' ')
    
    print('')





# In[2]:


#16
n=int(input("enter the value"))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
if(temp==sum):
    print("palindrome")
else:
    print("not pallindrome")


# In[3]:


#17
list=[1,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print(list)


# In[4]:


#18
def swapList(sl,pos1,pos2):
    n = len(sl)     
    # Swapping 
    temp = sl[pos1]
    sl[pos1] = sl[pos2]
    sl[pos2] = temp
    return sl      

l= [10, 14, 5, 9, 56, 12]
pos1= 2
pos2= 5

print(l)
print("Swapped list: ",swapList(l,pos1-1,pos2-1))


# In[5]:


#19
list=[1,2,3,4,5,6,7,8,9]
print(len(list))


# In[6]:


#20
a=7
b=6
if(a>b):
    print("a is greater")
else:
    print("b is greater")


# In[7]:


#21
a=7
b=6
if(a>b):
    print("a is lesser")
else:
    print("b is lesser")


# In[13]:


#22
string = 'chutkichutki'
half = int(len(string) / 2)
 
 
first_str = string[:half]
second_str = string[half:]
 
 
# symmetric
if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')
 
# palindrome
if first_str == second_str[::-1]: 
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')


# In[14]:


#23
list=['hello','cat','dog']
list.reverse()
print(list)


# In[17]:


#24
teststr = "bheem"
newstr = teststr.replace('e', '')
print ("The string after removal of i'th character( doesn't work) : " + newstr)
newstr = teststr.replace('b', '', 1)
print ("The string after removal of i'th character(works) : " + newstr)



# In[26]:


#25
str="buddy"
print(len(str))


# In[27]:


#26
n="how are you"
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)




# In[29]:


#27
import sys
tup1= ("hi", 1, 2, 3)
tup2= ("english", "math", "science")


print("Size of tuple1: ", sys.getsizeof(tup1), "bytes")
print("Size of tuple2: ", sys.getsizeof(tup2), "bytes")



# In[31]:


#28
tup=(2,4,1,6,3)
print("Maximum element",max(tup))
print("Minimum element",min(tup))


# In[30]:


#29
tuple = (10, 20, 30)
total = 0
for element in tuple:
    total += element
print("The Sum Of The Elements In The Tuple Is",total)


# In[1]:


#30
a=(5, 10, 15, 20)
b=(3, 5, 7 ,9)
print("First Matrix ",a)
print("Second Matrix: ",b)
result = tuple(map(lambda x, y: x + y,a,b))
print("Tuple Matrix After Addition: ",result)


# In[1]:


#31
list1 = [1, 2, 5, 6]
res = [(val, pow(val, 3)) for val in list1]
print(res)


# In[2]:


#32
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)


# In[3]:


#33
import random as rn
dict = {}
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;
print(dict)


# In[4]:


#34
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    return final
dict = {'a': 10, 'b': 20, 'c': 30}
print("Sum :", returnSum(dict))


# In[5]:


#35
import sys
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "zebra", 2: "Tiger", 3: "Fox", 4: "tiger"}
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")


# In[6]:


#36
test_set = set("geEks")
for val in test_set:
    print(val)


# In[7]:


#37
def Max(sets):
    return (max(sets))
sets = set([8, 16, 24, 1, 25, 30, 100, 65, 85])
print(Max(sets))


# In[ ]:


#38
def min(sets):
    return(min(sets))
sets = set([2,5,7,3,9,20])
print(min(sets))



# In[2]:


#39
list=['apple','orange','strawberry']
list.remove('orange')
print(list)


# In[1]:


#40
s={1,2,3,4,5}
p={5,6,7,8,9}
for i in s:
    for j in p:
        if i==j:
            print("the common element is", i)


# In[1]:


#41
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("the matrix is:")
for i in range(1, len(matrix)):
    matrix[i] = matrix[0]
print(matrix)


# In[2]:


#42
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()


# In[3]:


#43
elements = [1, 2, 3, 2, 1, 3, 4, 5, 4, 5, 5]
element_counts = {}
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
num_rows = max(element_counts.values())
num_cols = len(element_counts)
matrix = [[None] * num_cols for _ in range(num_rows)]
for col, element in enumerate(element_counts):
    count = element_counts[element]
    for row in range(count):
        matrix[row][col] = element
for row in matrix:
    print(row)


# In[4]:


#44
matrix = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9))
row_sums = [sum(row) for row in zip(*matrix)]
print("Row-wise sums:")
for sum_value in row_sums:
    print(sum_value)


# In[5]:


#45
def create_even_submatrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = 1
    return matrix
n = 4
result = create_even_submatrix(n)
for row in result:
    print(row)


# In[6]:


#46
import inspect

def my_function(guna,dinesh, kannan):
    pass

parameters = inspect.signature(my_function).parameters
parameter_names =list(parameters.keys()

print(parameter_names)


# In[7]:


#47
name = "riya"
age = 28
city = "New York"

print(name, age, city)


# In[8]:


#48
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

base =int(input("Enter the base: "))
exponent =int(input("Enter the power: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")


# In[9]:


#49

class grade:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def __repr__(self):
        return str((self.a, self.b))
  

g= [grade("riya", 'a'),
       grade("diya", 'b'),
       grade("tanvi", 'c'),
       grade("shalu", 'd'),
       grade("miya", 's')]
print(sorted(g, key=lambda x: x.b))


# In[ ]:


#50
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="riya", age=18, city="chennai")


# In[ ]:




