#!/usr/bin/python3

import sys
from mpmath import *

if __name__ == "__main__":
    num = str(sys.argv[1]).lstrip().rstrip()
    num = num.lstrip().rstrip()
    f=open("pi.txt","r")
    g=open("e.txt","r")
    mp.prec=128
    mp.dps=128
    k=open("./pi_output.txt","w")
    h=open("./output.txt","w")
    m=open("./e_output.txt","w")
    ee = ""
    l = len(num)
    ctr = 0
    while True:
        a=int(f.read(1))
        c=int(num[ctr])
        b=int(g.read(1))
        ee = ee + str(b)
        index = a*10 + b
        if index == 0:
            index = 100
        zero = str(zetazero(index).imag)
        idx = zero.index(".")
        zero = zero[(idx-2):]
        zero = zero.replace(".","")
        zero = zero[:11]
        digit = zero[c-1]
        h.write(str(digit) + ",")
        k.write(str(a) + ",")
        ctr = ctr + 1
        if ctr == l:
            break
    ee = ee[::-1]
    for x in ee:
        m.write(str(x) + ",")
    k.write("\n")
    h.write("\n")
    m.write("\n")
    k.close()
    h.close()
    m.close()
    f.close()
    g.close()
