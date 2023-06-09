import random

num = []
num1 = 1
print('ROBO :  Welcome to \'THE GUESSER\'')
print('ROBO :  This game can include upto 2 players')
print('ROBO :  In this game you have to guess a number between \'1 to 100\'')
players = input('ROBO :  How many players will play ?  ').lower().strip()
print('ROBO :  There will be some hints in the game')
print('ROBO :  We will indicate whether your guess is too high or too low to the \'RANDOM NUMBER\'')


def singleplayer():
    range = 100
    difficulty = input('What difficulty would you want to play with (Easy, Hard or Medium) ?  ').lower().strip()
    chance = 9
    name = input('Please tell your name :  ').capitalize()
    match difficulty:
        case 'easy':
            easy()
        case 'medium':
            medium()
        case 'hard':
            hard()
        case _:
            print('ERROR : No such difficulty exists 😵🥴')
    rand = random.choice(num)
    rand = str(rand)
    hint = rand[0]
    rand = int(rand)
    # space for the contain hint
    # if want to , can add the hint
    while chance >= 0:
        ans = int(input('Guess the Number : '))
        print('')
        if chance > 0:
            if ans == rand:
                print(f'{name}, You guessed it right')
                print(f'The answer is {rand}')
                print('YOU WON 🥳🥳')
                quit()
            else:
                print('The guess is incorrect')
                print(f'You have {chance} chances left')
        if chance == 0:
            print(f'{name}, You lost 😭😢')
            print('You are left with 0 chances')
            quit()
        chance -= 1
        if ans < rand:
            print('HINT :  The number you guessed is LOWER')
        else:
            print('HINT :  The number you guessed is HIGHER')
        print('')


def multiplayer():
    difficulty = input('What difficulty would you want to play with (Easy, Hard or Medium) ?  ').lower().strip()
    match difficulty:
        case 'easy':
            easy()
        case 'medium':
            medium()
        case 'hard':
            hard()
        case _:
            print('ERROR :  No such difficulty exists 😵🥴')
    rand = random.choice(num)
    rand = str(rand)
    hint = rand[0]
    rand = int(rand)
    # space for the contain hint
    # if want to , can add the hint
    chance = 10
    time = 10
    chance1 = 4
    chance2 = 4
    p1 = input('Who will be Player 1 ?  ').capitalize()
    p2 = input('Who will be Player 2 ?  ').capitalize()
    while chance >= 0:
        if time % 2 == 0:
            player1 = int(input(f'{p1} Guess the Number : '))
            print('')
            if chance > 0:
                if player1 == rand:
                    print('You guessed it right')
                    print(f'The answer is {rand}')
                    print(f'{p1}, YOU WON 🥳🥳')
                    quit()
                else:
                    print('The guess is incorrect')
                    print(f'{p1} have {chance1} chances left')
            chance1 -= 1
            if player1 < rand:
                print('HINT :  The number you guessed is LOWER')
            else:
                print('HINT :  The number you guessed is HIGHER')
            print('')
        elif time % 2 == 1:
            player2 = int(input(f'{p2} Guess the number :  '))
            print('')
            if chance > 0:
                if player2 == rand:
                    print('You guessed it right')
                    print(f'The answer is {rand}')
                    print(f'{p2}, YOU WON 🥳🥳')
                    quit()
                else:
                    print('The guess is incorrect')
                    print(f'{p2} have {chance2} chances left')
            chance2 -= 1
            if player2 < rand:
                print('HINT :  The number you guessed is LOWER')
            else:
                print('HINT :  The number you guessed is HIGHER')
            print('')
        chance -= 1
        time -= 1
        if time == 0:
            print('you both lost')
            print('you are left with 0 chances')
            quit()

def easy():
    print('You have to guess a number between 1 - 20')
    num1 = 1
    while num1 <= 20:
        num.append(num1)
        num1 += 1

def medium():
    print('You have to guess a number between 1 - 50')
    num1 = 1
    while num1 <= 50:
        num.append(num1)
        num1 += 1
def hard():
    print('You have to guess a number between 1 - 100')
    num1 = 1
    while num1 <= 100:
        num.append(num1)
        num1 += 1
match players:
    case '1' | 'one' | 'One':
        singleplayer()
    case '2' | 'two' | 'Two':
        multiplayer()
    case _:
        print('ERROR :  This game supports players upto 2 only 😐😐')
