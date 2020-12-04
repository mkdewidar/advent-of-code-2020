
import operator
import functools

def countTreesInSlope(right, down):
    with open('input.txt') as f:
        treeCount = 0

        # read ahead on the first line to find the length of a line which we
        # will use later to skip lines and emulate going "down" the slope
        # also find the length of a pattern so we can use it later to emulate
        # them being repeated
        # assuming here that all lines are the same length
        lineLength = len(f.readline())
        patternLength = lineLength - 1

        # we use this to track our true x position
        x = 0

        while True:
            # move down as many lines as needed
            # -1 compensates for the fact that the last readline moved us one
            # line down
            # if down is 1, then this seek does nothing and we only move down
            # as a result of the readline
            f.seek(f.tell() + (lineLength * (down - 1)))

            # read the line we've just moved to
            row = f.readline()

            # if we've seeked past the end of the file, this is how we know
            if not row:
                break

            x += right

            # net position: this is the terrain you would be on if the patterns
            # in the file actually went on forever
            netX = x % patternLength

            if row[netX] == '#':
                treeCount += 1

    return treeCount

results = []

results.append(countTreesInSlope(1, 1))
print('Num of trees for slope (1, 1): ' + str(results[-1]))
results.append(countTreesInSlope(3, 1))
print('Num of trees for slope (3, 1): ' + str(results[-1]))
results.append(countTreesInSlope(5, 1))
print('Num of trees for slope (5, 1): ' + str(results[-1]))
results.append(countTreesInSlope(7, 1))
print('Num of trees for slope (7, 1): ' + str(results[-1]))
results.append(countTreesInSlope(1, 2))
print('Num of trees for slope (1, 2): ' + str(results[-1]))

print('Product: ' + str(functools.reduce(operator.mul, results)))