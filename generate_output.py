#!/usr/bin/python3
import sys

num = str(sys.argv[1])
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

snippet1 = []
snippet2 =[]
snippet = []
position = 0
_snippet = snippet1
for x in list(zip(pp, n, ee)):
    if position + 1 in posits:
        _snippet.append("".join(x))
    elif -(position + 1) in posits:
        _snippet.append(str("-") + str("".join(x)))
    else:
        pass
    position = position + 1
    if position % (len(num)*4) == 0:
         _snippet = snippet2
         snippet.append(snippet1)
snippet.append(snippet2)
