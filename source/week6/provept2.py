print("\n" + "-" * 40)
print("     RESCUE EEVEE: WHISPERING WOODS")
print("-" * 40)
print("\nYou hear that an Eevee is lost in Whispering Woods.")


def get_choice(promt, valid_choices):
    while True:
        answer = input(promt).strip().lower()

        if answer in valid_choices:
            return answer

        print("Invalid choice. Please choose:", ", ".join(valid_choices))


available_items = ["rope", "berry", "knife"]
backpack = []
trust = 1

print("\nPlease choose two supplies to take on your adventure.")
print("Available supplies:", ", ".join(available_items))

while len(backpack) < 2:
    item = get_choice("\nWhat would you like to pack? (one at a time) ", available_items)

    backpack.append(item)
    available_items.remove(item)

    print("Your backpack:", ", ".join(backpack))

starter = get_choice("\nTime to pick your Pokemon:\nPIKACHU, CHARMANDER, or BULBASAUR\n> ", ["pikachu", "charmander", "bulbasaur"])

name =get_choice("\nWould you like to name your Pokemon? YES or NO: ", ["yes", "no"])

if name == "no":
    pokemon_name = starter
        
elif name == "yes":
    pokemon_name = input("\nWhat would you like to name your Pokemon? ").strip()

print(f"\nYou and {pokemon_name.capitalize()} are ready for an adventure!")

if starter == "pikachu":
    print("\nNice pick!!\n"r"""
⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋⠀⠀
""")
elif starter == "charmander":
    print("\nHere is your pokemon!\n"r"""
⠀⠀⠀⠀⠀⠀⣀⠤⠄⠒⠒⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡰⠊⠁⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⢡⡄⠀⠀⠀⠀⢀⡴⢠⢦⡈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⢋⠃⠀⠀⠀⠀⠀⠁⣧⣸⣧⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⡿⢿⠀⠀⠀⠀⠀⠀⠀⣟⠛⣹⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡟⠚⠀⠀⠀⠀⠀⠀⠀⠈⠉⢀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡀⠀⠀
⠀⠀⢸⡙⢶⣤⣄⣀⣀⣀⣤⡤⠲⡿⠁⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣼⠿⣿⡀⠀
⠀⠀⠀⠙⠢⣍⡓⢤⣴⣋⣉⡭⠛⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⠿⠀⠀⡇⠀
⠀⠀⠀⠀⠀⣀⡬⢿⠃⣻⡶⣆⡀⠀⠈⠉⠒⠦⢄⡀⠀⠀⠀⠀⠀⠀⣠⠇⠀⠀⠀⣷⠀
⣴⣶⠶⠒⠉⠀⠀⢸⠞⠁⠀⠀⠙⢆⠀⠀⠀⠀⠀⠈⠉⠚⣿⡶⠀⢰⠃⠀⠀⠀⢠⣿⣄
⠉⢻⣄⣀⡀⠀⢀⡾⠀⠀⠀⠀⠀⠈⢧⣀⣀⠀⠀⠀⣿⡧⠾⠗⠀⠀⢧⡀⠀⠀⠀⣡⠇
⠀⠉⠁⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠈⡆⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠳⣤⣀⠞⠁⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⡰⠃⡄⠀⠀⠀
⠀⠀⠀⠀⢀⡠⠚⡇⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⢳⡀⠀⠀⠀⣠⠞⠁⣠⡇⠀⠀⠀
⠀⠀⠀⢀⠎⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢳⠒⠈⠉⠀⢀⣴⡟⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠀⠀⠈⠣⢄⡀⠀⠀⠀⢇⠀⠀⠀⠀⠀⢸⡀⣀⡠⠔⡩⠞⠀⠀⠀⠀⠀
⠀⠀⠀⣈⣧⡀⠀⠀⠀⢠⠔⠛⠓⠒⠒⠚⠧⡀⠀⠀⠀⠈⡯⠄⠒⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣟⣶⣳⠤⠤⠔⠊⠀⠀⠀⠀⠀⠀⠀⢹⡀⢀⣀⣀⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢚⣾⣷⣟⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

elif starter == "bulbasaur":
    print("\nHere is your pokemon!\n"r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀
⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀
⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀
⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀
⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈
⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰
⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀
⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀
⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀
⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀
""")

