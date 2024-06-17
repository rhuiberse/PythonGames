
x = 100
random = 0

# Guess a number the computer is thinking of
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 1
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, Guess again. Too low.')
            attempts += 1
        elif guess > random_number:
            print('Sorry. Guess again. To high')
            attempts += 1
        
    print(f'Yes, {random_number} was the number we were looking for. You have guessed it in {attempts} attempts')



# Let the computer guess the number you are looking for. 
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempts = 1
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'I guessed {guess} ====== Is tis too High (h), too low (l) or correct (c)?')
        if feedback == 'h':
            high = guess -1
            attempts += 1
        elif feedback == 'l':
            low = guess +1
            attempts += 1
    
    print(f'Yes, I guessed your number {guess} correctly in {attempts} attempts.')

