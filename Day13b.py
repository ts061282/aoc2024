import importer
input = importer.parseInput(0)

machines = {}
unitConversion = 10000000000000
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
        machines[int((line-1)/4)][2] = [unitConversion + int(split[1].split(',')[0]), unitConversion + int(split[2])]

costA = 3
costB = 1

answer = 0
for machine in machines:
    det = (machines[machine][0][0]*machines[machine][1][1] - machines[machine][0][1]*machines[machine][1][0])
    aPress = int((machines[machine][2][0]*machines[machine][1][1] - machines[machine][2][1]*machines[machine][1][0]) / det)
    bPress = int((machines[machine][0][0]*machines[machine][2][1] - machines[machine][0][1]*machines[machine][2][0]) / det)
    if aPress * machines[machine][0][0] + bPress * machines[machine][1][0] == machines[machine][2][0]:
        if aPress * machines[machine][0][1] + bPress * machines[machine][1][1] == machines[machine][2][1]:
            answer += costA * aPress
            answer += bPress

print(answer)