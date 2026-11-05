import math
import random
import shutil
import time


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
GOLD = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
MAGENTA = "\033[95m"

MAX_ATTEMPTS = 6
HINT_COST = 25

CATEGORIES = {
    "1": ("Book of Mormon", [
        "nephi", "jacob", "enos", "jarom", "omni", "mormon",
        "mosiah", "alma", "helaman", "ether", "moroni",
    ]),
    "2": ("Bible", [
        "genesis", "exodus", "jonah", "ruth", "luke", "john",
        "paul", "james", "peter", "revelation",
    ]),
    "3": ("General Vocabulary", [
        "rocket", "forest", "planet", "puzzle", "wizard", "thunder",
        "comet", "castle", "dragon", "journey",
    ]),
}

CATEGORY_STYLES = {
    "Book of Mormon": (GOLD, "THE SACRED ARCHIVES"),
    "Bible": (CYAN, "THE ANCIENT KINGDOM"),
    "General Vocabulary": (MAGENTA, "THE WILDLANDS"),
}

LORE = {
    "Book of Mormon": "The archive remembers every faithful seeker.",
    "Bible": "Ancient pages turn as the kingdom watches.",
    "General Vocabulary": "Beyond the map, strange words guard hidden treasure.",
}

LOCATIONS = ["The Village", "The Whispering Woods", "The Crystal Library", "The Final Gate"]


def type_text(message, delay=0.015):
    """Print a message one character at a time."""
    for character in message:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def show_title():
    print(f"{CYAN}╔{'═' * 58}╗")
    print(f"║{BOLD}{'WORD QUEST: THE GRAND ADVENTURE'.center(58)}{RESET}{CYAN}║")
    print(f"║{'Guess wisely. Discover boldly.'.center(58)}║")
    print(f"╚{'═' * 58}╝{RESET}")
    show_stars()


def show_category_title(category_name):
    color, title = CATEGORY_STYLES[category_name]
    stars = "✦  ·  ✧  ·  ✦  ·  ✧  ·  ✦"
    print(f"{color}{stars.center(58)}{RESET}")
    print(f"{color}{BOLD}{title.center(58)}{RESET}")
    print(f"{color}{stars.center(58)}{RESET}")


def show_quest_map(location_index):
    print()
    print(f"{BOLD}QUEST MAP{RESET}")
    for index, location in enumerate(LOCATIONS):
        if index < location_index:
            marker = f"{GREEN}✓{RESET}"
        elif index == location_index:
            marker = f"{GOLD}➤{RESET}"
        else:
            marker = f"{GRAY}○{RESET}"
        print(f"  {marker} {location}")


def narrator(message):
    type_text(f"{CYAN}Narrator:{RESET} {message}", delay=0.01)


def villain(message):
    type_text(f"{RED}The Word Warden:{RESET} {message}", delay=0.01)


def show_stars():
    print(f"{CYAN}      .       *        .       ✦       .{RESET}")
    print(f"{GRAY}   *       .       ✧       .       *{RESET}")


def show_progress_bar(attempts_left):
    color = GREEN if attempts_left >= 4 else GOLD if attempts_left >= 2 else RED
    bar = "█" * attempts_left + "░" * (MAX_ATTEMPTS - attempts_left)
    print(f"{color}POWER [{bar}] {attempts_left}/{MAX_ATTEMPTS}{RESET}")


def mascot_reacts(won, close=False):
    if won:
        print(f"{GOLD}  /\\_/\\   The mascot celebrates!{RESET}")
        print(f"{GOLD} ( o.o )   \"You found it!\"{RESET}")
    elif close:
        print(f"{CYAN}  /\\_/\\   The mascot leans closer...{RESET}")
        print(f"{CYAN} ( o.o )   \"Almost there!\"{RESET}")
    else:
        print(f"{GRAY}  /\\_/\\   The mascot looks thoughtful.{RESET}")
        print(f"{GRAY} ( -.- )   \"Try another path.\"{RESET}")


def show_lightning():
    for frame in ("      \\ | /", "       \\|/", "        /\\"):
        print(f"{GOLD}{frame}{RESET}")
        time.sleep(0.08)
    type_text(f"{GOLD}LIGHTNING STRIKES! You are one letter away!{RESET}", delay=0.01)


