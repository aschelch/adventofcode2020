import re

file = open("input.txt", "r")
lines = [line.rstrip('\n') for line in file]

# count passwords that satify policy : letter contained between x and y times
count = 0
for i in range(len(lines)):
    res = re.search('([0-9]+)-([0-9]+) ([a-z]): (.*)', lines[i], re.IGNORECASE)
    
    x = int(res.group(1))
    y = int(res.group(2))
    password = res.group(4)
    letter = res.group(3)

    occurence = password.count(letter)
    if x <= occurence and occurence <= y :
        count+=1

print(count)

# count passwords that satify policy : letter exactly once in position x or y
count = 0
for i in range(len(lines)):
    res = re.search('([0-9]+)-([0-9]+) ([a-z]): (.*)', lines[i], re.IGNORECASE)

    x = int(res.group(1))
    y = int(res.group(2))
    password = res.group(4)
    letter = res.group(3)
    
    if (password[x-1] == letter and password[y-1] != letter) or (password[x-1] != letter and password[y-1] == letter) :
        count+=1
        
print(count)