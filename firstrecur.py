# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:11:34 2019

@author: Aman Aadi
"""

def firstrecur(s):
    d={}
    for i in s.upper():
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        if 2 in d.values():
            for j in d:
                if d[j]==2:
                    return j
    else:
        return "NONE OF EM"

print(firstrecur(input("Enter string to check: ")))