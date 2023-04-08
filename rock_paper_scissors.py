import random
print('Let\'s play rock paper scissors!')
options= ["🪨", "🧻", "✂️"]
player = int(input('Choose "0" for rock, "1" for paper, and "2" for scissors.\n'))
comp = random.randint(0,len(options)-1)


if player > 2:
    print('You can only choose 0, 1 or 2!')
else:
    if comp == player:
        print(f'You both chose {options[player]}. It\'s a draw!')
    elif comp > player:
        if comp == 2:
            if player == 0:
                print(f'You chose {options[player]}. The computer chose {options[comp]}. Rock beats scissors. You win!')
            else:
                print(f'You chose {options[player]}. The computer chose {options[comp]}. Scissors beats paper. Computer wins!')
        else:
            print(f'You chose {options[player]}. The computer chose {options[comp]}. Paper beats rock. Computer wins!')
    elif player > comp:
        if player == 2:
            if comp == 0:
                print(f'You chose {options[player]}. The computer chose {options[comp]}. Rock beats scissors. Computer wins!')
            else:
                print(f'You chose {options[player]}. The computer chose {options[comp]}. Scissors beats paper. You win!')
        else:
            print(f'You chose {options[player]}. The computer chose {options[comp]}. Paper beats rock. You win!')

playagain = input("Do you want to play again? Yes or no?\n").lower()

while playagain == "yes" or playagain == "y":
    print('Let\'s play rock paper scissors!')
    player = int(input('Choose "0" for rock, "1" for paper, and "2" for scissors.\n'))
    comp = random.randint(0, len(options)-1)
    if comp == player:
        print(f'You both chose {options[player]}. It\'s a draw!')
    elif comp > player:
        if comp == 2:
            if player == 0:
                print(f'You chose {options[player]}. The computer chose {options[comp]}.Rock beats scissors. You win!')
            else:
                print(f'You chose {options[player]}. The computer chose {options[comp]}. Scissors beats paper. Computer wins!')
        else:
            print(f'You chose {options[player]}. The computer chose {options[comp]}. Paper beats rock. Computer wins!')
    elif player > comp:
        if player == 2:
            if comp == 0:
                print(f'You chose {options[player]}. The computer chose {options[comp]}. Rock beats scissors. Computer wins!')
            else:
                print(f'You chose {options[player]}. The computer chose {options[comp]}. Scissors beats paper. You win!')
        else:
            print(f'You chose {options[player]}. The computer chose {options[comp]}. Paper beats rock. You win!')
    playagain = input('Do you want to play again? Yes or no?\n').lower()
else:
    print("Thanks for playing!")
