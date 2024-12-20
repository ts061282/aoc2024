import os

def gridPrint(positions = [[0,0]], inverse = False):
    xDim = [x[1] for x in positions]
    xDim.sort()
    xDim = xDim[len(positions)-1]
    yDim = [y[0] for y in positions]
    yDim.sort()
    yDim = yDim[len(positions)-1]
    output = ""
    if not inverse:
        for y in range(0,yDim+1):
            for x in range(0,xDim+1):
                if [y,x] in positions: output += "x"
                else: output += "."
        output += "\n"
    else:
        for x in range(0,xDim+1):
            for y in range(0,yDim+1):
                if [y,x] in positions: output += "x"
                else: output += "."
        output += "\n"
    os.system('cls')
    print(output)