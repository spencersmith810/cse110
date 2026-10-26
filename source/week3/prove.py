print("-"*30)
childprice = input("What is the price of a child's meal? $")
childprice = float(childprice)

adultprice = input("What is the price of an adult's meal? $")
adultprice = float(adultprice)

drinkprice = input("What is the price of a drink? $")
drinkprice = float(drinkprice)

child = input("How many children are with you? ")
child = int(child)

adult = input("How many adults are with you? ")
adult = int(adult)

drink = input('How many drinks would you like? ')
drink = int(drink)

tax = input('What is the sales tax rate? %')
tax = float(tax)

total = (childprice * child) + (adultprice * adult) + (drinkprice * drink)

taxamount = round(total * (tax / 100),2)

finaltotal = round(total + taxamount, 2)

print(f"\nYour total will be ${total:.2f} before sales tax")
print(f"Your total will be ${finaltotal:.2f}\n")

payment = input("How much cash are you using? ")
payment = float(payment)

change = round(payment - (total + taxamount),2)

print(f"\nYour change is ${change:.2f}\n")

print('Enjoy! Have a nice day!')

print("-"*30)