if starter == "pikachu":
    choice_one = get_choice(f"\nWhile on your search with {pokemon_name.capitalize()}, you reach a river. Do you CROSS the stepping stones or FOLLOW the riverbank? ", ["cross", "follow"])

    if choice_one == "cross":
        choice_one_one = get_choice("\nEevee is stranded on a small island. Do you BUILD a bridge or CALL to it? ", ["build", "call"])

        if choice_one_one == "build":
            print(
                "\nYou built the bridge and offered Eevee a safe path across! Eevee is SAVED!!!"
            )
        elif choice_one_one == "call":
            print(
                "\nYou called to Eevee, causing Eevee to jump across. Eevee landed in the water soaking you both! Eevee is saved!"
            )
        else:
            print("\nInvalid choice. Choose BUILD or CALL.")

    elif choice_one == "follow":
        while True:
            choice_one_two = get_choice("\nA nervous Psyduck blocks the way to Eevee. Do you OFFER a berry, WAIT, or use SPARK to make a friendly light show? ", ["offer", "wait", "spark"])
            if choice_one_two == "offer":
                if "berry" in backpack:
                    backpack.remove("berry")
                    print("\nYou offered Psyduck a berry. It was grateful and helped you save Eevee!")
                    break
                else:
                    print("\nYou didn't pack a berry! Choose WAIT or SPARK.")

            elif choice_one_two == "wait":
                print("\nPsyduck waddled away. You saved Eevee, but it took much longer.")
                break
            elif choice_one_two == "spark":
                print(f"\n{pokemon_name.capitalize()} sends tiny sparks into the air.")
                print("Psyduck enjoys the light show and helps you reach Eevee!")
                trust += 1
                break
    else:
        print("\nInvalid choice. Choose CROSS or FOLLOW.")

elif starter == "charmander":
    choice_two = get_choice(f"\n{pokemon_name.capitalize()} lights up a cave entrance. Do you ENTER the cave or CLIMB the hill above it? ", ["enter", "climb"])

    if choice_two == "enter":
        choice_two_one = get_choice("\nEevee is hiding behind a sleeping Onix. Do you SNEAK past or DISTRACT Onix? ", ["sneak", "distract"])

        if choice_two_one == "sneak":
            print("\nYou quietly rescue Eevee, and Onix doesn't notice.")
        elif choice_two_one == "distract":
            print(
                "\nOnix wakes up! But he is kind and helps you get Eevee safely back!"
            )
        else:
            print("\nInvalid choice. Choose SNEAK or DISTRACT.")

    elif choice_two == "climb":
        while True:
            choice_two_two = get_choice("\nYou spot Eevee on a narrow ledge. Do you LOWER a rope, FIND another route, or use GLOW to light the path? ", ["lower", "find", "glow"])

            if choice_two_two == "lower":
                if "rope" in backpack:
                    trust+=2
                    print("\nYou use your rope to bring Eevee safely up.")
                    break
                else:
                    print("\nYou didn't pack a rope! Choose FIND or GLOW.")

            elif choice_two_two == "find":
                print("\nA hidden trail leads you to Eevee. You also find a rare berry tree. SCORE!!")
                break
            elif choice_two_two == "glow":
                print(f"\n{pokemon_name.capitalize()} raises its glowing tail.")
                print("The light reveals a safe trail to the ledge. You guide Eevee back!")
                trust += 1
                break
    else:
        print("\nInvalid choice. Choose ENTER or CLIMB.")

