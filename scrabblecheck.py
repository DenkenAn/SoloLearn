# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:10:23 2019

@author: Aman Aadi
"""

score={("e","a","i","o","u","n","r","t","l","s","u"):1,("d","g"):2,("b","c",
       "m","p"):3,("f","h","v","w","y"):4,("k"):5,("j","x"):8,("q","z"):10}

def scoreme(s):
    tot=0
    for i in s:
        for j in score.keys():
            if i.lower() in j:
                tot+=score[j]
                break
    return tot

l=eval(input("Enter list of words [w1,w2,w3]: "))

best=0
bestboi="Not a choice"
for i in l:
    if scoreme(i)>best:
        best=scoreme(i)
        bestboi=i

print(bestboi,best)