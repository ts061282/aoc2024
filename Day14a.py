import importer
input = importer.parseInput(0)

positions = []
velocities = []

for line in input:
    
    splitline = line.split(" ")
    
    p = splitline[0].split("=")[1]
    p = p.split(",")
    p = [int(i) for i in p]
    positions += [[p[1],p[0]]]

    v = splitline[1].split("=")[1]
    v = v.split(",")
    v = [int(i) for i in v]
    velocities += [[v[1],v[0]]]

space = [103,101]
seconds = 100

for t in range(0,100):
    for robot in range(0,len(positions)):
        positions[robot][0] += velocities[robot][0]
        positions[robot][1] += velocities[robot][1]
        positions[robot][0] = positions[robot][0] % space[0]
        positions[robot][1] = positions[robot][1] % space[1]

quadrants = [[0,0],[0,0]]
for robot in range(0,len(positions)):
    halfwidth = int((space[1]-1)/2)
    halfheight = int((space[0]-1)/2)
    if positions[robot][0] < halfheight:
        if positions[robot][1] < halfwidth:
            quadrants[0][0] += 1
        elif positions[robot][1] > halfwidth:
            quadrants[0][1] += 1
    elif positions[robot][0] > halfheight:
        if positions[robot][1] < halfwidth:
            quadrants[1][0] += 1
        elif positions[robot][1] > halfwidth:
            quadrants[1][1] += 1

answer = quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]

print(answer)