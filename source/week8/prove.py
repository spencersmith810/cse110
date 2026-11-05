import math
import random
import shutil
import time

CYAN = "\033[96m"
GOLD = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"
MAX_ATTEMPTS = 6

WORD_CATEGORIES = {
    "book of mormon": [
        "nephi", "jacob", "enos", "jarom", "omni", "mormon",
        "mosiah", "alma", "helaman", "ether", "moroni",
    ],
    "bible": [
        "genesis", "exodus", "jonah", "ruth", "luke", "john",
        "paul", "james", "peter", "revelation",
    ],
    "general": [
        "rocket", "forest", "planet", "puzzle", "wizard", "thunder",
        "comet", "castle", "dragon", "journey",
    ],
}


def type_text(text, delay=0.025):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def reveal_hint(letters, delay=0.18):
    print("\nYour hint is: ", end="", flush=True)
    for letter in letters:
        print(letter, end=" ", flush=True)
        time.sleep(delay)
    print("\n")


def get_atmosphere(attempts_left):
    if attempts_left >= 5:
        return CYAN, "The quest begins."
    elif attempts_left >= 3:
        return GOLD, "The pressure is rising!"
    elif attempts_left > 0:
        return RED, "Every guess counts!"
    else:
        return RED, "No attempts remaining."


def show_attempts(attempts_left, show_message=True):
    color, message = get_atmosphere(attempts_left)
    meter = "■" * attempts_left + "□" * (MAX_ATTEMPTS - attempts_left)
    print(f"{color}ATTEMPTS LEFT  [{meter}]  {attempts_left}{RESET}")
    if show_message:
        print(f"{color}{message}{RESET}")


def get_victory_rank(guess_count):
    if guess_count == 1:
        return "First-Try Legend"
    elif guess_count <= 3:
        return "Word Detective"
    elif guess_count <= 5:
        return "Steadfast Seeker"
    else:
        return "Last-Chance Hero"


