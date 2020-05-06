'''
Description:

Write funcion that calculate algorytm fibonacci and can handle numbers ever 50. 
'''
#Solution:

import functools
@functools.lru_cache(None)

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

