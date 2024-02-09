#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Implement Linear Search Algorithm to find an elemnet in an array

array = [2,4,6,4] #given example
t = 6
for i in range(len(array)):
  if(array[i]==t):
    print("element is present at the index: ",i )


# In[1]:


def Linear_search(arr,num):
  for i in range(len(arr)):
    if arr[i] == num:
      return i
  return -1

def main():
    arr = []
    n = int(input("Enter the number of elements in the array: ")) #user input
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    num = int(input("element to be searched: "))


    t2 = Linear_search(arr, num)
    if t2!=-1:
      print("The element",num, "is found at :",t2)
    else:
      print("The element",num," not found ")

array = [2,4,6,4]
num =6
t= Linear_search(array,num)
if t!=-1:
  print("The element",num, "is found at :",t)
else:
  print("The element",num," not found ")

main()


# In[ ]:




