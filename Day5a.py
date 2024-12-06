import importer
input = importer.parseInput(0)

rules=[]
updates=[]
for line in input:
    if '|' in line:
        rules += [[int(x) for x in line.split('|')]]
    elif ',' in line:
        updates += [[int(x) for x in line.split(',')]]


answer = 0
for update in updates:
    valid = True
    for page in update:
        for rule in rules:
            try: 
                if page == rule[0] and update.index(rule[1]) < update.index(rule[0]):
                    valid = False
                    break
            except:
                next
    if valid:
        answer += update[int((len(update)-1)/2)]


print(answer)