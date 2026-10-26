print("-"*30)
print('Hello, I have a few questions for you! Please answer:')

first_n = float(input("Can you please type one number: "))
second_n = float(input("Can you please type another number: "))

if first_n> second_n:
    print("\nThe first number is greater")
else:
    print("The first number is not greater")

if first_n == second_n:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_n > first_n:
    print("The second number is greater")
else:
    print("The second number is not greater")

print('\nNext question!: ')

fav_animal = "sheep"

their_animal = input("What is your favorite animal?").strip().lower()

if their_animal == fav_animal:
    print('We have the same favorite animal!')
else:
    print('This is not my favorite animal...')

print("-"*30)
