import random

running = True
incorrect = 0
total_correct = 0
# game loop
while running:
    correct = 0
    game_mode = input('Choose Game mode (A, S, M, D): ')
    if game_mode == 'a':
        while correct < 10:
            number_1 = random.randint(0, 30)
            number_2 = random.randint(0, 30)
            result = number_1 + number_2
            user_guess = int(input(f'{number_1} + {number_2}'))

            if user_guess == result:  # If he gets answer right
                correct += 1
                total_correct += 1
            else:  # If he gets answer wrong
                incorrect += 1
                print('Incorrect')

            if correct == 10:
                print('Congratulations')
            if incorrect == 3:
                print('You Lost')
                running = False
                break

    if game_mode == 's':
        while correct < 10:
            number_1 = random.randint(0, 30)
            number_2 = random.randint(0, number_1)
            result = number_1 - number_2
            user_guess = int(input(f'{number_1} - {number_2}'))

            if user_guess == result:  # If he gets answer right
                correct += 1
                total_correct += 1
            else:  # If he gets answer wrong
                incorrect += 1
                print('Incorrect')

            if correct == 10:
                print('Congratulations')
            if incorrect == 3:
                print('You Lost')
                running = False
                break

    if game_mode == 'm':
        while correct < 10:
            number_1 = random.randint(0, 12)
            number_2 = random.randint(0, 12)
            result = number_1 * number_2
            user_guess = int(input(f'{number_1} * {number_2}'))

            if user_guess == result:  # If he gets answer right
                correct += 1
                total_correct += 1
            else:  # If he gets answer wrong
                incorrect += 1
                print('Incorrect')

            if correct == 10:
                print('Congratulations')
            if incorrect == 3:
                print('You Lost')
                running = False
                break

    if game_mode == 'd':
        while correct < 10:
            number_1 = random.randint(0, 12)
            number_2 = random.randint(0, 12) * number_1
            result = number_2 / number_1
            user_guess = int(input(f'{number_2} / {number_1}'))

            if user_guess == result:  # If he gets answer right
                correct += 1
                total_correct += 1
            else:  # If he gets answer wrong
                incorrect += 1
                print('Incorrect')

            if correct == 10:
                print('Congratulations')
            if incorrect == 3:
                print('You Lost')
                running = False
                break

print(f'Your score was {total_correct * 100}')