elif starter == "bulbasaur":
    choice_three = get_choice(f"\n{pokemon_name.capitalize()} discovers tracks near thick bushes. Do you TRACK the footprints or SEARCH the bushes? ", ["track", "search"])

    if choice_three == "track":
        print("\nYou follow the footprints to a gap in the trail.")

        if "rope" in backpack:
            print("You secure your rope around a tree and cross safely.")
        else:
            print(f"You didn't pack a rope, but {pokemon_name.capitalize()} has an idea!")
            print(f"{pokemon_name.capitalize()} stretches its vines across the gap.")
            print("You hold onto the vines and cross safely!")

        choice_three_one = get_choice("\nEevee's paw is caught under a branch! Do you LIFT it or use VINE to pull it away? ", ["lift", "vine"])

        if choice_three_one == "lift":
            print("\nYou lift the branch and free Eevee, but get super muddy!")
        elif choice_three_one == "vine":
            print(f"\n{pokemon_name.capitalize()}'s vine frees Eevee and reveals a buried Poke Ball.")
            backpack.append("Poke Ball")
        else:
            print("\nInvalid choice. Choose LIFT or VINE.")

    elif choice_three == "search":
        while True:
            choice_three_two = get_choice("\nEevee is tangled in thorny vines. Do you CUT the vines or UNTANGLE them? ", ["cut", "untangle"])

            if choice_three_two == "cut":
                if "knife" in backpack:
                    trust-=1
                    print("\n You use the knife to cut Eevee free! The knife scares off Eevee. You saved it but at what cost...")
                    break
                else:
                    print("\nYou didn't pack a knife! Choose UNTANGLE to try another route.")
            elif choice_three_two == "untangle":
                trust +=2
                print("\nUntangling takes much longer, but Eevee becomes your friend!")
                break

    else:
        print("\nInvalid choice. Choose TRACK or SEARCH.")

else:
    print("\nInvalid choice. Please choose PIKACHU, CHARMANDER, or BULBASAUR.")

if "berry" in backpack:
    berry_choice = get_choice("\nBefore you leave, Eevee sniffs the berry in your backpack. Do you FEED Eevee or KEEP it? ", ["feed", "keep"])

    if berry_choice == "feed":
        backpack.remove("berry")
        trust += 2
        print("\nEevee happily eats the berry and lets you scratch behind its ears!")
    else:
        print("\nYou save the berry for another adventure.")

print("\n" + "-" * 40)
print("\nItems in your backpack:")
if backpack:
    for item in backpack:
        print("- " + item)
else:
    print("Your backpack is empty.")

print("\nAs you leave the woods, Eevee looks back at you...")

if trust >= 3:
    if starter == "pikachu":
        evolution = "Jolteon"
    elif starter == "charmander":
        evolution = "Flareon"
    else:
        evolution = "Leafeon"

    print("\nA mysterious light surrounds Eevee...")
    print(f"Your bond with {pokemon_name.capitalize()} helped Eevee evolve into {evolution}!")
    print("Eevee nuzzles your hand and follows you home!\n")
    print("You gained a new Pokemon Companion!")
elif trust >= 1:
    print("Eevee gives a happy cry before returning to the woods.")
else:
    print("Eevee hurries into the bushes. Perhaps next time, be gentler.")

print("\nEevee is safe and sound!\n"r"""
⠀⠀⠀⠀⠀⠀⣀⣠⣤⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣧
⠀⠀⣀⣤⣶⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⣼
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⢷⣆⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⣿
⣾⣿⣿⣟⢛⣛⣛⣛⣋⠭⠥⠿⣿⣿⣷⣤⠀⠀⠀⢀⣀⣀⣠⣀⡀⢿⡇⠀⣸⡇
⣿⣿⣿⠻⢧⠙⢯⡀⠈⠉⠙⠛⠳⢦⣝⢿⣷⢠⣾⣿⣿⣿⣿⣿⣯⣬⡥⢰⡟⠀
⢹⣯⣛⠯⢿⣾⣷⣍⡳⣤⣀⠀⠀⠀⠉⠳⣍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀
⠈⠹⣿⣿⣾⣿⣿⣿⣿⣷⣭⣛⠷⢦⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⢋⣵⡾⣣⣤⣦⢻⣿⣿⣿⣻⠻⣿⣿⣿⡏⠖⢻⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⣱⣿⡟⠼⣻⣿⣿⢸⣿⣿⡇⡛⠀⣿⣿⣿⣧⡠⣸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⢹⣿⣿⣿⣏⢿⣿⣷⣕⣧⣿⣿⣿⢿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣠⢿⣿⡟⣿⣷⣭⣻⠿⢿⠿⠷⢞⣫⣵⠿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡟⣎⢿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⠁⠻⣷⡝⣩⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⣿⣿⣿⠉⠙⢻⢟⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡀⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⢿⡧⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀
""")

print(f"You and {pokemon_name.capitalize()} make a great team!")
print("Thank you for playing Rescue Eevee!")
print("Come back soon for another Pokemon adventure!")
print("-" * 40)
