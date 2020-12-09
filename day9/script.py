import re

file = open("input.txt", "r")
datas = [int(data.rstrip('\n')) for data in file]

def findSumIn(number, preamble):
    for a in preamble:
        others = preamble.copy()
        others.remove(a)
        if number - a in others:
            return True
    return False

def findInvalidNumber(datas, preamble):
    for i in range(preamble, len(datas)):
        number = datas[i]
        if not findSumIn(number, datas[i-preamble:i]):
            return number


def findContiguousList(datas, target):
    result = []
    for data in datas:
        if sum(result) == target:
            break
        result.append(data)
        while sum(result) > target:
            result.pop(0)
    return result
    

invalidNumber = findInvalidNumber(datas, 25)
print('Invalid number', invalidNumber)


contiguousList = findContiguousList(datas, invalidNumber)
print('Contiguous list ', contiguousList)

contiguousList.sort()
print('Encryption weakness ', contiguousList[0]+contiguousList[-1])



