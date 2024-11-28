# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

It begins by defining a Hangman class. This class initialises several attributes: a randomly selected word from a given word list, a list of underscores representing the word to be guessed, the number of lives remaining, the number of unique letters in the word, a list of guessed letters, and a list of words.

The check_guess method takes a user's guess as input. If the guess is correct, it updates the word_guessed list by replacing the corresponding underscores with the correct letter and decreases the num_letters count. If the guess is incorrect, it decreases the num_lives count.

The ask_for_input method prompts the user to enter a letter, validates the input, and calls the check_guess method.

The play_game function creates a Hangman object, named game, and enters a loop. It checks the number of lives and unique letters remaining to determine if the game is over. If not, it calls the ask_for_input method to get the user's guess.

The game continues until the player either guesses all the letters or runs out of lives.

## Installation instructions:

None.

## Usage intructions:

Run the file milestone_5.py through python to play. No other files are required. File names have been left in the naming convention prescribed by the project milestones. Under normal circumstances I would change these. 

### File structure:

-

### License information:

-


