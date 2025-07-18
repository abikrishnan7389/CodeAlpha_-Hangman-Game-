import random

def hangman():
    # List of 5 predefined words
    word_list = ["computer", "lion", "chef", "train", "river"]
    word = random.choice(word_list)  # Randomly choose a word
    guessed_word = ["_"] * len(word)  # Display as underscores
    guessed_letters = []  # Store guessed letters
    attempts_left = 6  # Limit of wrong guesses

    print("Welcome to Hangman!")
    print("Guess the word. You have 6 incorrect guesses.")
    
    while attempts_left > 0 and "_" in guessed_word:
        print("\nWord: ", " ".join(guessed_word))
        print("Guessed letters: ", ", ".join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        # Check for valid input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good job! The letter is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Wrong guess! You have {attempts_left} attempts left.")

    # Game over
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()
