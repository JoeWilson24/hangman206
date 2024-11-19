import random

word_list = ["banana", "strawberry", "peach", "mango", "melon"]

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Please enter a single letter guess:")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops, that is not a valid input")