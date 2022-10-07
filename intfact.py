#!/usr/bin/python3

import sys
import redis
from zeros import *

def satisfies(x, y):
    x = int(x)
    y = int(y)
    if x == 0 or y == 0:
        return False
    if x == y:
        return False
    odd_X = x % 2
    odd_Y = y % 2
    if odd_X*odd_Y == 0 and odd_X != odd_Y:
        return True
    else:
        return False
    return False

if __name__ == "__main__":
    num = str(sys.argv[1])
    l = len(num)
    server = redis.Redis(host='localhost',port='6379',db=0)
    counter = 0
    first = True
    prev_pos = -1
    while True:
        pos = 1
        while True:
            _cc = []
            _dd = []
            hash_map = dict([])
            f = open("./pi.txt","r")
            g = open("./e.txt","r")
            ctr = 0
            while ctr < pos:
                c = str(f.read(12))
                d = str(g.read(12))
                _cc.append(c)
                _dd.append(d)
                ctr = ctr + 1
                if pos == 1 and ctr == 3:
                    break
                elif pos == 2 and ctr == 10:
                    break
            __dd = []
            _dd = _dd[::-1]
            for x in _dd:
                __dd.append(x[::-1])
            _dd = __dd
            for zz in list(zip(_cc, _dd)):
                for xx in list(zip(zz[0], zz[1])):
                    if xx[0] == num[(pos - 1) % l] or xx[1] == num[(pos - 1) % l]:
                        if satisfies(xx[0], xx[1]) == True:
                            counter = counter + 1
            hash_map[(pos - 1) % l] = counter
            print([pos, counter, pos % l])
            if first == True and counter in zeros:
                first = False
                counter = 0
                prev_pos = (pos - 1) % l
                break
            y = ""
            if first == False:
                y = str(input("?"))
            if y == 'y':
               counter = 0
               break
            pos = pos + 1
            counter = 0
        f.close()
        g.close()


