#!/usr/bin/env python
# coding: utf-8

# In[1]:


# write a program that checks if a number entered by the user is even or odd and prints the result.
def compute_even_odd(y):
    if y%2==0:
        return "even"
    else:
        return "odd"
def exit_program():
    print("exiting the program...")

while True:
    y = int(input("Enter an integer: "))

    result = compute_even_odd(y)
    print("The number is", result)

    choice = input("If you want to continue (yes/no): ").lower()
    if choice != "yes":
        exit_program()
        break


# In[ ]:




