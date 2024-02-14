#!/usr/bin/env python
# coding: utf-8

# **Given an array of integers and target element, count the number of occurences of the target element in the array**

# In[12]:


def Count(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))  # user input
    print("Enter the elements of the array from 0 to:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    print(arr)
    target = int(input("enter the element to be searched: "))
    count = Count(arr,target)

    if count !=0:
                 print("The number appeared",count,"times")
    else:
                 print("The number is not in the list")




main()


# In[ ]:




