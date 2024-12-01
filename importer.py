def parseInput(test:bool = False):
    if test:
        input = open('test.txt')
    else:
        input = open('input.txt')
    output = []
    for line in input:
        line = line.strip()
        output.append(line)
    return output