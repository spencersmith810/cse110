print()
print("Hello! I would like to ask you a few questions!")

print("Question 1: \n")
age = input("How old are you?")
age = float(age)
age = (age+1)
print(f"For your next birthday, you will be turning {age}\n")

print("Question 2: \n")
egg = input("How many DOZENS of eggs do you have?")
egg = float(egg)
egg = egg * 12
print(f"You have {egg} eggs\n")

print("Question 3 & 4: \n")
cookie = input("How many cookies do you have?")
cookie = float(cookie)
people = input("How many people are with you?")
people = float(people)
div = (cookie/people)
print(f"This means, each of your {people} friends can eat {div} cookies!")