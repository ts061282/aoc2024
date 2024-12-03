def evaluateSubLevels(levels = [1,2,3,4]):
    increasing = levels[0] < levels[1]
    for level in range(0,len(levels)):
        if not level+1==len(levels): #if this isn't the last level
            if not ((levels[level] < levels[level+1] and increasing) or (levels[level] > levels[level+1] and not increasing)):
                return False
            levelStep = abs(levels[level]-levels[level+1])
            if levelStep < 1 or levelStep > 3:
                return False
    return True

def evaluateLevels(levels = [1,2,3,4,5]):
    increasing = levels[0] < levels[1]
    evaluateSubs = False
    for level in range(0,len(levels)):
        if not level+1==len(levels): #if this isn't the last level
            if not ((levels[level] < levels[level+1] and increasing) or (levels[level] > levels[level+1] and not increasing)):
                evaluateSubs = True
                break
            levelStep = abs(levels[level]-levels[level+1])
            if levelStep < 1 or levelStep > 3:
                evaluateSubs = True
                break
    if not evaluateSubs:
        return True
    else:
        sublevels = []
        for level in range(0,len(levels)):
            sublevel = []
            for lev in range(0,len(levels)):
                if not lev == level:
                    sublevel += [levels[lev]]
            sublevels += [sublevel]
        safe = False
        for slevel in sublevels:
            safe = safe or evaluateSubLevels(slevel)
        if safe: print(levels)
        return safe

import importer
input = importer.parseInput(0)

answer = 0

for line in input:
    levels = [int(x) for x in line.split(" ")]
    if evaluateLevels(levels):
        answer += 1

print(answer)