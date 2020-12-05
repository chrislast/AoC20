from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

PASSPORTS=[dict()]
for line in DATA:
    if not line:
        PASSPORTS.append(dict())
    else:
        for attr in line.split(" "):
            k=attr[:3]
            v=attr[4:]
            PASSPORTS[-1][k]=v

@part1
def func(expect=256):
    count = 0
    for passport in PASSPORTS:
        if "byr" in passport and \
           "iyr" in passport and \
           "eyr" in passport and \
           "hgt" in passport and \
           "hcl" in passport and \
           "ecl" in passport and \
           "pid" in passport:
           count += 1
    return count

@part2
def func(expect=198):
    count = 0
    for passport in PASSPORTS:
        if "byr" in passport and 1920 <= int(passport["byr"]) <= 2002 and \
           "iyr" in passport and 2010 <= int(passport["iyr"]) <= 2020 and \
           "eyr" in passport and 2020 <= int(passport["eyr"]) <= 2030 and \
           "hgt" in passport and re.match("^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$", passport["hgt"]) and \
           "hcl" in passport and re.match("^#[0-9a-f]{6}$", passport["hcl"]) and \
           "ecl" in passport and re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport["ecl"]) and \
           "pid" in passport and re.match("^[0-9]{9}$", passport["pid"]):
           count += 1
    return count
