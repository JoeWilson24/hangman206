#random fruit imported
from milestone_2 import word

#Function to prompt user to input a letter and checks whether the format is correct
def ask_for_input():
    while True: 
        guess = input("Please enter a single letter guess:")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character")
    check_guess(guess)

#Function to convert guessed letter to lower case check whether guessed letter is in word
def check_guess(guess):
    lower_guess = (guess.lower())
    if lower_guess in word:
        print(f"Good guess! {lower_guess} is in the word.")
    else:
        print(f"Sorry, {lower_guess} is not in the word. Try again.")

ask_for_input()