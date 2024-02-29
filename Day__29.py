#!/usr/bin/env python
# coding: utf-8

# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# In[1]:


def isValid(s: str) -> bool:
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or brackets_map[char] != stack.pop():
                return False
        else:
            return False
    
    return len(stack) == 0

# Test cases
print(isValid("()"))  
print(isValid("()[]{}")) 
print(isValid("(]"))  
print(isValid("([)]"))
print(isValid("{[]}"))


# In[ ]:




