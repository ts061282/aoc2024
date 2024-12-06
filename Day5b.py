def fixUpdate(update = [], rules = []):
    for page in range(0,len(update)):
        for rule in rules:
            try: 
                if update[page] == rule[0] and update.index(rule[1]) < update.index(rule[0]):
                    temp = update[page]
                    update[page] = update[page-1]
                    update[page-1] = temp
                    update = fixUpdate(update, rules) 
                    break
            except:
                next
    return update
    

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
    if not valid:
        answer += fixUpdate(update, rules)[int((len(update)-1)/2)]


print(answer)