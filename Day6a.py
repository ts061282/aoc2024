def turnFacing(facing = [-1,0]):
    if facing[0] == 0:
        facing[0] = facing[1]
        facing[1] = 0
    else:
        facing[1] = -1 * facing[0]
        facing[0] = 0
    return facing

import importer
input = importer.parseInput(0)

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
    if not position in path:
        path.append(position)
    try:
        if input[position[0]+facing[0]][position[1]+facing[1]] == '#':
            facing = turnFacing(facing)
        else:
            position = [position[0] + facing[0], position[1]+facing[1]]
            if position[0] < 0 or position[0] >= len(input[0]) or position[1] < 0 or position[1] >= len(input):
                onMap = False
    except:
        position = [position[0] + facing[0], position[1]+facing[1]]
        if position[0] < 0 or position[0] >= len(input[0]) or position[1] < 0 or position[1] >= len(input):
            onMap = False

answer = len(path)

print(answer)