def screen_shake():
    for offset in ("", "  ", "", " "):
        print(f"\033[2K\r{RED}{offset}~ incorrect guess ~{RESET}", end="", flush=True)
        time.sleep(0.06)
    print()


def show_rain():
    print(f"{CYAN}     |  /  |  /  |  /  |  /  |{RESET}")
    print(f"{CYAN}   /  |  /  |  /  |  /  |  /{RESET}")
    print(f"{GRAY}        The storm closes over the quest...{RESET}")


def show_treasure_chest(reward):
    print(f"{GOLD}       _____________{RESET}")
    print(f"{GOLD}      /             \\{RESET}")
    print(f"{GOLD}     /_______________\\{RESET}")
    print(f"{GOLD}     |   [  ✦  ]    |{RESET}")
    print(f"{GOLD}     |_______________|{RESET}")
    type_text(f"Treasure discovered: {reward}!", delay=0.02)


def show_level_up(level):
    print(f"{MAGENTA}★ ★ ★  LEVEL UP  ★ ★ ★{RESET}")
    type_text(f"You are now Quest Level {level}!", delay=0.02)


def random_event():
    events = [
        "A friendly guide gives you a small lantern.",
        "You discover a shortcut and gain confidence.",
        "The Word Warden leaves behind a mysterious clue.",
        "A quiet page whispers: patience reveals patterns.",
    ]
    narrator(random.choice(events))


def branch_story():
    print("1. Follow the glowing path")
    print("2. Search the old library")
    choice = input("Choose your path: ").strip()
    if choice == "2":
        narrator("The library rewards careful readers with deeper clues.")
        return "library"
    narrator("The glowing path leads bravely toward the next challenge.")
    return "path"


def show_encyclopedia(category_name, words):
    print(f"{BOLD}BOOK OF KNOWLEDGE: {category_name}{RESET}")
    print("Known words in this chapter: " + ", ".join(words[:5]) + "...")
    type_text(LORE[category_name], delay=0.01)


def show_ending(score, wins):
    if score >= 150:
        ending = "Legendary ending: the kingdom names a star after you."
    elif wins >= 2:
        ending = "Heroic ending: the archive opens its hidden chamber."
    else:
        ending = "Hopeful ending: every quest has taught you something new."
    type_text(f"{BOLD}{ending}{RESET}", delay=0.01)


def choose_category():
    print()
    type_text("Choose your word category:")
    print("1. Book of Mormon")
    print("2. Bible")
    print("3. General vocabulary")

    choice = input("Category: ").strip()
    if choice not in CATEGORIES:
        print("Unknown choice, so Book of Mormon was selected.")
        choice = "1"

    return CATEGORIES[choice]


def make_hint(secret_word, guess):
    """Create colored feedback for a guess."""
    hint = []
    correct_positions = 0

    for index, letter in enumerate(secret_word):
        if guess[index] == letter:
            hint.append(f"{GREEN}{letter.upper()}{RESET}")
            correct_positions += 1
        elif guess[index] in secret_word:
            hint.append(f"{GOLD}{guess[index]}{RESET}")
        else:
            hint.append(f"{GRAY}_{RESET}")

    return hint, correct_positions


def show_hint(hint):
    print("Hint: ", end="")
    for letter in hint:
        print(letter, end=" ")
    print()


def rank_for(guess_count, used_hint, bonus_won):
    if bonus_won:
        return "Bonus Word Champion"
    if guess_count == 1 and not used_hint:
        return "Scripture Scholar"
    if guess_count <= 3:
        return "Faithful Seeker"
    return "New Reader"


def rank_color(rank):
    if rank == "Scripture Scholar":
        return GOLD
    if rank == "Bonus Word Champion":
        return MAGENTA
    if rank == "Faithful Seeker":
        return GREEN
    return CYAN


def show_countdown():
    type_text("Preparing your victory celebration...", delay=0.02)
    for number in range(3, 0, -1):
        print(f"{GOLD}{number}...{RESET}", end=" ", flush=True)
        time.sleep(0.35)
    print(f"{GREEN}GO!{RESET}")


