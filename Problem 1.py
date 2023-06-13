# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:55:40 2023
If we list all the natural numbers below 
10 that are multiples of 
3 or 5, we get 3,5,6,9. The sum of these multiples is 23
.

Find the sum of all the multiples of 3 or  5 below 1000
.

@author: ilean
"""
result = 0
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        result += i 
print(result)

