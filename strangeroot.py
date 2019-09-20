# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:57:27 2019

@author: Aman Aadi
"""

def strroot(n):
    for i in str(round(n**(1/2),3)):
        if i in str(n**2):
            return True
    else:
        return False

print(strroot(int(input("Enter num to check: "))))