#Q3
player1=input("Enter Player 1:")
player_1_choice=input("Enter Player 1 choice:")
player2=input("Enter Player 2:")
player_2_choice=input("Enter Player 2 choice:")

def rpsGame(player_1_choice,player_2_choice):
    if player_1_choice == player_2_choice:
        print("Its a tie!!")
    elif player_1_choice == "Rock" and player_2_choice == "Scissor":
        print (player1,"wins!!")
    elif player_1_choice == "Rock" and player_2_choice == "Paper":
        print (player2,"wins!!")
    elif player_1_choice == "Scissor" and player_2_choice == "Paper":
        print (player1,"wins!!")
    elif player_1_choice == "Scissor" and player_2_choice == "Rock":
        print (player2,"wins!!")
    elif player_1_choice == "Paper" and player_2_choice == "Rock":
        print (player1,"wins!!")
    elif player_1_choice == "Paper" and player_2_choice == "Scissor":
        print (player2,"wins!!")

rpsGame(player_1_choice,player_2_choice)
