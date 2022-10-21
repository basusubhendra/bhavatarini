#!/usr/bin/python3
import sys
f=open("./pi.txt","r")
g=open("./pp_zeros.txt","w")
ctr = 2
while True:
    c=str(f.read(1))
    if not c or c == "" or len(c) == 0:
        break
    if c == '0':
        g.write(str(ctr)+",")
        ctr = 1
    ctr = ctr + 1
g.close()
f.close()
