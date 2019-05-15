#calculates chance of getting [arg 2] or more 6's when rolling [arg 1] amount of dice

import sys
import operator as op
from functools import reduce


def chanceOfN6(n,amnt,t):
    singleFailOutcomes = (t-1)**(amnt-n)
    singlePassOutcomes = (7-t)**(n)
    failCombos = ncr(amnt,amnt-n)
    passCombos = ncr(amnt,n)
    output = ((singleFailOutcomes * failCombos)+(singlePassOutcomes*passCombos))/(6**amnt)
    return output

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

amnt = int(sys.argv[1])
dif = int(sys.argv[2])
thresh = int(sys.argv[3])

output = sum([chanceOfN6(i,amnt,thresh) for i in range (dif,amnt+1)])
print("answer",output)