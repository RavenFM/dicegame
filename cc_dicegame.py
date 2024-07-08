import random

high_score = 0

def dice_game():
    while True:
        print("1. Roll the dice")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            total = roll1 + roll2

            print(f"\nYou rolled: {roll1} and {roll2}")
            print(f"Total: {total}")

            global high_score
            if total > high_score:
                high_score = total
                print("New high score!\n")
            else:
                print("\n")
        elif choice == "2":
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

dice_game()
