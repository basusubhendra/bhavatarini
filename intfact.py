#!/usr/bin/python3
import sys

def satisfies(x, y):
    x = int(x)
    y = int(y)
    odd_X = x % 2
    odd_Y = y % 2
    if odd_X * odd_Y == 0 and odd_X != odd_Y:
        return True
    else:
        return False
    return False

if __name__ == "__main__":
    num = str(sys.argv[1])
    f=open("./pi.txt","r")
    g=open("./e.txt","r")
    ctr = 0
    l = len(num)
    idx = 0
    ltr = ""
    rtr = ""
    t = 0
    accumulator = 0
    while True:
        c=str(f.read(12))
        d=str(g.read(12))
        c=c[2:]
        d=d[2:]
        success = False
        for x in list(zip(c,d)):
            if satisfies(x[0],x[1]) and (x[0] == num[ctr % l] or x[1] == num[ctr % l]):
                ctr = ctr + 1
                success = True
        if success == True:
            accumulator = accumulator + 1
        if ctr % 3 == 0:
            if t == 0 and accumulator > 0:
                input([ctr, accumulator])
                ltr = ltr + bin(accumulator)[2:][::-1]
                accumulator = 0
                idx = idx + 1
                if idx == 3:
                    idx = 0
                    t = 1 - t
            elif t == 1 and accumulator > 0:
                input([ctr,accumulator])
                rtr = rtr + bin(accumulator)[2:][::-1]
                accumulator = 0
                idx = idx + 1
                if idx == 3:
                    idx = 0
                    t = 1 - t
    f.close()
    g.close()
