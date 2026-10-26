intro_info=input('\nMy name is Spencer Smith, I wanted to ask you a question. \nIs that okay? (yes or no)\n')

if intro_info == "yes":
    user_favoritecolor=input('\nWonderful! I was wondering, whats your favorite color?\n')
    print(f"\nI also really love {user_favoritecolor.lower()}! Thank you for answering!\n")

if intro_info == "no":
    print(f"\nWell then, why are you here?\n")