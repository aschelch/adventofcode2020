import re

file = open("input.txt", "r")
lines = [line.rstrip('\n') for line in file]

seats = []
for line in lines:
    row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[7:10].replace('L', '0').replace('R', '1'), 2)
    seatId = row * 8 + column
    seats.append(seatId)

print("Max seat : ", max(seats))

missing = list(set(range(min(seats), max(seats))) - set(seats))

print("My seat : ", missing[0])



