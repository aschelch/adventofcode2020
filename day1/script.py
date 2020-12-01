file = open("input.txt", "r")
lines = [int(line.rstrip('\n')) for line in file]

# find a*b when a + b == 2020
for i in range(len(lines)):
    for j in range(i, len(lines)):
        if(lines[i] + lines[j] == 2020):
            print(lines[i] * lines[j])

# find a*b*c when a + b + c == 2020
for i in range(len(lines)):
    for j in range(i, len(lines)):
        for k in range(j, len(lines)):
            if(lines[i] + lines[j] + lines[k] == 2020):
                print(lines[i] * lines[j] * lines[k])

