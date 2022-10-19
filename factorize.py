#!/usr/bin/python3

import sys
from generate_output import *

def characterize(num):
    ctr = 0
    l = len(num)
    if l <= 3:
        return [num]
    triplets = []
    while (ctr + 3) <= l:
        triplets.append(num[ctr:(ctr + 3)])
        ctr = ctr + 1
    return triplets

if __name__ == "__main__":
    num = str(sys.argv[1])
    triplets = characterize(num)
    print(triplets)
    multiplier = [ 8, 10, 1 ]
    i = 0
    ll = len(triplets)
    solution_vector = []
    for x in triplets[::-1]:
        for y in range(0, multiplier[i]):
            solution_vector.append(x)
        i = ( i + 1 ) % 3
    solution_vector = solution_vector[::-1]
    lx = len(solution_vector)
    posits = synthesize(solution_vector) 
    print(solution_vector)
    print(posits)
    print(pi[:len(solution_vector)])
    print(e[:len(solution_vector)][::-1])
#    factor1, factor2 = analyze(posits, solution_vector)
    
