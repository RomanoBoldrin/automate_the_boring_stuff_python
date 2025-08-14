import time, sys, random

try:
    while True:
        random_1 = random.randint(2,12)
        random_2 = random.randint(2,12)

        for i in range(1, random_1):
            print('-' * (i * i))
            time.sleep(0.1)
        
        for i in range(random_2, 1, -1):
            print('-' * (i * i))
            time.sleep(0.1)

except KeyboardInterrupt:
    print()
    print('Exiting...')
    sys.exit()
    