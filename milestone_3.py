#random fruit imported
from milestone_2 import word

#prompts user to input a letter and checks whether the format is correct
while True: 
    guess = input("Please enter a single letter guess:")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character")

#Check whether guessed letter is in word
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")