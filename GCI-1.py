
# coding: utf-8

# In[21]:


for _ in range(10):
    print("GCI is great")
name = input("What's your name? ")
name = list(name)
revName = name[::-1]
print("Hi " + name + ", nice to meet you! Did you know that your name spelled backwards is " + revName + "?")

