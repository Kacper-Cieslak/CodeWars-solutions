'''
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
'''

# Solution:

import numpy as np

class Vector(np.ndarray):
    def __new__(cls, input_array, info=None):
        return np.asarray(input_array).view(cls)
    
    def __str__(self):
        return "({})".format(",".join([str(i) for i in self]))

    def add(self, v2):
        return self + v2

    def dot(self, v2):
        return sum(s * o for s, o in zip(self, v2))

    def equals(self, v2):
        return np.all(self == v2)

    def norm(self):
        return sum(f ** 2 for f in self) ** 0.5

    def subtract(self, v2):
        return self - v2
