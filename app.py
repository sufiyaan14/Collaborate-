# gui_dice_roller.py
import tkinter as tk
from tkinter import messagebox
import random
import time

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Digital Dice Roller 🎲")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.history = []

        # Title
        self.title_label = tk.Label(root, text="Digital Dice Roller", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # Dice sides input
        self.sides_label = tk.Label(root, text="Enter number of sides (default=6):")
        self.sides_label.pack()
        self.sides_entry = tk.Entry(root, width=10)
        self.sides_entry.pack(pady=5)

        # Roll button
        self.roll_button = tk.Button(root, text="🎲 Roll Dice", command=self.roll_dice, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.roll_button.pack(pady=10)

        # Result display
        self.result_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
        self.result_label.pack(pady=10)

        # History
        self.history_label = tk.Label(root, text="📜 Roll History", font=("Arial", 14, "bold"))
        self.history_label.pack(pady=5)

        self.history_listbox = tk.Listbox(root, width=40, height=10)
        self.history_listbox.pack(pady=5)

        # Buttons for history
        self.clear_button = tk.Button(root, text="🧹 Clear History", command=self.clear_history, bg="#f44336", fg="white")
        self.clear_button.pack(side=tk.LEFT, padx=30, pady=20)

        self.exit_button = tk.Button(root, text="🚪 Exit", command=root.quit, bg="#555", fg="white")
        self.exit_button.pack(side=tk.RIGHT, padx=30, pady=20)

    def roll_dice(self):
        sides = self.sides_entry.get()
        sides = int(sides) if sides.isdigit() else 6
        result = random.randint(1, sides)
        timestamp = time.strftime("%H:%M:%S")

        self.history.append((result, sides, timestamp))
        self.result_label.config(text=f"You rolled: {result} on a {sides}-sided dice 🎲")

        self.history_listbox.insert(tk.END, f"{result} (on {sides}-sided) at {timestamp}")

    def clear_history(self):
        self.history.clear()
        self.history_listbox.delete(0, tk.END)
        messagebox.showinfo("History", "History cleared successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

