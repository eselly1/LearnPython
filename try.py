import random
options={ 1:'Rock',
2:'Paper',
3:'Scissors',
}
print('Let\'s play rock, paper, scissors!')

def evaluate():
    player=int(input('Choose 1 for rock, 2 for paper or 3 for scissors: '))
    comp =random.randint(1,3)
    if player == comp:
        result=print(f'It\'s a draw! You both picked {options[player]}!')
    elif player > comp:
        if player == 2:
            result=print(f'You picked {options[player]}, and the computer picked {options[comp]}. You win!')
        elif player==3:
            if comp == 1:
                result=print(f'It\'s a draw! You both picked {options[player]}!')
            else:
                result=print(f'You picked {options[player]}, and the computer picked {options[comp]}. You win!')
    else:
        if comp == 2:
            result=print(f'It\'s a draw! You both picked {options[player]}!')
        elif comp==3:
            if player ==1:
                result=print(f'You picked {options[player]}, and the computer picked {options[comp]}. You win!')
            else:
                result=print(f'It\'s a draw! You both picked {options[player]}!')
    return result

evaluate()

playagain = True
while playagain:
    if play_again:=(str(input('Would you like to play again?: ')).lower) != 'y':
        playagain= False
    else:
        evaluate()
print('Thanks for playing!')
