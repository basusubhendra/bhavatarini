#!/usr/bin/python3
f=open("./zeros6","r")
lines=f.readlines()
g=open("zeros.py","w")
g.write("zeros=[")
for l in lines:
    ss = str(l).lstrip().rstrip()
    idx = ss.index(".")
    ss = ss[:idx]
    g.write(str(ss))
    if l != lines[-1]:
       g.write(",")
g.write("]")
g.close()
f.close()
