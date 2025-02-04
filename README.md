import random

# List of words
words = ['python', 'hangman', 'programming', 'easy', 'code']

# Choose a random word
word = random.choice(words)
guessed_word = ['_'] * len(word)
guessed_letters = []

# Number of attempts
attempts = 6

print("Welcome to Hangman!")

# Game loop
while attempts > 0 and '_' in guessed_word:
    print("\nWord:", ' '.join(guessed_word))
    print("Guessed letters:", ', '.join(guessed_letters))
    print(f"Attempts left: {attempts}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess.")

# Check win or lose
if '_' not in guessed_word:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame over. The word was: {word}")# Hangman.code
