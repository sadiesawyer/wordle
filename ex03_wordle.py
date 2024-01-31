"""EX03 - Structured Wordle!"""
__author__ = "730643126"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word = "codes"


def contains_char(secret_wrd: str, char_guess: str) -> bool:
    """Checks if the guessed character is contained in the secret word."""
    assert len(char_guess) == 1
    current_idx = 0

    while current_idx <= len(secret_wrd) - 1:
        
        if secret_wrd[current_idx] == char_guess:
            return True
        else:
            current_idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis indicating which characters of the guess are correct."""
    assert len(secret) == len(guess)
    
    guess_i = 0
    guess_emoji = ""
    
    while guess_i <= len(secret) - 1:
        
        if guess[guess_i] == secret[guess_i]:
            guess_emoji += GREEN_BOX
            guess_i += 1
        elif contains_char(secret, guess[guess_i]):
            guess_emoji += YELLOW_BOX
            guess_i += 1
        else:
            guess_emoji += WHITE_BOX
            guess_i += 1
    
    return guess_emoji


def input_guess(expected_length: int) -> str:
    """Prompts user for a guess until they give one of the right length."""
    guess_input = input(f"Enter a {(expected_length)} character word: ")
    while len(guess_input) != expected_length:
        guess_input = input(f"That wasn't {(expected_length)} chars! Try again: ")
    return guess_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number = 1
    has_won = False
    
    while not has_won and turn_number < 7:
        print(f"=== Turn {(turn_number)}/6 ===")
        current_guess = input_guess(len(secret_word))
        print(emojified(current_guess, secret_word))
        if current_guess == secret_word:
            print(f"You won in {(turn_number)}/6 turns!")
            has_won = True
            exit
        turn_number += 1
    if not has_won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()