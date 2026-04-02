# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:54:28 2026

@author: ACER
"""

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
       print(j, end=" ")
print()