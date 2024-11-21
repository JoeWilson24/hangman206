import random
word_list = ["banana", "strawberry", "peach", "mango", "melon"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for fruit_letter in range(len(self.word))]
        self.num_lives = num_lives
        self.num_letters = int(len(set(self.word)))
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self,guess):
        lower_case_guess = (guess.lower())
        if lower_case_guess in self.word:
            print(f"Good guess! {lower_case_guess} is in the word.")
            for letter in range(len(self.word)):
                if self.word[letter] == lower_case_guess:
                    self.word_guessed[letter] = lower_case_guess
            self.num_letters -= 1
            print(f"There are {self.num_letters} letters left to guess")
            print(self.word_guessed)
                    
        else:
            print(f"Sorry, {lower_case_guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True: 
            guess = input("Please enter a single letter guess:")
            if len(guess) != 1 or not guess.isalpha() == True:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
            break

test1=Hangman(["banana", "strawberry", "peach", "mango", "melon"])

test1.ask_for_input()



