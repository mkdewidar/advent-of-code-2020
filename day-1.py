
with open('input.txt') as f:
    numbers = [int(line) for line in f]

    p1Result = 0
    p2Result = 0

    for i in numbers:
        for j in numbers:
            if (i + j) == 2020:
                p1Result = i * j
            for k in numbers:
                if (i + j + k) == 2020:
                    p2Result = i * j * k

    print('Part 1: ', p1Result)
    print('Part 2: ', p2Result)
