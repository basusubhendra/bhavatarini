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

def decompose(solution_vector):
    nn = ""
    for x in solution_vector:
        nn = nn + x
    return nn

if __name__ == "__main__":
    num = str(sys.argv[1]).lstrip().rstrip()
    triplets = characterize(num)
    multiplier = [ 10, 8 ]
    i = 0
    ll = len(triplets)
    solution_vector = []
    for x in triplets:
        for y in range(0, multiplier[i]):
            solution_vector.append(x)
        i = ( i + 1 ) % 2
    lx = len(solution_vector)
    posits = synthesize(solution_vector) 
    ctr = 0
    triplet1 = []
    triplet2 = []
    triplet3 = []
    nn = decompose(solution_vector)
    for x in list(zip(pi[:lx], nn, e[:lx][::-1])):
        triplet1.append(x[0])
        triplet2.append(x[1])
        triplet3.append(x[2])
        ctr = ctr + 1
        if ctr % 3 == 0:
            print(["".join(triplet1), "".join(triplet2), "".join(triplet3)])
            triplet1 = []
            triplet2 = []
            triplet3 = []
            ctr = 0
    print("")
    print("===================")
    print("")
    print(posits)
    
