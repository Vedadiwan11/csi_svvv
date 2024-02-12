#!/usr/bin/env python
# coding: utf-8

# **Find the missing number: Given an array containing n distinct numbers taken from 0,1,2,-----n,find the one that is missing from the array**

# In[18]:


def Missing_number(arr,n):
    expected_sum =n*(n+1)/2

    array_sum= sum(arr)

    missing_number = expected_sum - array_sum
    print("The array is missing the number:", missing_number)


def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))  # user input
    print("Enter the elements of the array from 0 to",n,":")
    for i in range(n):
        element = int(input())
        arr.append(element)
    print(arr)
    Missing_number(arr,n)


main()


# In[ ]:


5

