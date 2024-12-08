import importer
input = importer.parseInput(0)

equations = []
for line in input:
    resultValue = int(line.split(':')[0])
    parameters = [int(x) for x  in line.split(' ')[1:]]
    equations += [(resultValue, parameters)]

answer = 0
for equation in equations:
    parameters = equation[1]
    permutations = [equation[0]]
    for parameter in range (len(equation[1])-1,-1,-1):
        for perm in range(0,len(permutations)):
            if str(parameters[parameter]) == str(permutations[perm])[-len(str(parameters[parameter])):] and parameters[parameter] != permutations[perm] and permutations[perm] >= 0:
                permutations.append(int(str(permutations[perm])[:-len(str(parameters[parameter]))]))
            if permutations[perm] % parameters[parameter] == 0 and permutations[perm] != 0:
                permutations.append(int(permutations[perm]/parameters[parameter]))
            permutations[perm] = permutations[perm]-parameters[parameter]
    for permutation in permutations:
        if permutation == 0:
            answer += equation[0]
            break

print(answer)