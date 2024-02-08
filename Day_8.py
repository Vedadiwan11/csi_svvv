#!/usr/bin/env python
# coding: utf-8

# In[9]:


#write a program to reverse an array.

array = [2, 4, 6, 4] # given example

print(array[::-1])


# In[10]:


# it includes example with user input

def reverse_of_array(arr):
  reverse = arr[::-1]
  print("The reverse of the string is: ", reverse)
  return reverse


def main():
    arr = []
    n = int(input("Enter the number of elements in the array: ")) #user input
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)


    reverse_of_array(arr)

#given example
array = [2,4,6,4]
t1 = reverse_of_array(array)
print("------------------------------------")
main()# call for user input

