#!/usr/bin/env python3
from numpy import loadtxt
array=loadtxt(open("sudoku2.txt"),delimiter=",",dtype=int)

def chk(check):         #Check for sorted list of 1-9
    if sorted(check)==[1,2,3,4,5,6,7,8,9]:return True
    else:return False

for h in range(9):       #Horizntal check
    Pass=chk(array[h])

for v in range(9):       #Vertical check
    check=[]
    for h in range(9):
        check.append(array[h][v])
    Pass=chk(check)

for hh in range(3):     #3x3 grid check
    for vv in range(3):
        check=[]
        for h in range(hh*3,hh*3+3):
            for v in range(vv*3,vv*3+3):
                check.append(array[h][v])
        Pass=chk(check)

if Pass:print("Yes")  #Check for Full Pass
else:print("No")
