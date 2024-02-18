#!/usr/bin/env python
# coding: utf-8

# given a string,count the nuber of vowels and consonants in the string

# In[6]:


def count():
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    count_vowel = 0 
    count_consonants =0
    string = input("enter the words:")
    for i in string:
        if(i in vowels):
            count_vowel=count_vowel+1 
        else:
            count_consonants=count_consonants+1

    return count_vowel,count_consonants 
count_vowel,count_consonants =count()
print("number of vovels:",count_vowel)
print("number of consonants:",count_consonants)

