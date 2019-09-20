# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:02:02 2019

@author: Aman Aadi
"""

import matplotlib.pyplot as plt
t1=eval(input("Enter (x1,y1): "))
t2=eval(input("Enter (x2,y2): "))

plt.plot([t1[0],t2[0]],[t1[1],t2[1]])
plt.title("TWO POINTS")

distance=((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2)**(1/2)
print(distance)
plt.show()