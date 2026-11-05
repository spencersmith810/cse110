word = "Commitment"

print("The letter m is capitalized:")

for letter in word:
    if letter.lower() == "m":
        print(letter.upper())
    else:
        print(letter.lower())


print()
favorite_letter = input("What is your favorite letter? ")

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()


print()
favorite_letter = input("What letter would you like to hide? ")

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()


print()
print("Stretch challenge")
quote = (
    "In coming days, it will not be possible to survive spiritually "
    "without the guiding, directing, comforting, and constant influence "
    "of the Holy Ghost."
)

again = "yes"
while again == "yes":
    number = int(input("Please enter a number: "))
    letter_count = 0

    for position, letter in enumerate(quote):
        if letter.isalpha():
            letter_count += 1

        if letter.isalpha() and letter_count % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter, end="")
    print()

    again = input("Would you like to enter another number? ").lower()

print("Goodbye")
