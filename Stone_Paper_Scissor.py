# imported Random Module
import random as r

# variables for Stone🪨 , Paper 📃, Scissor ✂️
options = ["stone", "paper", "scissors"]

# while loop for game :)
while True:
    # input for user
    Player_choice = input("Enter your choice (rock/paper/scissors):\n ")
    
    # making sure that player enters a correct value if Player_choice not in options:
    if Player_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # programme for computer
    computer_choice = r.choice(["stone", "paper", "scissors"])
    
    # printing values 
    print("Your choice is: \t" ,Player_choice )
    print("Computer's choice is: \t" ,computer_choice )

    if(Player_choice == "stone" and computer_choice == "scissors"):
        print("You win the game!") 
    
    elif(Player_choice == "paper" and computer_choice == "stone"):
        print("You win the game!") 

    elif(Player_choice == "scissors" and computer_choice == "paper"):
        print("You win the game!") 

    elif(Player_choice == computer_choice):
        print("It's a tie!")

    else:
        print("Oh! you lost the game")  
    
    # asking if player want to play ahead 
    Player_answer = input("Do you want to play again (yes/no): ")
    
    if(Player_answer.lower() != "yes"):
        break
    else:
        print("let's play again ")
   
print("Thanks for playing!")
