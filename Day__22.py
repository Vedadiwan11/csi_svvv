#!/usr/bin/env python
# coding: utf-8

# # Implement a recursive function to compute the nth fibonacci number.

# In[4]:


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter the value of n to compute the nth Fibonacci number: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")

