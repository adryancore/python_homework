def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        display = ""

        for char in secret_word:
            if char.lower() in guesses:
                display += char
            else:
                display += "_"
        
        print(display)
        return all(char.lower() in guesses for char in secret_word)

    return hangman_closure

# --- Game Logic ---
if __name__ == "__main__":
    secret = input("Enter the secret word: ").strip()
    hangman = make_hangman(secret)

    print("\nLet’s play Hangman!\n")

    while True:
        guess = input("Guess a letter: ").strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if hangman(guess):
            print("\n🎉 You guessed the word!")
            break
