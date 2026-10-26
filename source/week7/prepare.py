number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")
print()

answer = input("May I have a piece of candy? ").strip().lower()

while answer != "yes":
    answer = input("May I have a piece of candy? ").strip().lower()

print("Thank you.")
