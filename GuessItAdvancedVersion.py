from __future__ import annotations
import random
from dataclasses import dataclass
from typing import Optional


class InvalidGuessError(ValueError):
    """Raised when the a stupi* user enters a guess outside the allowed range."""


@dataclass
class GuessingGame:
    min_value: int = 1
    max_value: int = 100
    max_attempts: Optional[int] = None

    def __post_init__(self) -> None:
        self._rng = random.Random()
        self._secret_number = self._rng.randint(self.min_value, self.max_value)
        self.attempts = 0

    def validate_guess(self, guess: int) -> None:
        if not self.min_value <= guess <= self.max_value:
            raise InvalidGuessError(
                f"Guess must be between {self.min_value} and {self.max_value}"
            )

    def make_guess(self, guess: int) -> str:
        self.validate_guess(guess)
        self.attempts += 1

        if guess > self._secret_number:
            return "Too high!"
        elif guess < self._secret_number:
            return "Too low!"
        else:
            return f"🎉 Correct! You guessed it in {self.attempts} attempts."

    def is_game_over(self) -> bool:
        return self.max_attempts is not None and self.attempts >= self.max_attempts


def main() -> None:
    game = GuessingGame(min_value=1, max_value=100, max_attempts=10)

    print("🎯 Heyyy, Guess the Number Game")
    print("Type 'q' to quit.\n")

    while True:
        if game.is_game_over():
            print("❌ Game over! You've used all attempts.")
            break

        user_input = input("Heyy, Enter a guess (: ").strip()

        if user_input.lower() == "q":
            print("👋 Thanks for playing!")
            break

        try:
            guess = int(user_input)
            result = game.make_guess(guess)
            print(result)

            if result.startswith("🎉 Correct!"):
                break

        except ValueError:
            print("⚠️ Please enter a valid number.")
        except InvalidGuessError as e:
            print(f"⚠️ {e}")


if __name__ == "__main__":
    main()
