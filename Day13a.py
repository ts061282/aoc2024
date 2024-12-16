import importer
input = importer.parseInput(0)

machines = {}
for line in range(0,len(input)):
    if len(input[line]) < 7:
        continue
    if input[line][7] == 'A':
        split = input[line].split('+')
        machines.update({int(line/4):[[int(split[1].split(',')[0]),int(split[2])],[],[]]})
    elif input[line][7] == 'B':
        split = input[line].split('+')
        machines[int((line-1)/4)][1] = [int(split[1].split(',')[0]),int(split[2])]
    elif input[line][7] == 'X':
        split = input[line].split('=')
        machines[int((line-1)/4)][2] = [int(split[1].split(',')[0]),int(split[2])]

costA = 3
costB = 1
pressLimit = 100

for machine in machines.keys():
    for bPress in range(pressLimit,-1,-1):
        bX = machines[machine][1][0] * bPress
        bY = machines[machine][1][1] * bPress
        if bX > machines[machine][2][0]:
            continue
        if bY > machines[machine][2][1]:
            continue
        aX = machines[machine][2][0] - bX
        aY = machines[machine][2][1] - bY
        if aX / machines[machine][0][0] != aY / machines[machine][0][1]:
            continue
        if aX % machines[machine][0][0] != 0 or aY % machines[machine][0][1] != 0:
            continue
        if aX / machines[machine][0][0] > pressLimit or aY / machines[machine][0][1] > pressLimit:
            continue
        aPress = int(aX / machines[machine][0][0])
        machines[machine].append([aPress,bPress])
        break
    if len(machines[machine]) == 3:
        machines[machine].append(None)

answer = 0
for machine in machines:
    if not machines[machine][3] is None:
        answer += costA * machines[machine][3][0] + costB * machines[machine][3][1]


print(answer)