def show_finale(rank):
    size = shutil.get_terminal_size()
    width = max(1, min(size.columns - 1, 80))
    height = max(1, min(size.lines - 2, 24))

    if width < 20 or height < 10:
        print(f"{GREEN}YOU GOT IT! {rank}{RESET}")
        return

    particles = []
    launch_x = width // 2
    burst_y = height // 3
    launch_frames = height - 4 - burst_y + 1

    try:
        print("\033[2J\033[?25l", end="", flush=True)

        for frame in range(launch_frames + 120):
            screen = [[" " for _ in range(width)] for _ in range(height)]
            firework_frame = frame - launch_frames

            if frame < launch_frames:
                rocket_y = height - 4 - frame
                screen[rocket_y][launch_x] = f"{GOLD}^{RESET}"
                screen[rocket_y + 1][launch_x] = f"{GOLD}|{RESET}"
                screen[rocket_y + 2][launch_x] = f"{RED}*{RESET}"

            if firework_frame >= 0 and firework_frame % 18 == 0:
                if firework_frame == 0:
                    x, y = launch_x, burst_y
                else:
                    x = random.randint(5, width - 6)
                    y = random.randint(2, height // 2)
                color = random.choice([91, 92, 93, 94, 95, 96])

                for _ in range(45):
                    angle = random.uniform(0, math.tau)
                    speed = random.uniform(0.2, 1.2)

                    particles.append({
                        "x": x,
                        "y": y,
                        "vx": math.cos(angle) * speed * 2,
                        "vy": math.sin(angle) * speed,
                        "life": random.randint(15, 35),
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
                    symbol = "*" if spark["life"] > 12 else "."
                    screen[y][x] = (
                        f"\033[{spark['color']}m{symbol}\033[0m"
                    )

            particles = [
                spark for spark in particles if spark["life"] > 0
            ]

            if frame < launch_frames:
                labels = [(height - 1, "LAUNCHING...")]
            else:
                labels = [
                    (height // 2, "  YOU GOT IT!  "),
                    (height // 2 + 2, f"  {rank}  "),
                ]

            for row, message in labels:
                message = message[:width]
                start = (width - len(message)) // 2
                for index, letter in enumerate(message):
                    screen[row][start + index] = letter

            picture = "\n".join("".join(row) for row in screen)
            print(f"\033[H{picture}", end="", flush=True)
            time.sleep(1 / 30)

    except KeyboardInterrupt:
        pass
    finally:
        print(
            f"\033[0m\033[?25h\033[{height + 1};1H",
            end="",
            flush=True,
        )


print(f"{BOLD}Choose a word category:{RESET}")
print("1. Book of Mormon")
print("2. Bible")
print("3. General vocabulary")
category_choice = input("Category: ").strip()

if category_choice == "2":
    category_name = "bible"
elif category_choice == "3":
    category_name = "general"
else:
    category_name = "book of mormon"

secret_word = random.choice(WORD_CATEGORIES[category_name])
guess = ""
guess_count = 0

print()
print(f"{CYAN}╔{'═' * 48}╗")
print(f"║{BOLD}{'WORD QUEST'.center(48)}{RESET}{CYAN}║")
print(f"║{'Discover the hidden book'.center(48)}║")
print(f"╚{'═' * 48}╝{RESET}")
print()

print(f"{BOLD}How to read your hint:{RESET}")
print(f"  {GREEN}UPPERCASE{RESET} = correct letter and position")
print(f"  {GOLD}lowercase{RESET} = correct letter, wrong position")
print(f"  {GRAY}_{RESET}         = letter is not in the word")
print()

type_text(f"Clue: Your category is {category_name.title()}.")
print(f"You have {MAX_ATTEMPTS} guesses. Every entry uses an attempt.")
print()

hint = ""
for letter in secret_word:
    hint += "_ "

print(f"The Book of {GOLD}{hint}{RESET}")
print()

while guess != secret_word and guess_count < MAX_ATTEMPTS:
    attempts_left = MAX_ATTEMPTS - guess_count
    theme_color, _ = get_atmosphere(attempts_left)
    print(f"{theme_color}{'─' * 50}{RESET}")
    show_attempts(attempts_left)
    guess = input(f"{theme_color}Guess #{guess_count + 1}{RESET} > ").lower()
    guess_count += 1

    if guess != secret_word:
        if len(guess) != len(secret_word):
            type_text(
                f"Your guess needs {len(secret_word)} letters.",
                delay=0.01,
            )
            print()
        else:
            hint_letters = []

            for index in range(len(secret_word)):
                if guess[index] == secret_word[index]:
                    hint_letters.append(f"{GREEN}{guess[index].upper()}{RESET}")
                elif guess[index] in secret_word:
                    hint_letters.append(f"{GOLD}{guess[index]}{RESET}")
                else:
                    hint_letters.append(f"{GRAY}_{RESET}")

            reveal_hint(hint_letters, delay=0.08)

if guess == secret_word:
    rank = get_victory_rank(guess_count)

    if guess_count <= 3:
        type_text("Quick victory detected! Bonus round unlocked!", delay=0.02)
        bonus_word = random.choice(
            [word for words in WORD_CATEGORIES.values() for word in words]
        )
        bonus_guess = input(
            f"Bonus word ({len(bonus_word)} letters, one guess): "
        ).lower()
        if bonus_guess == bonus_word:
            type_text("BONUS COMPLETE! Your legend grows!", delay=0.02)
            rank = "Bonus Word Champion"
        else:
            type_text(f"The bonus word was {bonus_word.title()}.", delay=0.02)

    show_finale(rank)
    result_color = GREEN
    result_title = "QUEST COMPLETE!"
    result_detail = f"Rank: {rank}"
else:
    result_color = RED
    result_title = "QUEST OVER"
    result_detail = "Out of attempts. A new quest awaits!"

answer_line = f"Secret word: {secret_word.title()}"
count_line = f"Total guesses: {guess_count}"

print()
print(f"{result_color}╔{'═' * 48}╗")
print(f"║{BOLD}{result_title.center(48)}{RESET}{result_color}║")
print(f"║{result_detail.center(48)}║")
print(f"║{answer_line.center(48)}║")
print(f"║{count_line.center(48)}║")
print(f"╚{'═' * 48}╝{RESET}")
show_attempts(MAX_ATTEMPTS - guess_count, show_message=False)
print()
