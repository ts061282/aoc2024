def turnFacing(facing = [-1,0]):
    if facing[0] == 0:
        facing[0] = -1 * facing[1]
        facing[1] = 0
    else:
        facing[1] = -1 * facing[0]
        facing[0] = 0
    return facing

import importer
input = importer.parseInput(1)

onMap = True
path = []
facing = [-1,0]
position = [-1,-1]
for line in range(0,len(input)):
    try:
        position = [line,input[line].index('^')]
        break
    except:
        next

while onMap:
    path.append(position)
    if input[position[0]+facing[0]][position[1]+facing[1]] == '#':
        facing = turnFacing(facing)
    else:
        position = [position[0] + facing[0], position[1]+facing[1]]
        if position[0] < 0 or position[0] >= len(input[0]) or position[1] < 0 or position[1] >= len(input):
            onMap = False

answer = 0
for n in range(0,len(path)):
    if(path.pop not in path):
        answer += 1

print(answer)