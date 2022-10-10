#!/usr/bin/python3
import sys
f=open("./pi.txt","r")
g=open("./_pi.txt","w")
f.read(2)
g.write("3")
c=str(f.read(98))
g.write(c)
while True:
    c=str(f.read(100))
    if not c or c == "" or len(c) == 0:
        break
    g.write(str(c))
g.close()
f.close()
