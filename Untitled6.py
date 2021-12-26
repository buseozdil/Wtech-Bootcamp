#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open("poem.txt","r")
say = 0

for dize in f:
    if dize != "\n":
        say += 1

f.close()

print(say)


# In[3]:


with open("poem.txt", "r") as input:
      
    with open("new.txt", "w") as output:
        for dize in input:
            output.write(dize[0]+"\n")

with open("new.txt", "r") as f:
    dizeler=f.read()

print (dizeler)

