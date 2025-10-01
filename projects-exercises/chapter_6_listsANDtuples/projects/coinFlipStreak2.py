import random

headCounts = 0
tailCounts = 0
numberOfStreaks = 0
coinFlip = (1, 0) # heads = 1, tails = 0

for _ in range(1_000_000):
    flip = random.choice(coinFlip)

    if headCounts == 6 or tailCounts == 6:
        numberOfStreaks += 1
        headCounts = 0
        tailCounts = 0
    if flip == "1":
        headCounts += 1
        tailCounts = 0
    else:
        headCounts = 0
        tailCounts += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 10_000))