def show_fireworks(rank, shape="star"):
    """Display colored fireworks selected for the player's rank."""
    size = shutil.get_terminal_size()
    width = max(1, min(size.columns - 1, 80))
    height = max(1, min(size.lines - 2, 24))
    colors = {
        "Scripture Scholar": [93, 97, 96],
        "Bonus Word Champion": [95, 93, 96],
        "Faithful Seeker": [92, 96, 93],
        "New Reader": [96, 94, 93],
    }

    if width < 20 or height < 10:
        print(f"{rank_color(rank)}YOU GOT IT! {rank}{RESET}")
        return

    particles = []
    launch_x = width // 2
    burst_y = height // 3
    launch_frames = height - 4 - burst_y + 1

    try:
        print("\033[2J\033[?25l", end="", flush=True)
        for frame in range(launch_frames + 90):
            screen = [[" " for _ in range(width)] for _ in range(height)]
            firework_frame = frame - launch_frames

            if frame < launch_frames:
                rocket_y = height - 4 - frame
                screen[rocket_y][launch_x] = f"{GOLD}^{RESET}"
                screen[rocket_y + 1][launch_x] = f"{GOLD}|{RESET}"
                screen[rocket_y + 2][launch_x] = f"{RED}*{RESET}"

            if firework_frame >= 0 and firework_frame % 18 == 0:
                x = random.randint(5, width - 6)
                y = random.randint(2, height // 2)
                color = random.choice(colors[rank])

                for _ in range(40):
                    angle = random.uniform(0, math.tau)
                    speed = random.uniform(0.2, 1.2)
                    particles.append({
                        "x": x,
                        "y": y,
                        "vx": math.cos(angle) * speed * 2,
                        "vy": math.sin(angle) * speed,
                        "life": random.randint(15, 30),
                        "color": color,
                    })

            for spark in particles:
                spark["x"] += spark["vx"]
                spark["y"] += spark["vy"]
                spark["vy"] += 0.035
                spark["life"] -= 1
                x = int(spark["x"])
                y = int(spark["y"])

                if 0 <= x < width and 0 <= y < height:
                    shapes = {
                        "star": ("✦", "."),
                        "heart": ("♥", "."),
                        "spiral": ("@", "o"),
                    }
                    symbol = shapes[shape][0] if spark["life"] > 12 else shapes[shape][1]
                    screen[y][x] = (
                        f"\033[{spark['color']}m{symbol}{RESET}"
                    )

            particles = [spark for spark in particles if spark["life"] > 0]
            labels = [(height - 1, "LAUNCHING...")]
            if frame >= launch_frames:
                labels = [
                    (height // 2, "  VICTORY!  "),
                    (height // 2 + 2, f"  {rank}  "),
                ]

            for row, message in labels:
                message = message[:width]
                start = (width - len(message)) // 2
                for index, letter in enumerate(message):
                    screen[row][start + index] = letter

            print(f"\033[H{chr(10).join(''.join(row) for row in screen)}",
                  end="", flush=True)
            time.sleep(1 / 30)
    except KeyboardInterrupt:
        pass
    finally:
        print(f"\033[0m\033[?25h\033[{height + 1};1H", end="", flush=True)


def play_bonus_round(all_words):
    type_text("QUICK-WIN BONUS ROUND UNLOCKED!", delay=0.02)
    bonus_word = random.choice(all_words)
    bonus_guess = input(
        f"One bonus guess ({len(bonus_word)} letters): "
    ).lower()

    if bonus_guess == bonus_word:
        type_text("BONUS SUCCESS!", delay=0.02)
        return True

    type_text(f"The bonus word was {bonus_word.title()}.", delay=0.02)
    return False


def play_round(category_name, words, all_words, location_index):
    secret_word = random.choice(words)
    guess_count = 0
    score = 100
    used_hint = False
    hint_index = random.randrange(len(secret_word))
    hint_used_message = False

    show_quest_map(location_index)
    show_category_title(category_name)
    show_encyclopedia(category_name, words)
    type_text(f"Category: {category_name}")
    type_text(f"Your word has {len(secret_word)} letters.")
    type_text("Type 'hint' once for help. A hint costs 25 points.")
    villain("I have hidden a word in this realm. Can you reclaim it?")

    while guess_count < MAX_ATTEMPTS:
        guess = input(
            f"Guess {guess_count + 1}/{MAX_ATTEMPTS}: "
        ).strip().lower()

        if guess == "hint":
            if used_hint:
                type_text("You already used your hint token.")
            else:
                used_hint = True
                score -= HINT_COST
                type_text(
                    f"Hint: position {hint_index + 1} is "
                    f"'{secret_word[hint_index].upper()}'."
                )
            continue

        guess_count += 1
        score -= 10
        show_progress_bar(MAX_ATTEMPTS - guess_count)

        if len(guess) != len(secret_word):
            type_text(f"Your guess needs {len(secret_word)} letters.")
            screen_shake()
            mascot_reacts(False)
            continue

        if guess == secret_word:
            score += (MAX_ATTEMPTS - guess_count + 1) * 15
            mascot_reacts(True)
            return True, guess_count, max(score, 0), used_hint

        hint, correct_positions = make_hint(secret_word, guess)
        show_hint(hint)

        if len(secret_word) - correct_positions == 1:
            show_lightning()
            type_text("So close! Only one letter is out of place!")
            mascot_reacts(False, close=True)
        else:
            screen_shake()
            mascot_reacts(False)

        if not hint_used_message and used_hint:
            hint_used_message = True
            type_text("Keep going, seeker!")

    type_text(f"The secret word was {secret_word.title()}.")
    show_rain()
    return False, guess_count, 0, used_hint


def play_final_boss(all_words):
    villain("Final challenger! One word. One guess. No hints.")
    boss_word = random.choice(all_words)
    guess = input(f"FINAL BOSS ({len(boss_word)} letters): ").strip().lower()
    if guess == boss_word:
        type_text("The Word Warden has been defeated!", delay=0.02)
        return True
    type_text(f"The final boss word was {boss_word.title()}.", delay=0.02)
    return False


show_title()
type_text("Welcome to the most colorful word quest in the kingdom!", delay=0.02)

games_played = 0
wins = 0
losses = 0
total_guesses = 0
best_score = 0
bonus_wins = 0
treasures = []
level = 1
location_index = 0
final_boss_won = False
play_again = "yes"

while play_again == "yes":
    category_name, category_words = choose_category()
    all_words = [word for _, words in CATEGORIES.values() for word in words]
    branch_story()
    won, guesses, score, used_hint = play_round(
        category_name, category_words, all_words, location_index
    )

    games_played += 1
    total_guesses += guesses

    if won:
        wins += 1
        bonus_won = False
        if guesses <= 3:
            bonus_won = play_bonus_round(all_words)
            if bonus_won:
                bonus_wins += 1

        rank = rank_for(guesses, used_hint, bonus_won)
        best_score = max(best_score, score)
        show_countdown()
        firework_shape = random.choice(["star", "heart", "spiral"])
        type_text(f"Firework pattern: {firework_shape.title()}", delay=0.01)
        show_fireworks(rank, firework_shape)
        reward = random.choice(["a crystal key", "a silver compass", "a page of lore"])
        treasures.append(reward)
        show_treasure_chest(reward)
        level = 1 + wins // 2
        if wins > 1 and wins % 2 == 0:
            show_level_up(level)
        location_index = min(location_index + 1, len(LOCATIONS) - 1)
        if wins == 3:
            final_boss_won = play_final_boss(all_words)
        print(f"{rank_color(rank)}Rank: {rank}{RESET}")
        print(f"{rank_color(rank)}Score: {score}{RESET}")
    else:
        losses += 1
        print(f"{RED}QUEST OVER. Better luck next round!{RESET}")

    random_event()
    play_again = input("Play again? ").strip().lower()

print()
print(f"{CYAN}{'═' * 30}{RESET}")
type_text("FINAL QUEST STATISTICS")
print(f"Games played: {games_played}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Bonus wins: {bonus_wins}")
print(f"Treasures found: {len(treasures)}")
print(f"Quest level: {level}")
print(f"Final boss defeated: {'yes' if final_boss_won else 'no'}")
if games_played > 0:
    print(f"Average guesses: {total_guesses / games_played:.1f}")
print(f"Best score: {best_score}")
print(f"{CYAN}{'═' * 30}{RESET}")
show_ending(best_score, wins)
type_text("Thanks for playing Word Quest!")
