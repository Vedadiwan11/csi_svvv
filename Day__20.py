#!/usr/bin/env python
# coding: utf-8

# **Given a string, containing a mix of uppercase and lowercase, toggle the  case of each character**
# 

# In[6]:


def toggle_char(string):
  toggle_string = ""
  for char in string:
    if char.islower():
      toggle_string += char.upper()
    else:
      char.isupper()
      toggle_string += char.lower()

  return toggle_string



def main():
  string = input("enter the words:")
  str1 = toggle_char(string)

  print("The output would be:",str1)


main()


# In[ ]:




