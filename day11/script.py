import re

file = open("input.txt", "r")
seats = [list(data.rstrip('\n')) for data in file]

rows = len(seats)
columns = len(seats[0])

# Get seat status in (dc,dr) direction (outside considered empty L)
def statusDirection(s, c, r, dc, dr):
    if c+dc < 0 or c+dc >= columns or r+dr < 0 or r+dr >= rows: # Out of bound in empty 
        return 'L'
    if s[r+dr][c+dc] == '.': # If floor, check further
        return statusDirection(s, c+dc, r+dr, dc, dr)
    return s[r+dr][c+dc]

# Check if seat in (dc,dr) direction is empty
def emptyDirection(s, c, r, dc, dr):
    return statusDirection(s, c, r, dc, dr) == 'L'

# Check if seat in (dc,dr) direction is occuppied
def occupiedDirection(s, c, r, dc, dr):
    return statusDirection(s, c, r, dc, dr) == '#'

# Look around and check if all is empty
def emptyAround(s, c, r):  
    return emptyDirection(s, c, r, -1, -1) and emptyDirection(s, c, r, 0, -1) and emptyDirection(s, c, r, +1, -1) \
       and emptyDirection(s, c, r, -1, 0)                                     and emptyDirection(s, c, r, +1, 0) \
       and emptyDirection(s, c, r, -1, +1) and emptyDirection(s, c, r, 0, +1) and emptyDirection(s, c, r, +1, +1)

# Look around and check if there are too many occupied seats
def tooManyAround(s, c, r):
    occupied = 0
    occupied += 1 if occupiedDirection(s, c, r, -1, -1) else 0
    occupied += 1 if occupiedDirection(s, c, r,  0, -1) else 0
    occupied += 1 if occupiedDirection(s, c, r, +1, -1) else 0
    occupied += 1 if occupiedDirection(s, c, r, -1,  0) else 0
    occupied += 1 if occupiedDirection(s, c, r, +1,  0) else 0
    occupied += 1 if occupiedDirection(s, c, r, -1, +1) else 0
    occupied += 1 if occupiedDirection(s, c, r,  0, +1) else 0
    occupied += 1 if occupiedDirection(s, c, r, +1, +1) else 0
    return occupied >= 5

changed = True
while changed:

    newSeats = [row[:] for row in seats]
    changed = False
    for r in range(rows):
        for c in range(columns):
            if seats[r][c] == '.':
                continue
            if seats[r][c] == 'L' and emptyAround(seats, c, r):
                newSeats[r][c] = '#'
                changed = True
                continue
            if seats[r][c] == '#' and tooManyAround(seats, c, r):
                newSeats[r][c] = 'L'
                changed = True
                continue
    seats = newSeats

result = '\n'.join([''.join(x) for x in seats])
print(result.count('#'))


