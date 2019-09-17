# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:58:28 2019

@author: Aman Aadi
"""

def isprime(n):
    assert (n>1),"Lol bad number"
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False

def isemirp(n):
    assert (n>1),"Lol bad number"
    result = True if isprime(n) and isprime(int(str(n)[::-1])) else False
    return result

print(isemirp(int(input("Enter to check: "))))

#BONUS

def isemirprange(start,end):
    l=[]
    for i in range(start,end+1):
        if isemirp(i):
            l.append(i)
    return l

print(isemirprange(int(input("Enter start: ")),int(input("Enter end: "))))