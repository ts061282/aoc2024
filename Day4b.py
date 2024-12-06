import importer
input = importer.parseInput(0)

answer = 0

for line in range(1,len(input)-1):
    for char in range (1,len(input[line])-1):
        if input[line][char] == 'A':
            if (input[line-1][char-1] == 'M' and input[line+1][char+1] == 'S') or (input[line-1][char-1] == 'S' and input[line+1][char+1] == 'M'):
                if (input[line-1][char+1] == 'M' and input[line+1][char-1] == 'S') or (input[line-1][char+1] == 'S' and input[line+1][char-1] == 'M'):
                    answer += 1

print(answer)