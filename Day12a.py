def getPerim(region = [[0,0]]):
    perim = 0
    for plot in region:
        if not [plot[0]-1,plot[1]] in region:
            perim += 1
        if not [plot[0]+1,plot[1]] in region:
            perim += 1
        if not [plot[0],plot[1]-1] in region:
            perim += 1
        if not [plot[0],plot[1]+1] in region:
            perim += 1        
    return perim

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
    answer += len(region[0]) * getPerim(region[0])

print(answer)