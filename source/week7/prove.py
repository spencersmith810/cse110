# CSE 110 - Word Guessing Game
# Spencer Smith

secret_word = "mosiah"
guess = ""
guess_count = 0

print("Welcome to the word guessing game!")
print()

# Generate one underscore for each letter in the secret word.
hint = ""
for letter in secret_word:
    hint += "_ "
print(f"Your hint is: {hint}")

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if guess != secret_word:
        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            print()
        else:
            hint = ""

            for index in range(len(secret_word)):
                # Check the exact position before checking elsewhere in the word.
                if guess[index] == secret_word[index]:
                    hint += guess[index].upper() + " "
                elif guess[index] in secret_word:
                    hint += guess[index] + " "
                else:
                    hint += "_ "

            print(f"Your hint is: {hint}")

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
