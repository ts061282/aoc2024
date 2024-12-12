import importer
input = importer.parseInput(0)

FAT = [] #sector, filename, filesize, checked?
sector = 0
for char in range(0,len(input[0])):
   if char % 2 == 1:
        sector += int(input[0][char])
   else:
      FAT += [[sector,int(char/2),int(input[0][char]),False]]
      sector += int(input[0][char])

file=len(FAT)-1
while file >= 0:
   if not FAT[file][3]:
      FAT[file][3] = True
      for gap in range(0,file):
         if FAT[gap+1][0] - FAT[gap][0] - FAT[gap][2] >= FAT[file][2]:
               FAT[file][0] = FAT[gap][0] + FAT[gap][2]
               FAT = FAT[:gap+1] + [FAT[file]] + FAT[gap+1:file] + FAT[file+1:]
               file += 1
               break
   file -= 1
                
answer = 0
for file in FAT:
   for block in range(file[0],file[0]+file[2]):
      answer += block * file[1]

print(answer)