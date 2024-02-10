#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Implement bubble sort algorithmto sort an array 

def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def print_array(arr):
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()

def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))  # user input
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    Bubble_sort(arr)
    print("The sorted elements are:", end=" ")
    print_array(arr)

main()


# In[ ]:




