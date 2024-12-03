import importer
input = importer.parseInput()

left = []
right = []

#parse input into individual location IDs and assign to two lists
for line in input:
    line = line.split("   ")
    left.append(int(line[0]))
    right.append(int(line[1]))

#sort the two lists
left.sort()
right.sort()

#iterate through the list(s), summing the product of the left Location ID with the count of that Location ID in the right list
answer = 0
for i in range(0,len(left)):
    answer += left[i] * right.count(left[i])

print(answer)