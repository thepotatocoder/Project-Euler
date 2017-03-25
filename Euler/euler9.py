
from __future__ import print_function
from math import sqrt

"""
A**2 + B**2 = C**2
A + B + C = NUM
"""
NUM = 1000

A = 1
B = 1
C = 0

while A < NUM:
    while B < NUM:
        C = sqrt(A**2 + B**2)
        if A + B + C == NUM:
            print('A: {0}, B: {1}, C: {2}, R: {3}'.format(A, B, C, A*B*C))
        B += 1
    A += 1
    B = 1
