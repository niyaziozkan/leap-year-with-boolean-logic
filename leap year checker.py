#!/usr/bin/env python
# coding: utf-8

# In[ ]:


year = int(input("Please enter a 4-digit year: "))
divide_4 = year % 4
divide_100 = year % 100
divide_400 = year % 400
leap_year = (not divide_4 and not divide_100 and not divide_400) or             (bool(divide_100) and bool(divide_400) and bool(not divide_4))
print(leap_year)

