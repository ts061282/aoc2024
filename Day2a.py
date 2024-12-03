import importer
input = importer.parseInput(0)

answer = 0

for line in input:
    levels = [int(x) for x in line.split(" ")]
    safety = 1
    increasing = levels[0] < levels[1]
    for level in range(0,len(levels)):
        if not level+1==len(levels): #if this isn't the last level
            if not ((levels[level] < levels[level+1] and increasing) or (levels[level] > levels[level+1] and not increasing)):
                safety = 0
                break
            levelStep = abs(levels[level]-levels[level+1])
            if levelStep < 1 or levelStep > 3:
                safety = 0
                break
    answer += safety

print(answer)