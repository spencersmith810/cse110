secret_word = "mosiah"
max_attempts = 6
guess_count = 0

print("Guess the name of a book in the Book of Mormon.")
print(f"You have {max_attempts} guesses.")

while guess_count < max_attempts:
    guess = input("Your guess: ").lower()
    guess_count += 1

    if guess == secret_word:
        print(f"Correct! You guessed it in {guess_count} attempts.")
        break

    if len(guess) != len(secret_word):
        print(f"Your guess must have {len(secret_word)} letters.")
    else:
        hint = ""

        for index in range(len(secret_word)):
            if guess[index] == secret_word[index]:
                hint += guess[index].upper()
            elif guess[index] in secret_word:
                hint += guess[index]
            else:
                hint += "_"

        print(f"Hint: {hint}")
        print(f"Attempts left: {max_attempts - guess_count}")
else:
    print(f"You are out of guesses. The word was {secret_word}.")
