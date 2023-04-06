import random
num = []
num1 = 1
print('ROBO :  Welcome to \'THE GUESSER\'')
print('ROBO :  This game can include upto 2 players')
print('ROBO :  In this game you have to guess a number between \'1 to 100\'')
players = input('ROBO :  Please tell how many players will play ?  ')
while num1 <= 100:
    num.append(num1)
    num1 += 1
random = random.choice(num)


def singleplayer():
    chance = 14
    while chance >= 0:
        ans = input('Guess the Number : ')
        if chance > 0:
            if ans == random:
                print('You guessed it right')
                print(f'The answer is {random}')
                print('YOU WON 🥳🥳')
                quit()
            else:
                print('The guess is incorrect')
                print(f'You have {chance} chances left')
        if chance == 0:
            print('You lost')
            print('You are left with 0 chances')
        chance -= 1


def multiplayer():
    chance = 20
    time = 20
    chance1 = 9
    chance2 = 9
    while chance >= 0:
        if time % 2 == 0:
            player1 = input(f'{p1} Guess the Number : ')
            if chance > 0:
                if player1 == random:
                    print('You guessed it right')
                    print(f'The answer is {random}')
                    print(f'{p1}, YOU WON 🥳🥳')
                    quit()
                else:
                    print('The guess is incorrect')
                    print(f'{p1} have {chance1} chances left')
            chance1 -= 1
        elif time % 2 == 1:
            player2 = input(f'{p2} Guess the number :  ')
            if chance > 0:
                if player2 == random:
                    print('You guessed it right')
                    print(f'The answer is {random}')
                    print(f'{p2}, YOU WON 🥳🥳')
                    quit()
                else:
                    print('The guess is incorrect')
                    print(f'{p2} have {chance2} chances left')
            chance2 -= 1
        chance -= 1
        time -= 1


match players:
    case '1' | 'one' | 'One':
        name = input('Please tell your name : ')
        print(f'{name}, You will have a total of 15 chances')
        singleplayer()
    case '2' | 'two' | 'Two':
        p1 = input('Please tell who will be Player 1 : ')
        p2 = input('Please tell who will be Player 1 : ')
        print(f'{p1} and {p2}, You both will have a total of 20 chances (10 each)')
        multiplayer()
