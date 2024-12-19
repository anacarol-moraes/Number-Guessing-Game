import random
#take the input from the user
def main():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0 

    while True:
        try: 
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print ("Please guess a number within the range!")
            elif guess < number_to_guess:
                print ("Too low, try again.")
            elif guess> number_to_guess:
                print ("Too high, try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} trys.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
main()