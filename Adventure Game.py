import time

def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    time.sleep(1)
    print("You find yourself at the entrance of a dense, dark forest.")
    time.sleep(1)
    print("Your goal is to reach the other side. Be cautious, as the forest is full of surprises!")
    time.sleep(1)
    print("\nLet the adventure begin!\n")

def make_choice(choices):
    print("Choose your path:")
    for i, option in enumerate(choices, start=1):
        print(f"{i}. {option}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(choices):
            return int(choice)
        else:
            print("Invalid choice. Please enter a valid number.")

def forest_path():
    print("\nYou start walking along a narrow path.")
    time.sleep(1)
    print("Ahead, you see two different routes diverging.")
    time.sleep(1)

    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou chose the left path.")
        time.sleep(1)
        print("As you proceed, you encounter a friendly creature that guides you safely through the forest.")
        return "safe"
    else:
        print("\nYou chose the right path.")
        time.sleep(1)
        print("Unfortunately, you stumble upon a trap and lose some valuable items.")
        return "trap"

def encounter_enemy():
    print("\nWhile navigating through the forest, you suddenly encounter a mysterious enemy!")
    time.sleep(1)

    choices = ["Fight the enemy", "Try to sneak away"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou decide to confront the enemy.")
        time.sleep(1)
        print("After a fierce battle, you emerge victorious.")
        return "victory"
    else:
        print("\nYou attempt to sneak away, but the enemy notices you.")
        time.sleep(1)
        print("You manage to escape, but your journey becomes more perilous.")
        return "escape"

def main():
    introduction()

    path_result = forest_path()

    if path_result == "safe":
        print("\nYou successfully navigate through the forest and reach the other side safely!")
    elif path_result == "trap":
        print("\nThe trap sets you back, but you continue your journey with caution.")

    enemy_result = encounter_enemy()

    if enemy_result == "victory":
        print("\nWith the enemy defeated, you continue your journey with confidence.")
        print("Congratulations! You've successfully completed the Mysterious Forest Adventure.")
    elif enemy_result == "escape":
        print("\nYou manage to escape the enemy, but the forest becomes even more mysterious.")
        print("Thank you for playing the Mysterious Forest Adventure.")

if __name__ == "__main__":
    main()
