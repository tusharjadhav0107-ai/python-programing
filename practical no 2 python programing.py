# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  print("Leap Year")
else:
    print("Not a Leap Year")
