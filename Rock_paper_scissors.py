import random
while True:
    user_action = input("Enter a choice(rock paper, scissors: )")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action =random.choice(possible_actions)
    print(f"\nYou chose {user_action},computer chose{computer_action}.\n")
    if user_action == computer_action:
        print("Its a tie")
    elif user_action == 'rock':
        if computer_action == 'scissors':
            print("Rock smashes scissors you win!!!!!!!!!!!!!!")
        else:
            print("paper covers rock your lose!!!")
    elif user_action == 'paper':
        if computer_action == 'rock':
            print("Paper covers rock you win  you win!!!!!!!!!!!!!!")
        else:
            print("scissor cuts paper your lose!!!")
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print("scissors cuts paper you win!!!!!!!!!!!!!!")
        else:
            print("rock smashes scissors your lose!!!") 
    playagain = input("DO YOU WANT TO PLAY AGAIN? (Y/N): ")
    if playagain != "Y":
        break

