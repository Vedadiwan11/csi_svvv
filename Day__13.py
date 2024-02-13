#!/usr/bin/env python
# coding: utf-8

# **Given an array of integers, find the maximum, minimum, sum and the average of the array**

# In[8]:


def Max_Min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in arr:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    return max_val, min_val

def Sum(arr):
  sum=0
  for i in arr:
    sum = sum +i
  return sum

def Average(arr):
    total_sum = Sum(arr)
    average = total_sum / len(arr)
    return average


def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))  # user input
    print("Enter the elements of the array from 0 to:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    print(arr)
    max_val, min_val = Max_Min(arr)
    print("Maximum value in the array:", max_val)
    print("Minimum value in the array:", min_val)
    sum1= Sum(arr)
    print("Total sum of array is:",sum1)
    avg = Average(arr)
    print("The average of the array is:",avg)



main()


# In[ ]:




