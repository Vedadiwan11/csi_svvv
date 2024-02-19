#!/usr/bin/env python
# coding: utf-8

# **Given a string, find the first non-repeating characterr in it and return its index. If it doesn't exist return -1 **

# In[9]:


def first_non_repeated_char(string):
    if(len(string) == 0):
      print("EMTPY STRING")

    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(string):
        if char_count[char] == 1:
            return char,i

    return -1,-1

def main():
  string = input("enter the words:")
  char, index = first_non_repeated_char(string)

  if char!=-1:
    print("The chararcter is {} at the index {}:".format(char, index))
  else:
    print("There are no non-repeated characters in the input.")

main()

