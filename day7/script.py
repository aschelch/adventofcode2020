import re

file = open("input.txt", "r")
rules = [rule.rstrip('\n') for rule in file]

bagContents = dict()
bagContainers = dict()

# Rule extractions
for rule in rules:

    bag = re.search('^([^,\.]*) bags contain', rule, re.IGNORECASE).group(1)
    contents = re.findall('([0-9]+) ([^,\.]*) bags?', rule, re.IGNORECASE)

    bagContents[bag] = contents

    # To find bag containers, lets save for each bag, all possible container bag
    for _ , content  in contents:
        if(content not in bagContainers):
            bagContainers[content] = []
        bagContainers[content].append(bag)

 
# Part 1

seen = []
def findContainers(bag):

    if(bag in seen): # Avoid a infiniti loop
        return []
    seen.append(bag)

    if(bag not in bagContainers):
        return []
    
    res = bagContainers[bag] # Direct containers
    for container in bagContainers[bag]:
        res.extend(findContainers(container)) # Indirect containers
    return res


print(len(set(findContainers('shiny gold'))))


# Part 2

def countBagInside(bag):
    if(len(bagContents[bag]) == 0):
        return 0

    res = 0
    for subbag in bagContents[bag]:
        res += int(subbag[0]) + int(subbag[0]) * countBagInside(subbag[1])
    return res

print(countBagInside('shiny gold'))



