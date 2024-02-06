#!/usr/bin/env python
# coding: utf-8

# In[2]:


#write a program to print all the elements in an array.

array = [2, 4, 6, 8] # given example

print("The elements are:", end=" ")
for i in array:
    print(i, end=" ")


# In[1]:


# it includes example with user input

def print_numbers_in_array(arr):
    print("Numbers in the array:", end=" ")
    for num in arr:
        print(num, end=" ")

def main():
    arr = []
    n = int(input("Enter the number of elements in the array: ")) #user input
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)


    print_numbers_in_array(arr)

#given example
array = [2,4,6,8]
t1 = print_numbers_in_array(array)
print("------------------------------------")
main()# call for user input


# In[ ]:




