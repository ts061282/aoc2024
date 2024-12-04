def mul(x,y):
    return x * y

import importer
import re
input = importer.parseInput()

muls = []
for line in input:
    muls += re.findall(r"mul\(\d{1,},\d{1,}\)",line)

answer = 0
for products in muls:
    answer += eval(products)

print(answer)