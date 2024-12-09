def updateFirstEmpty(blocks = [],firstEmptyBlock = 0):
     for block in range(firstEmptyBlock+1,len(blocks)):
          if blocks[block] == []:
            return block
          
def updateLastData(blocks = [],lastDataBlock = 0):
     for block in range(lastDataBlock-1,-1,-1):
          if not blocks[block] == []:
            return block

import importer
input = importer.parseInput(0)

blocks = []
even = True
fileID = 0
lastFileBlock = 0
for char in range(0,len(input[0])):
    for block in range(0,int(input[0][char])):
            if even:
                blocks.append([fileID])
                lastFileBlock = len(blocks)-1
            else:
                blocks.append([])
    if even:
         fileID += 1
    even = not even

lastDataBlock = len(blocks)
lastDataBlock = updateLastData(blocks,lastDataBlock)
firstEmptyBlock = 0
firstEmptyBlock = updateFirstEmpty(blocks,firstEmptyBlock)
while firstEmptyBlock < lastDataBlock:
    blocks[firstEmptyBlock] = blocks[lastDataBlock]
    blocks[lastDataBlock] = []
    lastDataBlock = updateLastData(blocks,lastDataBlock)
    firstEmptyBlock = updateFirstEmpty(blocks,firstEmptyBlock)

answer = 0
for block in range(0,len(blocks)):
    if not blocks[block] == []:
        answer += blocks[block][0] * block

print(answer)