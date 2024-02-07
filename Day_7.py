#!/usr/bin/env python
# coding: utf-8

# In[3]:


#write a program to find the sum of all elements in an array.

array = [2, 4, 6, 4] # given example

print("The sum is:", end=" ")
sum= 0
for i in array:
  sum = sum +i

print(sum)



# In[5]:


# it includes example with user input

def sum_in_array(arr):
    print("The sum is:", end=" ")
    sum= 0
    for i in array:
      sum = sum +i
    print(sum)

def main():
    arr = []
    n = int(input("Enter the number of elements in the array: ")) #user input
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)


    sum_in_array(arr)

#given example
array = [2,4,6,4]
t1 = sum_in_array(array)
print("------------------------------------")
main()# call for user input


# In[ ]:




