import sys

def collatz(number):
    while True:
        if number == 1:
            print()
            sys.exit()
        if (number % 2) == 0:
            number //= 2
            print(number, end=' ')
        else:
            number *= 3
            number += 1
            print(number, end=' ')

while True:
    try:
        user_number = collatz(int(input('Enter a number: \n>')))
        print(user_number, end=' ')

    except ValueError:
        print('Insert only integers.\n')
        continue

