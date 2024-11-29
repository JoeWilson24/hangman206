import random
word_list = ["banana", "strawberry", "peach", "mango", "melon"]

class Hangman:
    def __init__(self, word_list, num_lives=5):                                    #Defining the hangman class, initialising the class attributes
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for random_fruit_letter in range(len(self.word))] #Creating a list of underscores for every letter in hidden word
        self.num_lives = num_lives
        self.num_letters = int(len(set(self.word)))                                #The number of unique letters in the word, made using the 'set' function
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
                    
        else:
            print(f"Sorry, {lower_case_guess} is not in the word. Try again.")
            print(f"Guessed letters: {self.list_of_guesses}")
            self.num_lives -= 1                                             #Reduce number of lives by 1 for each incorrect guess
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True: 
            guess = input("Please enter a single letter guess:")
            if len(guess) != 1 or not guess.isalpha() == True:              #Check whether letter guessed is single and alphabetical
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:                             #Check if letter has already been guessed
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)                          #Add guess to list of guesses
                self.check_guess(guess)
            break

test1=Hangman(["banana", "strawberry", "peach", "mango", "melon"])

test1.ask_for_input()



