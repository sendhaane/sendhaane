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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




