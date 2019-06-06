#!/usr/bin/env python
# coding: utf-8

# In[25]:


Num_cmd = int(input())
i = 0
namespaces={
    'global': {'parent':None, 'vars':[]},
}

def getName(x, c):
        a = namespaces.get(c)
        b = a.get('vars')
        if x in b:  
            return c
        else:
            c = a.get('parent')
            if c == None:
                return None
            else:            
                return getName(x, c) 
        

while i < Num_cmd:
    cmd, name, arg = input().split()
    
    if cmd == 'add':
        a = namespaces.get(name)
        b = a.get('parent')
        c = a.get('vars')
        c.append(arg)
        dictionary = dict.fromkeys([name], {'parent':b,'vars':c})
        namespaces.update(dictionary)     
    
    elif cmd == 'get':
        print(getName(arg, name))       
    
    elif cmd == 'create':
        if arg in namespaces:
            dictionary = dict.fromkeys([name], {'parent':arg, 'vars':[]})              
            namespaces.update(dictionary)    
    i += 1


# In[ ]:





# In[ ]:





# In[ ]:




