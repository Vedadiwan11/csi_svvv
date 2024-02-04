#!/usr/bin/env python
# coding: utf-8

# In[1]:


# define a funtion that calculates the factorial of a given number and use it find the factorial of 5.


# In[2]:


import math
def factorial(num):
    return(math.factorial(num))

n = factorial(5)
print("The factorial of 5 is", n)

print("--------------------------")
print("user's input")

num = int(input("enter the number: "))
f= factorial(num)
print("The factorial of",num, "is",f)


# In[ ]:




