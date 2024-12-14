import importer
input = importer.parseInput(0)

stones = [int(x) for x in input[0].split(' ')]

blinks = 25

for blink in range(0,blinks):
    newStones = []
    for stone in stones:
        digits = len(str(stone))
        if stone == 0:
            newStones.append(1)
            next
        elif digits % 2 == 0:
            newStones.append(int(str(stone)[:int(digits/2)]))
            newStones.append(int(str(stone)[int(digits/2):]))
            next
        else: newStones.append(stone*2024)
    stones = newStones

answer = len(stones)

print(answer)