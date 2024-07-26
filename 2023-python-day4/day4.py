import os

def check_line(line):
    """
    Processes a line of text containing winning numbers and a player's hand, and calculates a score based on the matches.

    Parameters:
    line (str): A string containing a card description with winning numbers and the player's hand, separated by '|'.
                The format is expected to be "Card X: <winning_numbers> | <hand_numbers>".

    Card  80: 32 70 81 23 72 90 58 50 27  1 | 18 72 46  5 85 68 16 83 62 51 98 42 49 14  2 78 63 45 21 82 97 96 56 19 36

    Returns:
    int: The score calculated based on the number of matches between winning numbers and hand numbers.
         Returns 0 if no matches are found.
    """
    numbers = line.split(":")[1]
    winner_numbers_str, hand_str = numbers.split("|")[0], numbers.split("|")[1]

    winner_numbers = set(winner_numbers_str.split())
    hand = set(hand_str.split())

    found = len([num for num in hand if num in winner_numbers])

    return 2 ** (found - 1) if found > 0 else 0

if __name__ == "__main__":
    lines = open('input.txt').readlines()

    result = 0
    for line in lines:
        result += check_line(line)
    print(result)