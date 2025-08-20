# dice_roller.py
import random
import time

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    history = []
    print("🎲 Welcome to Digital Dice Roller 🎲")
    
    while True:
        print("\n--- Menu ---")
        print("1. Roll Dice 🎲")
        print("2. View History 📜")
        print("3. Clear History 🧹")
        print("4. Exit 🚪")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            sides = input("How many sides should the dice have? (default=6): ")
            sides = int(sides) if sides.isdigit() else 6
            result = roll_dice(sides)
            timestamp = time.strftime("%H:%M:%S")
            history.append((result, sides, timestamp))
            print(f"✅ You rolled a {result} on a {sides}-sided dice at {timestamp}.")
            
        elif choice == "2":
            if not history:
                print("📭 No rolls yet.")
            else:
                print("\n📜 Roll History:")
                for i, (res, sides, ts) in enumerate(history, start=1):
                    print(f"{i}. {res} (on {sides}-sided dice) at {ts}")
                    
        elif choice == "3":
            history.clear()
            print("🧹 History cleared.")
            
        elif choice == "4":
            print("👋 Goodbye, happy rolling!")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
