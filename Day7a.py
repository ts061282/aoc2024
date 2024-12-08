import importer
input = importer.parseInput(1)

equations = []
for line in input:
    resultValue = int(line.split(':')[0])
    parameters = line.split(' ')[1:]
    equations += [(resultValue, parameters)]

answer = 0
for equation in equations:
    permutations = [equation[1][0]]
    for parameter in range (1, len(equation[1])):
        for perm in range(0,len(permutations)):
            permutations.append("(" + permutations[perm]+"+"+equation[1][parameter] + ")")
            permutations[perm] = "(" + permutations[perm]+"*"+equation[1][parameter] + ")"
    for permutation in permutations:
        if eval(permutation) == equation[0]:
            answer += equation[0]
            break

print(answer)