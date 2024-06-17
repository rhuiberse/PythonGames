import random
user = None
computer = None

def rps_play():
    user = input("(r) for Rock, (p) for Paper and (s) for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    # R > S, S > P, P > R
    if rps_win(user, computer):
        return 'You won!'
    
    return 'You Lost!'


def rps_win(player, opponent):
    # return True if player wins
    # R > S, S > P, P > R
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


rps_play()