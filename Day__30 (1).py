#!/usr/bin/env python
# coding: utf-8

# In[2]:


def generate_personalized_message(name, feedback):
    message_template = """
Hello {name},

Thank you for providing your insights. We're thrilled to learn about your journey and the significant lessons acquired throughout the 30 Days of Code challenge. Your commitment and passion have truly been motivating. Best of luck in all your future coding pursuits!

Warm regards,

"""

    personalized_message = message_template.format(name=name, feedback=feedback)
    return personalized_message


def main():
    # Prompt user for name and feedback
    name = input("Enter your name: ")
    feedback = input("Share your 30-day journey experience and what you've learned: ")

    # Generate and display personalized message
    message = generate_personalized_message(name, feedback)
    print(message)


if __name__ == "__main__":
    main()


# In[ ]:




