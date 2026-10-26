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

print("\nPlease choose two supplies to take on your adventure.")
print("Available supplies:", ", ".join(available_items))

while len(backpack) < 2:
    item = get_choice("\nWhat would you like to pack? (one at a time) ", available_items)

    backpack.append(item)
    available_items.remove(item)

    print("Your backpack:", ", ".join(backpack))

starter = get_choice("\nTime to pick your Pokemon:\nPIKACHU, CHARMANDER, or BULBASAUR\n> ", ["pikachu", "charmander", "bulbasaur"])

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
    choice_one = get_choice("\nWhile on your search with Pikachu, you reach a river. Do you CROSS the stepping stones or FOLLOW the riverbank? ", ["cross", "follow"])

    if choice_one == "cross":
        choice_one_one = get_choice("\nEevee is stranded on a small island. Do you BUILD a bridge or CALL to it? ", ["build", "call"])

        if choice_one_one == "build":
            print(
                "\nYou built the bridge and offered Eevee a safe path across! It is SAVED!!!"
            )
        elif choice_one_one == "call":
            print(
                "\nYou called to Eevee, causing Eevee to jump across. Eevee landed in the water soaking you both! Eevee is saved!"
            )
        else:
            print("\nInvalid choice. Choose BUILD or CALL.")

    elif choice_one == "follow":
        while True:
            choice_one_two = get_choice("\nA nervous Psyduck blocks the way to Eevee. Do you OFFER a berry or WAIT? ", ["offer", "wait"])

            if choice_one_two == "offer":
                if "berry" in backpack:
                    print("\nYou offered Psyduck a berry. It was grateful and helped you save Eevee!")
                    break
                else:
                    print("\nYou didn't pack a berry! Choose WAIT to try another route.")

            elif choice_one_two == "wait":
                print("\nPsyduck waddled away. You saved Eevee, but it took much longer.")
                break
    else:
        print("\nInvalid choice. Choose CROSS or FOLLOW.")

elif starter == "charmander":
    choice_two = get_choice("\nCharmander lights up a cave entrance. Do you ENTER the cave or CLIMB the hill above it? ", ["enter", "climb"])

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
            choice_two_two = get_choice("\nYou spot Eevee on a narrow ledge. Do you LOWER a rope or FIND another route? ", ["lower", "find"])

            if choice_two_two == "lower":
                if "rope" in backpack:
                    print("\nYou use your rope to bring Eevee safely up.")
                    break
                else:
                    print("\nYou didn't pack a rope! Choose FIND to try another route.")

            elif choice_two_two == "find":
                print("\nA hidden trail leads you to Eevee. You also find a rare berry tree. SCORE!!")
                break
    else:
        print("\nInvalid choice. Choose ENTER or CLIMB.")

elif starter == "bulbasaur":
    choice_three = get_choice("\nBulbasaur discovers tracks near thick bushes. Do you TRACK the footprints or SEARCH the bushes? ", ["track", "search"])

    if choice_three == "track":
        choice_three_one = get_choice("\nEevee's paw is caught under a branch! Do you LIFT it or use VINE to pull it away? ", ["lift", "vine"])

        if choice_three_one == "lift":
            print("\nYou lift the branch and free Eevee, but get super muddy!")
        elif choice_three_one == "vine":
            print("\nBulbasaur's vine frees Eevee and reveals a buried Poke Ball.")
            backpack.append("Poke Ball")
        else:
            print("\nInvalid choice. Choose LIFT or VINE.")

    elif choice_three == "search":
        while True:
            choice_three_two = get_choice("\nEevee is tangled in thorny vines. Do you CUT the vines or UNTANGLE them? ", ["cut", "untangle"])

            if choice_three_two == "cut":
                if "knife" in backpack:
                    print("\n You use the knife to cut Eevee free! The knife scares off Eevee. You saved it but at what cost...")
                    break
                else:
                    print("\nYou didn't pack a knife! Choose UNTANGLE to try another route.")
            elif choice_three_two == "untangle":
                print("\nUntangling takes much longer, but Eevee becomes your friend!")
                break

    else:
        print("\nInvalid choice. Choose TRACK or SEARCH.")

else:
    print("\nInvalid choice. Please choose PIKACHU, CHARMANDER, or BULBASAUR.")

print("\n" + "-" * 40)
print("\nItems you collected:")
if backpack:
    for item in backpack:
        print("- " + item)
else:
    print("Your backpack is empty.")

print("Thank you for playing Rescue Eevee!")
print("Come back soon for another Pokemon adventure!")
print("-" * 40)
