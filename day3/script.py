import re

file = open("input.txt", "r")
lines = [line.rstrip('\n') for line in file]

def countTree(right, down):
    column = 0
    treeCount = 0   
    for i in range(0, len(lines), down):
        if(lines[i][column] == '#'):
            treeCount += 1
        column = (column+right) % len(lines[i])
    return treeCount

a = countTree(1,1)
b = countTree(3,1)
c = countTree(5,1)
d = countTree(7,1)
e = countTree(1,2)

print(a*b*c*d*e)




    