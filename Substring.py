# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:41:10 2020

@author: Eknath
"""
x = input("Enter a string")
y = input("Enter a string")
stack,i = [],0
while(len(stack)!=len(y)):
    if x[i] in y:
        stack.append(x[i])
    elif stack!=[] and i not in y:
        stack = []
    i= i +1
    if i==len(x):
        break
if len(stack)==len(y):
    print("Substring")
else:
    print("Not substring")


