import random as rn

words = {
    "PYTHON": "A programming language",
    "DATABASE": "A place to store data",
    "FUNCTION": "Reusable block of code",
    "VARIABLE": "Stores a value",
    "ALGORITHM": "Steps to solve a problem"
}

attempts, points = (3, 0)


def select_word():
    random_word = rn.choice(list(words.keys()))
    letters = list(random_word)
    rn.shuffle(letters)
    return letters, random_word


def display(random_word, letters, attempts):
    if random_word in words:
        print(f"Scrambled Word: {''.join(letters)}")
        print(f"You have {attempts} attempts.")


def guess(letters, random_word, attempts, points):

    while attempts > 0:
        display(random_word, letters, attempts)

        guessing = input(
            "Enter your guess, 'hint' for a hint, or 'quit' to skip: "
        ).strip()

        if not guessing:
            print("Empty guess is not allowed.")
            continue

        elif guessing.upper() == random_word:
            points += 3
            print("Correct! You earned 3 points.")
            print(f"Your total points: {points}")
            break

        elif guessing.lower() == "hint":
            points -= 1
            print(f"Hint: {words[random_word]}")
            print(f"Your total points: {points}")
            continue

        elif guessing.lower() == "quit":
            print(f"The correct word was: {random_word}")
            break

        else:
            attempts -= 1
            print("Incorrect guess!")
            print(f"{attempts} attempts left")

    if attempts == 0:
        print(f"Out of attempts! The word was: {random_word}")

    print(f"Points: {points}")
    return points


while True:
    attempts = 3
    letters, random_word = select_word()

    points = guess(letters, random_word, attempts, points)

    continu = input(
        "Play another round? (yes/no): "
    ).lower().strip()

    if continu != "yes":
        print("Game Over!")
        print(f"Final points: {points}")
        break
