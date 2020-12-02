
import re
import operator

def isValidSledRentalPassword(values):
    minOccurence = int(values.group(1))
    maxOccurence = int(values.group(2))
    occuringCharacter = values.group(3)
    password = values.group(4)

    numberOfOccurances = password.count(occuringCharacter)
    if (numberOfOccurances >= minOccurence) and (numberOfOccurances <= maxOccurence):
        return True

    return False

def isValidTobogganRentalPassword(values):
    firstPosition = int(values.group(1)) - 1
    secondPosition = int(values.group(2)) - 1
    character = values.group(3)
    password = values.group(4)

    if operator.xor(password[firstPosition] == character,
        password[secondPosition] == character):

        return True

    return False

with open('input.txt') as f:
    parser = re.compile('(\d+)-(\d+) (.*): ?(.+)')
    validSledPasswordCount = 0
    validTobogganPasswordCount = 0

    for line in f:
        parts = parser.search(line)

        if isValidSledRentalPassword(parts):
            validSledPasswordCount += 1

        if isValidTobogganRentalPassword(parts):
            validTobogganPasswordCount += 1

    print('valid sled rental passwords: ' + str(validSledPasswordCount))
    print('valid toboggan rental passwords: ' + str(validTobogganPasswordCount))
