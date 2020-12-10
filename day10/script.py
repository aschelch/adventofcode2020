import re

file = open("input.txt", "r")
outlets = [int(data.rstrip('\n')) for data in file]

#Part 1

outlets.sort()

output = 0
diff1 = 0
diff3 = 0
for outlet in outlets:
    if outlet-output == 1:
        diff1 += 1
    elif outlet-output == 3:
        diff3 += 1
    else:
        print('pb')
    output = outlet
diff3 += 1

print('1-jolt diff', diff1)
print('3-jolt diff', diff3)
print('Part 1 result =', diff1*diff3)


# Part 2 dirty solution..

cache = dict()
def numberToGoTo(start, target):

    if(start in cache):
        return cache[start]

    if start == target:
        cache[start] = 1
        return 1
    
    nextOutlets = [o for o in outlets if o > start and o-start<=3 ]
    if len(nextOutlets) == 0:
        cache[start] = 0
        return 0

    res = 0
    for o in nextOutlets:
        res += numberToGoTo(o, target)

    cache[start] = res
    return res

print('Part 2 result =', numberToGoTo(0, max(outlets)))


# Part2 better solution

path = dict()
path[0] = 1
for outlet in outlets:
    
    path[outlet] = 0
    if outlet-1 in path:
        path[outlet] += path[outlet-1]
    if outlet-2 in path:
        path[outlet] += path[outlet-2]
    if outlet-3 in path:
        path[outlet] += path[outlet-3]
print('Part 2 result (better) =', path[outlets[-1]])
