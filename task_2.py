import random

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player"
    else:
        return "Computer"

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors or quit to exit): ").lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        if player_choice not in choices:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        
        if winner == "Draw":
            print("It's a draw!")
        elif winner == "Player":
            print("Congratulations! You win!")
        else:
            print("Computer wins! Better luck next time.")
        
if __name__ == "__main__":
    play_game()
