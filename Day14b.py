import importer
import os
input = importer.parseInput(0)

positions = []
velocities = []

for line in input:
    
    splitline = line.split(" ")
    
    p = splitline[0].split("=")[1]
    p = p.split(",")
    p = [int(i) for i in p]
    positions += [[p[1],p[0]]]

    v = splitline[1].split("=")[1]
    v = v.split(",")
    v = [int(i) for i in v]
    velocities += [[v[1],v[0]]]

space = [103,101]

seconds = 0
safetyFactor = 0
safetyMin = 322752530 #arbitrarily larger than noise safety factors
safteyMax = 0
while True:
    seconds += 1
    for robot in range(0,len(positions)):
        positions[robot][0] += velocities[robot][0]
        positions[robot][1] += velocities[robot][1]
        positions[robot][0] = positions[robot][0] % space[0]
        positions[robot][1] = positions[robot][1] % space[1]

    quadrants = [[0,0],[0,0]]
    for robot in range(0,len(positions)):
        halfwidth = int((space[1]-1)/2)
        halfheight = int((space[0]-1)/2)
        if positions[robot][0] < halfheight:
            if positions[robot][1] < halfwidth:
                quadrants[0][0] += 1
            elif positions[robot][1] > halfwidth:
                quadrants[0][1] += 1
        elif positions[robot][0] > halfheight:
            if positions[robot][1] < halfwidth:
                quadrants[1][0] += 1
            elif positions[robot][1] > halfwidth:
                quadrants[1][1] += 1

    safetyFactor = quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]

    if safetyFactor == 105255744: #outlier safety factor 
        answer = seconds
        break

    #initially ran this code to find an outlier, as a pictogram is more highly ordered than random positions, the safety factor from part one was a hint towards this and was an effective measure
    #if safetyFactor > safteyMax: safteyMax = safetyFactor 
    #if safetyFactor < safetyMin: safetyMin = safetyFactor

    #print(safetyMin, ", ", safteyMax)

print(answer)