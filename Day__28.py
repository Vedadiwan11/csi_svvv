#!/usr/bin/env python
# coding: utf-8

# Covert roman number into integer

# In[1]:


def romanToInt(s: str) -> int:
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_to_int[char]
        if value > prev_value:
            total += value - 2 * prev_value  # Subtract twice the previous value
        else:
            total += value
        prev_value = value
    
    return total

# Test cases
print(romanToInt("III"))     
print(romanToInt("LVIII"))   
print(romanToInt("MCMXCIV")) 


# In[ ]:




