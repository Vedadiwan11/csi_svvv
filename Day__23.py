#!/usr/bin/env python
# coding: utf-8

# # Write a recursive function  to calculate the sum of digits of positive integer
# 

# In[4]:


def sum_of_digit( n ):
    if n == 0:
        return 0
    elif n<0:
        return -1
    else:
        return (n % 10 + sum_of_digit(int(n / 10)))

n = int(input("Enter the number of numbers you want to add: "))
result = sum_of_digit(n)
if result == -1:
    print("Invalid input: Number of numbers should be non-negative.")
else:
    print(f"The sum of the given numbers is: {result}")

