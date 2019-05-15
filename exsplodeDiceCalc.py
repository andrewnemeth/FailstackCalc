from random import randint
from collections import Counter
import collections
import csv
sampleConut = 1000000
poolRange = (1,8)
NUM_DECIMAL = 5

def rollDie():
    hits = 0
    roll = randint(1,6)
    if(roll > 3):
        hits = hits+1
    if(roll == 6):
        hits += rollDie()

    return hits

def rollPool(num):
    return sum([rollDie() for x in range(num)])


def statsForPoolSice(poolsize):
    output = Counter([rollPool(poolsize) for x in range(sampleConut)])
    del output[0]
    for key in output:
        output[key] = (output[key]*100)/sampleConut

    output = collections.OrderedDict(sorted(output.items()))

    chancePerVal = [output[key] for key in output]
    chanceAtLeastVal = [round(sum([chancePerVal[i] for i in range(j,len(chancePerVal))]),NUM_DECIMAL) for j in range (0, len(chancePerVal))]
    return chanceAtLeastVal


allData = [statsForPoolSice(x) for x in range (1,9)]
with open ("rollData.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter='\t',quoting=csv.QUOTE_MINIMAL)
    writer.writerows(allData)