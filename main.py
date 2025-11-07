# main.py
# Author: Kayode Okanlawon
# QCC ID: 24615461
#
# ET574 HW4 - Dice Game Simulator
# Implements Die and DiceGame classes and a small console menu.

import random

class Die:
    def __init__(self, sides: int = 6):
        """Create a die with given number of sides (default 6)."""
        if sides < 1:
            raise ValueError("Die must have at least 1 side.")
        self.sides = sides

    def roll(self) -> int:
        """Roll the die and return an integer between 1 and sides (inclusive)."""
        return random.randint(1, self.sides)


class DiceGame:
    def __init__(self):
        """Create a dice game using two standard six-sided dice."""
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total: int) -> str:
        """
        Evaluate a roll total and return result:
         - "Win" for totals 7 or 11
         - "Lose" for totals 2, 3, 12
         - "Roll Again" for totals 4-6 and 8-10
        """
        if total in (7, 11):
            return "Win"
        if total in (2, 3, 12):
            return "Lose"
        if total in (4, 5, 6, 8, 9, 10):
            return "Roll Again"
        # For totals outside 2-12 (shouldn't happen with two six-sided dice),
        # provide a clear string so tests can detect unexpected values.
        return "Invalid Total"

    def play_round(self):
        """
        Roll both dice and return a 4-tuple:
        (roll1: int, roll2: int, total: int, result: str)
        """
        r1 = self.die1.roll()
        r2 = self.die2.roll()
        total = r1 + r2
        result = self.evaluate_roll(total)
        return r1, r2, total, result


def main():
    game = DiceGame()

    menu = (
        "\nDice Game Simulator\n"
        "1. Play a round\n"
        "2. Exit\n"
        "Choose an option (1-2): "
    )

    while True:
        try:
            choice = input(menu).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting. Goodbye!")
            break

        if choice == "1":
            r1, r2, total, result = game.play_round()
            print(f"\nYou rolled: {r1} and {r2}")
            print(f"Total: {total}")
            print(f"Result: {result}\n")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please select 1 or 2.")

if __name__ == "__main__":
    main()
