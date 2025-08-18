import random

def main():
    heads_count = 0
    tails_count = 0

    sequence = []

    for i in range(10_000):
        heads_or_tails = random.randint(0,1) # 0 for head, 1 for tails

        if heads_or_tails == 0:
            heads_count += 1
            sequence.append('H')
        else:
            tails_count += 1
            sequence.append('T')

    for i in sequence:
        heads_six_sequence = []
        heads_six_streak = 0

        if sequence[i] == 'H':
            if len(heads_six_sequence) < 6:
                heads_six_sequence.append('H')
            else:
                heads_six_streak += 1

    for i in sequence:
        tails_six_sequence = []
        tails_six_streak = 0

        if sequence[i] == 'H':
            if len(tails_six_sequence) < 6:
                tails_six_sequence.append('H')
            else:
                tails_six_streak += 1
    


    # maybe iterate and do both at the same time? IDK



    return heads_count, tails_count, sequence
heads_count, tails_count, sequence = main()



print(heads_count)
print(tails_count)
