# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:52:08 2026

@author: ACER
"""
n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
   fact = fact * i
print("Factorial:", fact)
