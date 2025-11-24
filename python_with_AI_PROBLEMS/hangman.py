# Objective: Write a python program to implement Water Jug Problem.
import random

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
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

def hangman():
    word_list = ["artificial", "intelligence", "python", "algorithm", "machine", "learning", "data", "science"]
    word = random.choice(word_list).lower()
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_as_list = list("_" * len(word))
                for i, letter in enumerate(word):
                    if letter in guessed_letters:
                        word_as_list[i] = letter
                if "_" not in word_as_list:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                break
        else:
            print("Invalid input.")

        print(display_hangman(tries))
        print(" ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print("\n")

    if guessed:
        print(f"Congratulations! You guessed the word {word}. You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")

# Run the Hangman game
hangman()