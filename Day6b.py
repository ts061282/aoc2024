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
turnings = []
startfacing = [-1,0]
startposition = [-1,-1]
for line in range(0,len(input)):
    try:
        startposition = [line,input[line].index('^')]
        break
    except:
        next

answer = 0
for x in range(0,len(input[0])):
    for y in range (0,len(input)):
        inputAdd = input.copy()
        onMap = True
        position = startposition.copy()
        facing = startfacing.copy()
        turnings = []
        if inputAdd[y][x] == '.':
            inputAdd[y] = inputAdd[y][0:x] + '#' + inputAdd[y][x+1:]
        else:
            continue
        loop = False

        while onMap:
            if position[0] + facing[0] < 0 or position[0] + facing[0] >= len(inputAdd) or position[1]+facing[1] < 0 or position[1]+facing[1] >= len(inputAdd[0]):
                onMap = False
                break
            if inputAdd[position[0]+facing[0]][position[1]+facing[1]] == '#':
                facing = turnFacing(facing)
                if not [facing,position] in turnings:
                    turnings.append([facing.copy(),position.copy()])
                else:
                    loop = True
                    break
            else:
                position = [position[0] + facing[0], position[1]+facing[1]]
        answer += loop

print(answer)