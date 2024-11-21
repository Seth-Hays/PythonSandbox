"""
Type your header comment.
Hays - November 2024
"""


def main() -> None:
    word: str = input()
    a,b = word.split(" ")

    speed: int = int(a)
    isBday: bool = bool(b)

    if isBday:
        speed = speed - 5

    if speed <= 60:
        print("no ticket")
    
    elif speed > 80:
        print("big ticket")
    
    else:
        print("small ticket")

