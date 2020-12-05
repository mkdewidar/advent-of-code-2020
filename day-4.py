
import itertools
import re

def validateByr(v):
    return (int(v) <= 2002) and (int(v) >= 1920)

def validateIyr(v):
    return (int(v) <= 2020) and (int(v) >= 2010)

def validateEyr(v):
    return (int(v) <= 2030) and (int(v) >= 2020)

def validateHgt(v):
    unit = v[-2:]
    amount = v[:-2]
    if not amount.isdigit():
        return False
    amount = int(amount)
    if unit == 'cm':
        return (amount <= 193) and (amount >= 150)
    if unit == 'in':
        return (amount <= 76) and (amount >= 59)
    return False

def validateHcl(v):
    return re.search('#[0-9a-f]{6}', v) != None

def validateEcl(v):
    return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validatePid(v):
    return (len(v) == 9) and (v.isdigit())

requiredFields = {
    'byr': validateByr,
    'iyr': validateIyr,
    'eyr': validateEyr,
    'hgt': validateHgt,
    'hcl': validateHcl,
    'ecl': validateEcl,
    'pid': validatePid
}

# A generator that reads from f until the end of a entry (which is marked by a
# extra newline) or until the end of the file.
# returns empty set if there is nothing to read, or a set
# containing the field names of the
def readPassportEntry(f):
    currentPassportFields = {}

    for line in f:
        if line.isspace(): # a newline on its own marks the end of a entry
            yield currentPassportFields
            currentPassportFields = {}
            continue

        for field in line.split(' '):
            fieldName, fieldValue = field.rstrip().split(':')
            currentPassportFields[fieldName] = fieldValue

    yield currentPassportFields
    currentPassportFields = {}
    return # the end

with open('input.txt') as f:
    basicValidPassportCount = 0
    advancedValidPassportCount = 0

    for passport in readPassportEntry(f):
        fieldsPresent = True
        fieldsValid = True

        for key, value in requiredFields.items():
            if not passport.get(key):
                fieldsPresent = False
                continue

            if not value(passport.get(key)):
                fieldsValid = False

        if fieldsPresent:
            basicValidPassportCount += 1

        if fieldsPresent and fieldsValid:
            advancedValidPassportCount += 1

    print(f'Passports with present fields: {basicValidPassportCount}')
    print(f'Passports with correct fields: {advancedValidPassportCount}')
