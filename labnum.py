# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:24:09 2019

@author: Aman Aadi
"""

def labnum(n):
    assert n>=2,"Ya dumdum!"
    for i in range(2,n//2+1):
        if n%i==0 and n%(i**2)==0:
            return True
    else:
        return False

print(labnum(int(input("Enter number to test: "))))

#BONUS

def labnumrange(start,end):
    l=[]
    for i in range(start,end+1):
        if labnum(i):
            l.append(i)
    return l

print(labnumrange(int(input("Enter start: ")),int(input("Enter end: "))))