"""
Rolls some stuff.
Hays - November 2024
"""

import random

def roll_n_times(n:int) -> int:
    total: int = 0
    for _ in range (n):
        roll: int = random.randint(1,6)
        total += roll
    return total

def is_winner(total: int, min_to_win: int) -> bool:
    if total > min_to_win:
        return True
    else:
        return False

def main() -> None:
    #variable setup
    MIN_WIN: int = 13
    roll_num: int = 3

  #how many times it rolls the dice
    total: int = roll_n_times(roll_num)

    #print out the results
    print(total)

  #if win
    if is_winner(total, MIN_WIN):
        print(f"You won ${total}")
  #if fail
    else:
        print(f"HA HA YOU ONLY GOT {total}! HOW TERRIBLE ARE YOU????")


if __name__ == "__main__":
    main()