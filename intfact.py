#!/usr/bin/python3

import sys
import redis

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
    idx = 0
    while True:
        pos = 1
        while True:
            _cc = []
            _dd = []
            hit = 0
            counter = 0
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
                if idx == 0 and ctr == 3:
                    break
                elif idx == 1 and ctr == 10:
                    break
            __dd = []
            _dd = _dd[::-1]
            for x in _dd:
                __dd.append(x[::-1])
            _dd = __dd
            for zz in list(zip(_cc, _dd)):
                t = 0
                for xx in list(zip(zz[0], zz[1])):
                    if xx[0] == num[counter % l] or xx[1] == num[counter % l]:
                        if satisfies(xx[0], xx[1]) == True:
                            counter = counter + 1
                            if t < 2:
                                continue
                            else:
                                hit = hit + 1
                                print("hit")
                    t = t + 1
            hash_map[pos] = hit
            input([pos, hit])
            pos = pos + 1
        idx = idx + 1
        f.close()
        g.close()


