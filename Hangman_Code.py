import random

def load_words():
    return ["python", "hangman", "developer", "github", "opensource", "programming", "terminal", "computer"]

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_game():
    word = random.choice(load_words()).upper()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6
    
    print("Welcome to Hangman!")
    
    while tries > 0 and word_letters:
        print(display_hangman(tries))
        print("Word: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print(f"Tries left: {tries}")
        print("Guessed letters: ", " ".join(guessed_letters))
        
        guess = input("Enter a letter: ").upper()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            tries -= 1
            guessed_letters.add(guess)
            print("Incorrect guess.")
        
        print("\n")
    
    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    play_game()