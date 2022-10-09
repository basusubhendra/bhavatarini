#!/usr/bin/python3

import sys
from zeros import zeros

def characterize(num):
    tuples = []
    ctr = 0
    l = len(num)
    while ctr < l - 1:
        tuples.append(num[ctr] + num[ctr + 1])
        ctr = ctr + 1
    return tuples

def _deriveRelation_(x, y):
    x = int(x)
    y = int(y)
    if x == y and x == 0:
        return 5
    elif x == 0:
        return 4
    elif y == 0:
        return 3
    elif x == y:
        return 2
    elif x > y:
        return 1
    elif x < y:
        return 0
    return - 1

def deriveRelation(tt):
    _relations_ = []
    for x in tt:
        _relations_.append(_deriveRelation_(x[0], x[1]))
    return _relations_

f=open("./pi.txt","r")
g=open("./e.txt","r")
x=10
y=10
num = str(sys.argv[1])
tuples = characterize(num)
_relations_ = deriveRelation(tuples)
idx1=0
idx2=0
_z_=int(sys.argv[2])
z = int(zeros[_z_-1])
pp=str(f.read(z*x*y))
ee=str(g.read(z*x*y))[::-1]
ctr = 0
counter = 0
zero_cnt = 0
one_cnt = 0
ll = len(_relations_)
while ctr < (x*y):
    _pp_ = pp[ctr] + pp[ctr + 1]
    _ee_ = ee[ctr] + ee[ctr + 1]
    px = int(_pp_)
    ex = int(_ee_)
    success1 = False
    success2 = False
    if _relations_[idx1 % ll] == _deriveRelation_(pp[ctr], pp[ctr + 1]):
        success1 = True
        idx1 = idx1 + 1
    if _relations_[idx2 % ll] == _deriveRelation_(ee[ctr], ee[ctr + 1]):
        success2 = True
        idx2 = idx2 + 1
    if success1 == True and success2 == True:
        if counter == 0 or counter == 1 or counter == 8 or counter == 9:
            zero_cnt = zero_cnt + 1
        elif counter == 2 or counter == 3 or counter == 4 or counter == 5 or counter == 6 or counter == 7:
            one_cnt = one_cnt + 1
    ctr = ctr + 2
    counter = (counter + 1) % 10
print(zero_cnt)
print(one_cnt)
f.close()
g.close()
