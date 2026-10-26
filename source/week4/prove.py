print("-"*30)
childprice = float(input("What is the price of a child's meal? $"))

adultprice = float(input("What is the price of an adult's meal? $"))

drinkprice = float(input("What is the price of a drink? $"))

child = int(input("How many children are with you? "))

adult = int(input("How many adults are with you? "))

drink = int(input('How many drinks would you like? '))

tax = float(input('What is the sales tax rate? %'))

total = (childprice * child) + (adultprice * adult) + (drinkprice * drink)

taxamount = round(total * (tax / 100),2)

print(f"\nYour total will be ${total:.2f} before sales tax")
print(f"Your sales tax will be ${taxamount:.2f}\n")

tip = input('Would you like to add a tip? ').lower()

if tip == "yes":
    tip_amount = float(input("How much would you like to tip? yes or no $"))

elif tip == "no":
    tip_amount = 0

finaltotal = total + taxamount + tip_amount

print(f"Your final total will be ${finaltotal:.2f}\n")

payment = float(input("How much cash are you using to pay? $"))

change = round(payment - finaltotal, 2)

print(f"\nYour change is ${change:.2f}\n")

print('Enjoy! Have a nice day!')

print("-"*30)
