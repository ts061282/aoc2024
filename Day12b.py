def countSides(plots = {0:[0]}):
    sides = 0
    for key in plots.keys():
        plots[key].sort()
        sides += 1
        currentSide = plots[key][0]
        for side in range(1,len(plots[key])):
            if plots[key][side] != currentSide + 1:
                sides += 1
            currentSide = plots[key][side]
    return sides

def getSides(region = [[0,0]]):
    leftSides = {}
    rightSides = {}
    bottomSides = {}
    topSides = {}
    for plot in region:
        if not [plot[0]-1,plot[1]] in region:
            if not plot[0] in leftSides.keys():
                leftSides.update({plot[0]:[plot[1]]})
            elif not plot[1] in leftSides[plot[0]]:
                leftSides[plot[0]] += [plot[1]]
        if not [plot[0]+1,plot[1]] in region:
            if not plot[0] in rightSides.keys():
                rightSides.update({plot[0]:[plot[1]]})
            elif not plot[1] in rightSides[plot[0]]:
                rightSides[plot[0]] += [plot[1]]
        if not [plot[0],plot[1]-1] in region:
            if not plot[1] in topSides.keys():
                topSides.update({plot[1]:[plot[0]]})
            elif not plot[0] in topSides[plot[1]]:
                topSides[plot[1]] += [plot[0]]
        if not [plot[0],plot[1]+1] in region:
            if not plot[1] in bottomSides.keys():
                bottomSides.update({plot[1]:[plot[0]]})
            elif not plot[0] in bottomSides[plot[1]]:
                bottomSides[plot[1]] += [plot[0]]
    sides = countSides(leftSides) + countSides(rightSides) + countSides(topSides) + countSides(bottomSides)
    return sides

def findRegion(region = [[0,0]],garden = [['A'],['A']]):
    newPlots = False
    for plot in region:
        if plot[0]-1 >= 0:
            if garden[plot[0]-1][plot[1]] == garden[plot[0]][plot[1]]:
                if not [plot[0]-1,plot[1]] in region:
                    region.append([plot[0]-1,plot[1]])
                    newPlots = True
        if plot[0]+1 < len(garden[0]):
            if garden[plot[0]+1][plot[1]] == garden[plot[0]][plot[1]]:
                if not [plot[0]+1,plot[1]] in region:                
                    region.append([plot[0]+1,plot[1]])
                    newPlots = True
        if plot[1]-1 >= 0:
            if garden[plot[0]][plot[1]-1] == garden[plot[0]][plot[1]]:
                if not [plot[0],plot[1]-1] in region:                
                    region.append([plot[0],plot[1]-1])
                    newPlots = True
        if plot[1]+1 < len(garden[plot[0]]):
            if garden[plot[0]][plot[1]+1] == garden[plot[0]][plot[1]]:
                if not [plot[0],plot[1]+1] in region:                
                    region.append([plot[0],plot[1]+1])
                    newPlots = True
    if newPlots:
        return findRegion(region,garden)
    else:
        return region

import importer
input = importer.parseInput(0)

garden = [[char for char in line] for line in input]

regions = []
for row in range(0,len(garden)):
    for plot in range(0,len(garden[row])):
        accountedFor = False
        for region in regions:
            if [row,plot] in region[0]: accountedFor = True
        if not accountedFor:
            region = findRegion([[row,plot]],garden)
            regions.append([region])

answer = 0
for region in regions:
    answer += len(region[0]) * getSides(region[0])

print(answer)