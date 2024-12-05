import re
import importer
input = importer.parseInput(0)

transpInput = ['' for i in range(0,len(input[0]))]
for line in input:
    for char in range(0,len(line)):
        transpInput[char] += line[char]

tiltInput = ['' for i in range(0,len(input[0])+len(input)-1)]
for line in range(0,len(input)):
    for char in range(0,len(input[line])):
        tIndex = line + char
        tiltInput[tIndex] = input[line][char] + tiltInput[tIndex]

transpTiltInput = ['' for i in range(0,len(input[0])+len(input)-1)]
for line in range(0,len(input)):
    for char in range(len(input[line])-1,-1,-1):
        tIndex = line + (len(input[line])-1-char)
        transpTiltInput[tIndex] = input[line][char] + transpTiltInput[tIndex]

answer = 0

for line in input:
    answer += len(re.findall("XMAS",line)) + len(re.findall("SAMX",line))

for line in transpInput:
    answer += len(re.findall("XMAS",line)) + len(re.findall("SAMX",line))

for line in tiltInput:
    answer += len(re.findall("XMAS",line)) + len(re.findall("SAMX",line))

for line in transpTiltInput:
    answer += len(re.findall("XMAS",line)) + len(re.findall("SAMX",line))

print(answer)