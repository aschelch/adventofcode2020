from copy import deepcopy


datas = [data.rstrip('\n') for data in open("input.txt", "r")]

def intToBitArray(value):
    b = [int(digit) for digit in bin(int(value))[2:]]
    b = ([0] * (36-len(b))) + b
    return b

def applyMask(value, mask):
    b = intToBitArray(value)
    for i in range(36):
        if mask[i] == 'X':
            continue
        b[i] = int(mask[i])
    return int("".join(map(str,b)), 2)


memory = dict()
for data in datas:
    if data[0:4] == "mask":
        mask = data[7:]
        continue

    addr = data[4:data.find("]")]
    value = int(data[data.find("=")+2:])

    memory[addr] = applyMask(value, mask)

print("Part 1 result", sum(memory.values()))



def applyMask2(addr, mask):
    r = [intToBitArray(addr)]
    for i in range(36):
        if mask[i] == '0':
            continue
        if mask[i] == '1':
            for j in range(len(r)):
                r[j][i] = 1
        if mask[i] == 'X':
            r = deepcopy(r)+deepcopy(r)
            for j in range(len(r)):
                r[j][i] = 0 if j < len(r)/2 else 1
    return [int("".join(map(str,a)), 2) for a in r]



memory = dict()
for data in datas:
    if data[0:4] == "mask":
        mask = data[7:]
        continue

    addr = data[4:data.find("]")]
    value = int(data[data.find("=")+2:])

    addrList = applyMask2(addr, mask)
    for a in addrList:
        memory[a] = value
    

print("Part 2 result", sum(memory.values()))

