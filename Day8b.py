def calcNodes(stationA = [0,0], stationB = [0,0], mapWidth = 0, mapHeight = 0):
    nodesOnMap = []
    offset = [stationB[0]-stationA[0],stationB[1]-stationA[1]]
    lowDenom = min(abs(offset[0]),abs(offset[1]))
    maxIter = math.ceil(mapWidth/lowDenom)
    for x in range(0,maxIter):
        if (stationA[0] - x*offset[0] >= 0 and stationA[0] - x*offset[0] <= mapWidth):
            if (stationA[1] - x*offset[1] >= 0 and stationA[1] - x*offset[1] <= mapHeight):
                nodesOnMap += [[stationA[0] - x*offset[0],stationA[1] - x*offset[1]]]
        if (stationB[0] + x*offset[0] >= 0 and stationB[0] + x*offset[0] <= mapWidth):
            if (stationB[1] + x*offset[1] >= 0 and stationB[1] + x*offset[1] <= mapHeight):
                nodesOnMap += [[stationB[0] + x*offset[0],stationB[1] + x*offset[1]]]
    return nodesOnMap

import importer
import math
input = importer.parseInput(0)

frequencies = {}
for line in range(0,len(input)):
    for char in range(0,len(input[0])):
        if input[line][char].isalpha() or input[line][char].isdigit():
            if not input[line][char] in frequencies:
                frequencies.update({input[line][char]:[[line,char]]})
            else:
                frequencies.get(input[line][char]).append([line,char])

mapWidth = len(input)-1
mapHeight = len(input[0])-1
answer = 0
countedNodes = []
for frequency in frequencies:
    nodes = []
    for stationA in range(0,len(frequencies[frequency])-1):
        for stationB in range(stationA+1,len(frequencies[frequency])):
            for node in calcNodes(frequencies[frequency][stationA],frequencies[frequency][stationB],mapWidth,mapHeight):
                if not node in nodes:
                    nodes += [node]
    for node in nodes:
        if not node in countedNodes:
            answer += 1
    countedNodes += nodes

print(answer)