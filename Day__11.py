#!/usr/bin/env python
# coding: utf-8

# **Implemnt the insertion sort algorithm to sort an array of integers in non _decreasing order.
# After sorting the array , implement the binary search algorithmto search for the given number in the sorted array.**

# In[7]:


def insertion_sort(arr):         #insertion sort
  for i in range(1,len(arr)):
    key = arr[i]

    j = i-1
    while j>=0 and key<arr[j]:
      arr[j+1] = arr[j]
      j -=1
    arr[j+1] = key


def print_array(arr):
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()


def binary_search(arr, l, r, num):      # binary search
  while l <=r:

    mid = l +(r-l)//2

    if arr[mid]== num:
      return mid

    elif arr[mid] < num:
      r = mid - 1

    else:
      l = mid + 1

  #not present
  return -1


def main():
    arr = []
    n = int(input("Enter the number of elements in the array: "))  # user input
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    insertion_sort(arr)
    print("The sorted elements are:", end=" ")
    print_array(arr)

    num = int(input("enter elemnt to be searched: "))
    result = binary_search(arr, 0, len(arr)-1, num)
    if result != -1:
      print("element", num, "is present at index",result)

    else:
      print("element", num,"is not present in array")


main()

