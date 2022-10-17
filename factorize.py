#!/usr/bin/python3
import sys
from gmpy2 import *
from mpmath import *
from pi import *
from e import *

def characterize(num):
    ctr = 0
    l = len(num)
    triplets = []
    while ctr % l != 0 or ctr == 0:
         triplet = []
         zero_counter = 0
         for x in range(0, 3):
             nn = num[(ctr + x) % l]
             if nn == '0':
                 zero_counter = zero_counter + 1
             triplet.append(nn)
         triplet = "".join(triplet)
         triplets.append(triplet)
         ctr = ctr + (3 - (zero_counter % 3))
    return triplets
        
if __name__ == "__main__":
    num = str(sys.argv[1])
    print(num)
    triplets = characterize(num)
    print(triplets)
