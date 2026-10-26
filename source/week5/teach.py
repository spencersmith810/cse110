width = 30

print("\n" + "-" * width)
print("Did you pass your class??".center(width))
print("-" * width)
print("Let's check...\n".center(width))

grade = float(input("\nWhat percentage grade did you get?: "))

passing = float(input("\nWhat percentage is passing the class?: "))

if grade >= 90:
    print("\nYou got an A in your class!!!")

elif grade >= 80:
    print("\nYou got a B in your class!")

elif grade >= 70:
    print("\nYou got a C in your class.")

elif grade >= 60:
    print("\nYou got a D in your class :(")

elif grade < 60:
    print("\nYou got a F in your class...")

if grade >=passing:
    print("\nYou passed the class!\n")
    
elif grade < passing:
    print("\nYou failed... :( \n\nWOMP WOMP")

if grade >= 90:
    letter = "A"

elif grade >= 80:
    letter = "B"

elif grade >= 70:
    letter = "C"

elif grade >= 60:
    letter = "D"

else:
    letter = "F"

if grade >= 93:
    letter = "A"

elif grade >= 90:
    letter = "A-"

elif grade >= 87:
    letter = "B+"

elif grade >= 83:
    letter = "B"

elif grade >= 80:
    letter = "B-"

elif grade >= 77:
    letter = "C+"

elif grade >= 73:
    letter = "C"

elif grade >= 70:
    letter = "C-"

elif grade >= 67:
    letter = "D+"

elif grade >= 60:
    letter = "D"
    
else:
    letter = "F"

print(f"\nYour letter grade is {letter}. Go tell your parents!\n")

print(f"\nYour letter grade is {letter}. Go tell your parents!\n")
