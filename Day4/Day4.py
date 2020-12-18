codes = ["byr", "iyr", "eyr","hgt","hcl","ecl", "pid"]

def valid_pass(passport):
    for code in codes:
        if code not in passport:
   
            return False
    return True

def part_one():
    # read data
    with open('input.txt') as input:
        data = input.readlines()
        data = [line.strip() for line in data]
        
        valid_passports = []

        count = 0
        passport = ''
        for line in data:
            if line != '':
                passport += ' ' + line
                # print(passport)
            else:
                if valid_pass(passport) == True:
                    count += 1
                    valid_passports.append(passport)
                    # print("count", count, passport)
                passport =''
    
    # check last line
    if valid_pass(passport) == True:
        count += 1
        valid_passports.append(passport)
    
    print(count)
    return valid_passports

def part_two(passport):
    # make dict
    # print(passports)
    data = {}
    passport = passport.split()

    for item in passport:
        key = item[:3]
        value = item[4:]
        data[key] = value
    # print(data)

    if not valid_byr(data['byr']):
        return False
    if not valid_iyr(data['iyr']):
        return False
    if not valid_eyr(data['eyr']):
        return False
    if not valid_hgt(data['hgt']):
        return False
    if not valid_hcl(data['hcl']):
        return False
    if not valid_ecl(data['ecl']):
        return False
    if not valid_pid(data['pid']):
        return False
    
    return True

def valid_byr(byr):
    # byr = four digits; at least 1920 and at most 2002.
    length = len(byr)
    byr = int(byr)

    if length != 4 or byr < 1920 or byr > 2020:
        return False 
    return True 

def valid_iyr(iyr):
    # iyr = four digits; at least 2010 and at most 2020.
    iyr = int(iyr)

    if iyr < 2010 or iyr > 2020:
        return False
    return True

def valid_eyr(eyr):
    # four digits; at least 2020 and at most 2030.
    eyr = int(eyr)

    if eyr < 2020 or eyr > 2030:
        return False
    return True

def valid_hgt(hgt):
    units = hgt[-2:]

    if units not in ['in', 'cm']:
        return False
    
    hgt = int(hgt[:-2])

    # If in, the number must be at least 59 and at most 76.
    if units == 'in':
        if hgt < 59 or hgt > 76:
            return False

    # If cm, the number must be at least 150 and at most 193.
    if units == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    return True
import re
def valid_hcl(hcl):
    # a # followed by exactly six characters 0-9 or a-f.
    if hcl[0] != '#':
        
        return False

    if len(hcl[1:]) != 6:
        # print(hcl)
        return False
    
    if re.search('[g-z]', hcl[1:]):
        return False
    return True

def valid_ecl(ecl):
    # exactly one of: amb blu brn gry grn hzl oth.
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if ecl not in colors:
        return False
    
    return True

def valid_pid(pid):
    # a nine-digit number, including leading zeroes.
    if len(pid) != 9:
        return False
    return True

def pass_passports():
    valid_pass = part_one()
    final_count = 0
    for passport in valid_pass:
        if part_two(passport):
            # print(passport)
            final_count += 1
    return final_count -1
    
print(pass_passports())