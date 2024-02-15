#!/usr/bin/env python
# coding: utf-8

# **Given an input array, rotate the the array to right by k steps where k is non negative**

# In[2]:


def rotateArray(a,d): #approach through slicing
    n=len(a)
    d = d % n
    a[:]=a[d:n]+a[0:d]
    return a

def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))  # user input
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    print(arr)
    d = int(input("Enter number of rotation: "))
    print("Rotated list is")
    print(rotateArray(arr,d))


main()


# In[ ]:


75

