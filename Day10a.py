def coordsInList(coords = [0,0], coordList = [[0,0]]):
    coords=coords[0]
    for coord in coordList:
        if coord[0] == coords[0] and coord[1] == coords[1]:
            return True
    return False

def mapTrails(trails,input):
    newTrails = []
    for trail in trails:
        stepCoords = trail[len(trail)-1]
        stepVal = int(input[stepCoords[0]][stepCoords[1]])
        if stepCoords[0]-1 >= 0:
            if int(input[stepCoords[0]-1][stepCoords[1]]) == stepVal + 1:
                newTrails += [trail + [[stepCoords[0]-1,stepCoords[1]]]]
        if stepCoords[0]+1 < len(input):
            if int(input[stepCoords[0]+1][stepCoords[1]]) == stepVal + 1:
                newTrails += [trail + [[stepCoords[0]+1,stepCoords[1]]]]
        if stepCoords[1]-1 >= 0:
            if int(input[stepCoords[0]][stepCoords[1]-1]) == stepVal + 1:
                newTrails += [trail + [[stepCoords[0],stepCoords[1]-1]]]
        if stepCoords[1]+1 < len(input[stepCoords[0]]):
            if int(input[stepCoords[0]][stepCoords[1]+1]) == stepVal + 1:
                newTrails += [trail + [[stepCoords[0],stepCoords[1]+1]]]
    if len(newTrails) == 0:
        return None
    if stepVal == 8:
        return newTrails
    else:
        return mapTrails(newTrails, input)

import importer
input = importer.parseInput(0)

trailheads = []
for row in range(0,len(input)):
    for col in range(0,len(input[row])):
        if int(input[row][col]) == 0:
            trailheads += [[row,col]]

answer = 0
for trailhead in trailheads:
    trails = mapTrails([[trailhead]], input)
    if not trails == None:
        trails = [x[-1:] for x in trails]
        nines = []
        for trail in trails:
            if not coordsInList(trail,nines):
                nines += trail
                answer += 1

print(answer)