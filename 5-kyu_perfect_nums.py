'''
URL: https://www.codewars.com/kata/54d4c8b08776e4ad92000835

Destricption: 

A perfect power is a classification of positive integers:

In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer.
More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.

Examples
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
'''

from math import log, sqrt

def isPP(n):
    n = int(n)
    
    if n < 4:
        return None
        
    num1 = round(sqrt(n), 3)

    if num1 == round(num1):
        return [int(num1), 2]

    for i in range(2, n//2):
        k = round(log(n)/log(i), 6)
        
        if k == round(k):
            return [i, int(k)]
            
    return None
