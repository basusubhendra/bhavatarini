#!/usr/bin/python3
import sys

def satisfies(x, y):
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
        if (ctr + 1) % 3 == 0:
            if t == 0:
                input(bin(accumulator)[2:][::-1])
                ltr = ltr + bin(accumulator)[2:][::-1]
                accumulator = 0
                idx = idx + 1
                if idx == 3:
                    idx = 0
                    t = 1 - t
            elif t == 1:
                input(bin(accumulator)[2:][::-1])
                rtr = rtr + bin(accumulator)[2:][::-1]
                accumulator = 0
                idx = idx + 1
                if idx == 3:
                    idx = 0
                    t = 1 - t
    f.close()
    g.close()
