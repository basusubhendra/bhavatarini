#!/usr/bin/python3
import sys
from pi import pi
from e import e
from rsa2048 import num
#num = str(sys.argv[1])
n=num*8
ll = len(n)
pp = pi[:ll]
ee = e[:ll]
l = len(num)
position = 0
posits = []
n = num*8
for x in list(zip(pp, n, ee)):
    if x[0] == '0' or x[1] == '0' or x[2] == '0':
        pass
    elif x[0] == x[2] and int(x[1]) < int(x[0]) and int(x[1]) < int(x[2]):
        posits.append(-position)
    elif x[0] == x[2] and int(x[1]) > int(x[0]) and int(x[1]) > int(x[2]):
        posits.append(-position)
    elif int(x[0]) < int(x[1]) and int(x[2]) < int(x[1]):
        posits.append(position)
    elif int(x[0]) > int(x[1]) and int(x[2]) > int(x[1]):
        posits.append(position)
    else:
        pass
    position = position + 1
ee = ee[::-1]
