import re

file = open("input.txt", "r")
lines = [line.rstrip('\n') for line in file]


def isValidPassport(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    missing = list(set(required) - set(passport))
    if(len(missing) >= 2 or (len(missing) == 1 and missing[0] != 'cid')):
        return False

    if(int(passport['byr']) < 1920 or int(passport['byr']) > 2002):
        return False

    if(int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020):
        return False

    if(int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030):
        return False

    if(passport['hgt'].find('cm') > 0):
        h = int(passport['hgt'][:-2])
        if(h < 150 or h > 193):
            return False
    elif(passport['hgt'].find('in') > 0):
        h = int(passport['hgt'][:-2])
        if(h < 59 or h > 76):
            return False
    else:
        return False

    if(re.match('^#[0-9a-f]{6}$', passport['hcl']) == None):
        return False

    if(passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False

    if(re.match('^[0-9]{9}$', passport['pid']) == None):
        return False

    return True

result = 0
passport = []
for i in range(0, len(lines)):
    if(len(lines[i]) == 0):
        result += 1 if isValidPassport(dict(passport)) else 0
        passport = []
        continue
    passport.extend([(elem.split(":")[0], elem.split(":")[1]) for elem in lines[i].split(" ")])

if(len(passport) > 0):
    result += 1 if isValidPassport(dict(passport)) else 0

print(result)   
