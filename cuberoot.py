# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:05:11 2019

@author: Aman Aadi
"""

import numpy as np
num=int(input(""))
r=abs(num)
a=np.arange(0,r,0.0001)
g=a**3-r
b=np.argmin(np.abs(g))
result = a[b] if num==r else -1*a[b]
print(result)