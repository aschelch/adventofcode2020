import re

file = open("input.txt", "r")
instructions = [data.rstrip('\n') for data in file]

north = 0
east = 0
heading = 90 # North = 0, East = 90

for instruction in instructions:
    if instruction[0] == 'N':
        north += int(instruction[1:])
    elif instruction[0] == 'S':
        north -= int(instruction[1:])
    elif instruction[0] == 'E':
        east += int(instruction[1:])
    elif instruction[0] == 'W':
        east -= int(instruction[1:])
    elif instruction[0] == 'F':
        if heading == 0:
            north += int(instruction[1:])
        elif heading == 180:
            north -= int(instruction[1:])
        if heading == 90:
            east += int(instruction[1:])
        elif heading == 270:
            east -= int(instruction[1:])
    elif instruction[0] == 'L':
        heading += 360-int(instruction[1:])
    elif instruction[0] == 'R':
        heading += int(instruction[1:])
    heading = heading % 360

print("Part 1 result", abs(north) + abs(east))


# Part 2

shipNorth = 0
shipEast = 0
wpNorth = 1
wpEast = 10

for instruction in instructions:
    oldNorth = wpNorth
    oldEast = wpEast 
    if instruction[0] == 'N':
        wpNorth += int(instruction[1:])
    elif instruction[0] == 'S':
        wpNorth -= int(instruction[1:])
    elif instruction[0] == 'E':
        wpEast += int(instruction[1:])
    elif instruction[0] == 'W':
        wpEast -= int(instruction[1:])
    elif instruction[0] == 'F':
        shipNorth += int(instruction[1:]) * wpNorth
        shipEast += int(instruction[1:]) * wpEast
    elif instruction[0] == 'L':
        if int(instruction[1:]) == 90:
            wpEast = -oldNorth
            wpNorth = oldEast
        if int(instruction[1:]) == 180:
            wpEast = -oldEast
            wpNorth = -oldNorth
        if int(instruction[1:]) == 270:
            wpEast = oldNorth
            wpNorth = -oldEast
    elif instruction[0] == 'R':
        if int(instruction[1:]) == 90:
            wpEast = oldNorth
            wpNorth = -oldEast
        if int(instruction[1:]) == 180:
            wpEast = -oldEast
            wpNorth = -oldNorth
        if int(instruction[1:]) == 270:
            wpEast = -oldNorth
            wpNorth = oldEast

print("Part 2 result", abs(shipNorth) + abs(shipEast))




