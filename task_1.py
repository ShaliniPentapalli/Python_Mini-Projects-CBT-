import random

def get_feedback(secret, guess):
    correct_position = 0
    correct_digit = 0
    secret_counts = {}
    guess_counts = {}
    
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            correct_position += 1
        else:
            if secret[i] in secret_counts:
                secret_counts[secret[i]] += 1
            else:
                secret_counts[secret[i]] = 1
            if guess[i] in guess_counts:
                guess_counts[guess[i]] += 1
            else:
                guess_counts[guess[i]] = 1
    
    for digit in guess_counts:
        if digit in secret_counts:
            correct_digit += min(secret_counts[digit], guess_counts[digit])
    
    return correct_position, correct_digit

def play_game():
    num_digits = int(input("Enter the number of digits for the secret number: "))
    
    # Player 1 sets the secret number
    secret_number = input(f"Player 1, set your secret number (a {num_digits}-digit number): ")
    print("\n" * 50)  # Clear the screen
    
    attempts_p2 = 0
    guess = ""
    while guess != secret_number:
        guess = input(f"Player 2, enter your guess (a {num_digits}-digit number): ")
        attempts_p2 += 1
        if guess == secret_number:
            print(f"Correct! Player 2 guessed the number in {attempts_p2} attempts.")
            break
        correct_position, correct_digit = get_feedback(secret_number, guess)
        print(f"Feedback: {correct_position} correct digit(s) in the correct position, {correct_digit} correct digit(s) but in the wrong position.")
    
    # Switch roles
    print("\n" * 50)  # Clear the screen
    secret_number = input(f"Player 2, set your secret number (a {num_digits}-digit number): ")
    print("\n" * 50)  # Clear the screen
    
    attempts_p1 = 0
    guess = ""
    while guess != secret_number:
        guess = input(f"Player 1, enter your guess (a {num_digits}-digit number): ")
        attempts_p1 += 1
        if guess == secret_number:
            print(f"Correct! Player 1 guessed the number in {attempts_p1} attempts.")
            break
        correct_position, correct_digit = get_feedback(secret_number, guess)
        print(f"Feedback: {correct_position} correct digit(s) in the correct position, {correct_digit} correct digit(s) but in the wrong position.")
    
    # Determine the winner
    if attempts_p1 < attempts_p2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_p1 > attempts_p2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("The game is a draw!")

if __name__ == "__main__":
    play_game()
