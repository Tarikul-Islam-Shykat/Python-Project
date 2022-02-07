import random
def play():
    while True:
        try:
            user1 = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
            if (user1 == 'r') or (user1 == 'p') or (user1 == 's'):
                user = user1
                break
            else:
                raise ValueError
        except ValueError:
            print("Choice doesn't exist")
            continue
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie\n'

    if is_win(user, computer):
        return 'You won!\n'
    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

start = input("Press [P] to play or [S] to stop\n")

while True:
    if(start.lower() == 'p'):
        print(play())
        start_again = input("[P] to play again or [S] to stop\n")
        if(start_again.lower() == 'p'):
            continue
        else:
            print("Game Ended")
            break
    else:
        print("Game Ended")
        break
