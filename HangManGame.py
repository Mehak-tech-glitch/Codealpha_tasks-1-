import random

def get_random_word():
    words = ["python", "hangman", "developer", "keyboard", "notebook", "laptop", "variable"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
         "Game over.The word was:,word_to_guess"
         display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman Game!")
    word_to_guess = get_random_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nWord to guess: ", display_word(word_to_guess, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess.")
            attempts -= 1
            print(f"Attempts left: {attempts}")

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    else:
        print("\nGame over. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()