import random


choices = ['Rock','Paper','Scissors']
rounds = int(input("How many rounds would you like to play?"))

player_score = 0
computer_score = 0

player = False

random.seed()


while True:
    player = input('Rock,Paper or Scissors? ').capitalize()
    computer = random.choice(choices)
    if player == computer:
        print('TIE!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You Lose!')
            computer_score+=1
        else:
            print('You Win!')
            player_score +=1
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You Lose!')
            computer_score+=1
        else:
            print('You Win!')
            player_score +=1
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You Lose!')
            computer_score+=1
        else:
            print('You Win!')
            player_score +=1
    elif player == 'End':
        print('Final Scores')
        print('Computer Score: {}'.format(computer_score))
        print('Player Score: {}'.format(player_score))
        break

