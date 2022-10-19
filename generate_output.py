#!/usr/bin/python3
import sys
from pi import pi
from e import e

def synthesize(solution_vector):
    ll = len(solution_vector)
    pp = pi[:ll]
    ee = e[:ll]
    position = 0
    posits = []
    for x in list(zip(pp, solution_vector, ee)):
        if x[0] == '0' or x[1] == '0' or x[2] == '0':
            pass
        elif int(x[0]) < int(x[1]) and int(x[2]) < int(x[1]):
            posits.append(position)
        elif int(x[0]) > int(x[1]) and int(x[2]) > int(x[1]):
            posits.append(position)
        else:
            pass
        position = position + 1
    return posits

def analyze(posits, solution_vector):
    ll = len(solution_vector)
    pp = pi[:ll]
    ee = e[:ll][::-1]
    for x in list(zip(pp, solution_vector, ee)):
        pass
        """
        elif x[0] == x[2] and int(x[1]) < int(x[0]) and int(x[1]) < int(x[2]):
            posits.append(-position)
        elif x[0] == x[2] and int(x[1]) > int(x[0]) and int(x[1]) > int(x[2]):
            posits.append(-position)
            """
