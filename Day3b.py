def mul(x,y):
    return x * y

operate = True

import importer
import re
input = importer.parseInput()

muls = []
for line in input:
    muls += re.findall(r"do\(\)|don't\(\)|mul\(\d{1,},\d{1,}\)",line)

answer = 0
for products in muls:
    if products == "do()":
        operate = True
    elif products == "don't()":
        operate = False
    elif operate:
        answer += eval(products)

print(answer)