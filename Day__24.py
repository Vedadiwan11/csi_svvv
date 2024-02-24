#!/usr/bin/env python
# coding: utf-8

# # Write a recursive Function to check whether a given string is palindrome or not

# In[3]:


def Is_palindrome(s):
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Check if the first and last characters are the same
    elif s[0] == s[-1]:
        # Recur for the substring excluding the first and last characters
        return Is_palindrome(s[1:-1])
    else:
        # If the first and last characters are different, it's not a palindrome
        return False

string = input("Enter a string: ")
if Is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")


# In[ ]:




