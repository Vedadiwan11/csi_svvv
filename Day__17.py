#!/usr/bin/env python
# coding: utf-8

# **Given a string, remove duplicate characters and return the reulting string**

# In[3]:


def Duplicate(str):
  t = " "
  for i in str:
    if (i in t):
      pass
    else:
      t= t+i
  return t



def main():
  string = input("enter the words:")
  new_str = Duplicate(string)
  print("The resulting string would be:",new_str)

main()


# In[ ]:




