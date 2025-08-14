import random, sys, time

wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')


while True:
    print(f'\n{wins} Wins, {losses} Losses, {ties} Ties\n')

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('>')
        player_move = (player_move.lower()).strip()

        if player_move == 'q':
            print('Is this a goodbye?\nThanks for using this program!')
            sys.exit()

        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        else:
            print('Please, no inventing the rules here! Play fair.\n')

    # converts player_move to a number (0 to 2)
    if player_move == 'r':
        player_move = 0
    elif player_move == 'p':
        player_move = 1
    elif player_move == 's':
        player_move = 2

    rps = ['ROCK', 'PAPER', 'SCISSORS']

    computer_move = random.randint(0, 2) # 0 = rock, 1 = paper, 2 = scissors

    print(f'\n{rps[player_move]} VS {rps[computer_move]}')
    
    if rps[player_move] == rps[computer_move]:
        print('It is a tie!')
        ties += 1
    elif rps[player_move] == rps[0] and rps[computer_move] == rps[1]:
        print('You lost!')
        losses += 1
    elif rps[player_move] == rps[0] and rps[computer_move] == rps[2]:
        print('You win!')
        wins += 1
    elif rps[player_move] == rps[1] and rps[computer_move] == rps[0]:
        print('You win!')
        wins += 1
    elif rps[player_move] == rps[1] and rps[computer_move] == rps[2]:
        print('You lost!')
        losses += 1
    elif rps[player_move] == rps[2] and rps[computer_move] == rps[0]:
        print('You lost!')
        losses += 1
    elif rps[player_move] == rps[2] and rps[computer_move] == rps[1]:
        print('You win!')
        wins += 1
    else:
        print('Something went wrong!')
