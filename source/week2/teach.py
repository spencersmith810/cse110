"""
Team activity for week 2 - asking for an ID Badge
Spencer Smith
"""
print('Please input the following information:\n')

first = input("First Name: ")
last = input('Last Name: ')
email = input('Email Address: ')
phone = input('Phone Number: ')
job = input('Job Title: ')
idnumber = input('School ID Number: ')

print('\nWhat is your favorite:')

candy = input('Candy: ')
bevy = input('Beverage: ')
movie = input('Movie: ')
fav_color = input('Color: ')

phone = f"({phone[:3]}){phone[3:6]}-{phone[6:]}"


print('\nThe ID Card is:')
print("-"*30)
print(f'{last.upper()}, {first.capitalize()}\n{job.title()}\nID: {idnumber}\n\n{email.lower()}\n{phone}\n\n')
print('Your favorites are...\n'
    f"Candy: {candy.title():<30}Beverage: {bevy.title()}\n"
    f"Movie: {movie.title():<30}Color: {fav_color.title()}"
)
print("-"*30)