#!/usr/bin/env python
# coding: utf-8

# # Implement a reucrsive function to find the sum of user given array

# In[2]:


def recursive_sum(arr, n):
    if n <= 0:
        return 0
    else:
        return arr[n - 1] + recursive_sum(arr, n - 1)

# Function to take user input for array elements
def take_user_input():
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)
    return arr

# Main function
def main():
    arr = take_user_input()
    total_sum = recursive_sum(arr, len(arr))
    print("Sum of the array elements:", total_sum)

if __name__ == "__main__":
    main()

