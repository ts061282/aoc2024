def xmasAs(input = []):
    asCoords = []
    for line in range(0,len(input)):
        for position in range(0,len(input[line])-2):
            if input[line][position:position+3] == "MAS" or input[line][position:position+3] == "SAM":
                asCoords.append((line,position+1))
    return asCoords

import re
import importer
input = importer.parseInput(1)

tiltInput = ['' for i in range(0,len(input[0])+len(input)-1)]
for line in range(0,len(input)):
    for char in range(0,len(input[line])):
        tIndex = line + char
        tiltInput[tIndex] = input[line][char] + tiltInput[tIndex]

transpTiltInput = ['' for i in range(0,len(input[0])+len(input)-1)]
for line in range(0,len(input)):
    for char in range(len(input[line])-1,-1,-1):
        tIndex = line + (len(input[line])-1-char)
        transpTiltInput[tIndex] = transpTiltInput[tIndex] + input[line][char]

answer = 0

tiltAs = xmasAs(tiltInput)
transpTiltAs = xmasAs(transpTiltInput)

for aye in tiltAs:
    if (aye[1],aye[0]) in transpTiltAs: #need to transpose coordinate of As correctly to compare
        answer += 1

print(answer)