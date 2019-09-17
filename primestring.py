# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:31:20 2019

@author: Aman Aadi
"""
import re

def primstr(s):
    for i in range(1,(len(s)//2)+1):
        patt=r'^({})+$'.format(s[:i])
        if re.search(patt,s[i:]):
            return True
    else:
        return False

print(primstr("abac"))