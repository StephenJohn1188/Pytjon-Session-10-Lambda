#!/usr/bin/env python
# coding: utf-8

# # Map Function

# In[ ]:





# In[9]:


List=[1,2,3,4,5,6,7,8]
list(map(lambda x : x*2, List))


# In[12]:


C=[32.4, 33.8, 34.9, 35.67, 33.89]
F= list(map(lambda x : (9/5)*x + 32, C))
print(F)


# In[13]:


C=list(map(lambda x: (5/9)*(x-32), F))
print(C)


# In[14]:


newlistC= [round (x,2) for x in C]


# In[16]:


newlistC


# In[18]:


newlist = [ '%.2f' % j for j in C]
newlist


# # Filter in Lambda 

# In[20]:


listf = [1,2,3,4,5]
list(filter(lambda x : x>2, listf))


# In[21]:


even = lambda x: x%2 == 0
list(filter(even,range(11)))


# In[26]:


[x for x in range(11) if x%2 == 0]


# # Exception Handling

# In[28]:


7/0


# In[29]:


try:
    7/0
except ZeroDivisionError as err:
    print("Handling run time error: ", err)


# In[31]:


try:
   8*m+2
except NameError as err:
    print("Handling run time error: ", err)


# In[35]:


def div():
    a=3
    b=0
    c=3/0
    print(c)


# In[38]:


try:
   div()
except ZeroDivisionError as err:
    print("Handling run time error: ", err)


# In[53]:


def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print("The Result is: ", result)
    finally:
        print("executing finally clause")   


# In[55]:


divide(70,5)


# In[56]:


divide(2,0)

