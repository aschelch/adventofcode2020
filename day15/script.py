starting = [0,13,1,16,6,17]

played = dict()
last = None
for turn in range(1, 30000001):

    if turn <= len(starting):

        if last != None:
            played[last] = turn-1
    
        last = starting[turn-1]
        continue

    if last not in played.keys():

        if last != None:
            played[last] = turn-1

        last = 0
        continue


    lastTurn = played[last]
    if last != None:
        played[last] = turn-1

    last = (turn-1) - lastTurn

print("Step 1 result", last)