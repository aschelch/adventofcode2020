
lines = [line.rstrip('\n') for line in open("input.txt", "r")]

#  Build range list for each field
fields = dict()
for i in range(lines.index('')):
    fields[lines[i][:lines[i].index(':')]] = [
        [int(a) for a in lines[i][lines[i].index(':')+1:lines[i].index(' or')].split('-')],
        [int(a) for a in lines[i][lines[i].index(' or ')+4:].split('-')]
    ]
    pass

# Value is in one of field ranges
def isValueValid(value):
    for field in fields.values():
        for range in field:
            if value >= range[0] and value <= range[1]:
                return True
    return False

def errorRate(values):
    result = 0
    for value in values:
        if not isValueValid(value):
            result += value
    return result

others = lines[lines.index('nearby tickets:')+1:]

result = 0
for ticket in others:
    result += errorRate([int(a) for a in ticket.split(',')])
        
print('Step 1 result', result)


# Part 2 

#  Get list of possible fields for a value
def getPossibleFields(value):
    possible = []
    for field in fields:
        for range in fields[field]:
            if value >= range[0] and value <= range[1]:
                possible.append(field)
    return possible


mine = [int(a) for a in lines[lines.index('your ticket:')+1].split(',')]


valid = []
for ticket in others:
    isValid = True
    for value in [int(a) for a in ticket.split(',')]:
        if not isValueValid(value):
            isValid = False
    if isValid:
        valid.append(ticket)

# List all possible fieds for each column
possibilities = [list(fields.keys()) for _ in range(len(mine))]
for ticket in valid:
    values = [int(a) for a in ticket.split(',')]
    for i in range(len(values)):
        possibilities[i] = list(set(possibilities[i]).intersection(set(getPossibleFields(values[i]))))

    
position = dict()
single = ()
while single != None:

    # Search a colunm where there is only on possibility
    single = None
    for i in range(len(possibilities)):
        if len(possibilities[i]) == 1:
            single = (possibilities[i][0], i)
            break

    # If none, we have finished or we are stuck
    if single == None:
        break

    position[single[0]] = single[1]

    # Remove current field from all others possibilites
    for i in possibilities:
        if single[0] in i:
            i.remove(single[0])


print('Step 2 result', mine[position['departure location']]*mine[position['departure date']]*mine[position['departure track']]*mine[position['departure platform']]*mine[position['departure station']]*mine[position['departure time']])