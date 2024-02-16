#!/usr/bin/env python
# coding: utf-8

# **Given a string, reverse the characters in the string**

# In[2]:


def Reverse(str):
  return str[::-1]

def main():
  string = input("enter the words:")
  new_str = Reverse(string)
  print("The reverse of string is:",new_str)

main()


# In[ ]:




