import random


def swgGame(comp_selection, user_selection):
    if comp_selection == user_selection:     
        return None

    elif comp_selection == 's':
        if user_selection=='w':
            return False
        elif user_selection=='g':
            return True
    
    elif comp_selection == 'w':
        if user_selection=='g':
            return False
        elif user_selection=='s':
            return True
    
    elif comp_selection == 'g':
        if user_selection=='s':
            return False
        elif user_selection=='w':
            return True


game_choices=['s','g','w']

comp_selection=random.choice(game_choices)



user_selection = input("Enter your choice: ")
predict_winner = swgGame(comp_selection, user_selection)

print("Computer chose: ", comp_selection)
print("User chose : ", user_selection)

if predict_winner == None:
    print("Its a tie!")
elif predict_winner:
    print("User Won!")
else:
    print("User Lost!")





