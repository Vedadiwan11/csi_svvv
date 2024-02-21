#!/usr/bin/env python
# coding: utf-8

# **Write recursive function to calculate the factorial of a given number non-negative number**

# In[7]:


def Factorial(num):
    if num == 0:
        return 1
    else:
        return num * Factorial(num-1)

def main():
  num = int(input("Enter the nuber: "))
  fact_num = Factorial(num)
  print("The factorial of of {} is {}.".format(num, fact_num))

main()

