print("Amusement Park Ride Requirements")
print("Please enter heights in inches.\n")

age_one = int(input("What is the age of the first rider? "))
height_one = float(input("What is the height of the first rider? "))

if 12 <= age_one <= 17:
    passport_one = input("Does the first rider have a golden passport (yes/no)? ").strip().lower()
    if passport_one == "yes":
        age_one = 18

second_rider = input("Is there a second rider (yes/no)? ").strip().lower()
can_ride = False

if second_rider == "yes":
    age_two = int(input("What is the age of the second rider? "))
    height_two = float(input("What is the height of the second rider? "))

    if 12 <= age_two <= 17:
        passport_two = input("Does the second rider have a golden passport (yes/no)? ").strip().lower()
        if passport_two == "yes":
            age_two = 18

    if height_one >= 36 and height_two >= 36:
        if age_one >= 18 or age_two >= 18:
            can_ride = True
        elif age_one >= 12 and age_two >= 12 and height_one >= 52 and height_two >= 52:
            can_ride = True
        elif (age_one >= 16 and age_two >= 14) or (age_two >= 16 and age_one >= 14):
            can_ride = True

elif second_rider == "no":
    if age_one >= 18 and height_one >= 62:
        can_ride = True

if can_ride:
    print("\nWelcome to the ride. Please be safe and have fun!\n")
else:
    print("\nSorry, you may not ride.\n")
