# --- A Dice simulator. ---
# --- made by pvk-96 ---
# --- Changes are encouraged ---
import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    print("🎲 Dice Roller Simulator")
    while True:
        input("Press Enter to roll the dice... ")
        print(f"You rolled: {roll_dice()}")
        
        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye! 👋")
            break
