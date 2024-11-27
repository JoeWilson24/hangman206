import random
word_list = ["banana", "strawberry", "peach", "mango", "melon"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for random_fruit_letter in range(len(self.word))] #Creating a list of underscores for every letter in hidden word
        self.num_lives = num_lives
        self.num_letters = int(len(set(self.word)))
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self,guess):
        lower_case_guess = (guess.lower())
        if lower_case_guess in self.word:
            print(f"Good guess! {lower_case_guess} is in the word.")
            for letter in range(len(self.word)):                            #Iterate through the random word
                if self.word[letter] == lower_case_guess:                   #Indexing the random word for the guessed letter
                    self.word_guessed[letter] = lower_case_guess            #Indexing the blank guessed word for the guessed letter and replacing
            self.num_letters -= 1                                           #Reduce number of letters by 1 for correct guess
            print(f"There are {self.num_letters} letters left to guess")
            print(self.word_guessed)
            print("")
                    
        else:
            print(f"Sorry, {lower_case_guess} is not in the word. Try again.")
            print(f"Guessed letters: {self.list_of_guesses}")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")
            print(self.word_guessed)
            print("")

    def ask_for_input(self):
        while True: 
            guess = input("Please enter a single letter guess:")
            if len(guess) != 1 or not guess.isalpha() == True:              #Check whether letter guessed is single and alphabetical
                print("Invalid letter. Please enter a single alphabetical character")
                print("")
            elif guess in self.list_of_guesses:                             #Check if letter has already been guessed
                print("You already tried that letter!")
                print("")
            else:
                self.list_of_guesses.append(guess)                          #Add guess to list of guesses
                self.check_guess(guess)
            break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters == 0:
            print("Congratulations, you won the game!")
            break
        else:
            game.ask_for_input()

play_game(word_list)