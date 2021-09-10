import random


choices = ['Rock','Paper','Scissors']
rounds = int(input("How many rounds would you like to play?"))

player_score = 0
computer_score = 0

player = False

random.seed()
history={}
list1=[]
for i in range(rounds):
    print("select option for round ",i+1)
    player_choice = int(input('Rock: 1,Paper: 2 or Scissors: 3?  '))
    computer_choice = random.choice(choices)
    history[i+1]=list((choices[player_choice-1],computer_choice))

round=int (input("Enter the round for which you need the information >>"))
if(round>0 and round<=rounds):
    player=history[round-1][0]
    computer=history[round-1][1]
    print("Player choice=",player)
    print("Computer choice=",computer)
    if player == computer:
        print('TIE!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('Computer win round ',round)
            
        else:
            print('Player win round ',round)
            
    elif player == 'Paper':
        if computer == 'Scissors':
            print('Computer win round ',round)
            
        else:
            print('Player win round ',round)
            
    elif player == 'Scissors':
        if computer == 'Rock':
            print('Computer win round ',round)
            
        else:
            print('Player win round ',round)

else:
    print("There is no round",round)
            




