import random


def main():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
    print("\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    try:
        difficulty = int(input("\nEnter your choice (1-3): "))
        if difficulty > 3 or difficulty < 1:
            print("Enter number only in range 1-3 !")
            return
    except ValueError:
        print("Invalid input. Enter a number 1-3 !")
        return
    
    print(f"\nGreat! You have selected the {'Easy' if difficulty == 1 else ('Medium' if difficulty == 2 else 'Hard')} difficulty level.\nLet's start the game!")

    chances = 10 if difficulty == 1 else (5 if difficulty == 2 else 3)
    attempts = 0
    correct_answer = random.randint(1, 100)

    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
            if guess > 100:
                print("Number can't be bigger than 100 !")
                continue
            elif guess < 1:
                print("Number can't be less than 1 !")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        attempts += 1
        
        if guess == correct_answer:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess > correct_answer:
            print(f"Incorrect !. The number is less than {guess}")
        elif guess < correct_answer:
            print(f"Incorrect !. The number is more than {guess}")
        
        print(f"Remaining chances: {chances - attempts}")
    if attempts == chances and guess != correct_answer:
        print(f"You run out of chances ! Correct answer was: {correct_answer}")
        

        




if __name__ == "__main__":
    main()