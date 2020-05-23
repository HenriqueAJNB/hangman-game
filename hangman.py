status = [
    r"""
_____________
|            |
|            
|           
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|            |
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|\
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|\
|           / 
|=====================
""",
    r"""
_____________
|            |
|            O
|            -
|           /|\
|           / \
|=====================

YOU LOOSE!
""",
]


class Hangman(object):
    def __init__(self):
        self.secret_word = self.get_secret_word()
        self.correct_letters = []
        self.missed_letters = []
        self.error = 0
        self.attempts = 6
        print(
            """ <<<<<<<<<<<<<<<<<< Welcome to hangman HUNGER GAME! >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
        )

    def get_secret_word(self):
        from random import choice

        with open("words.txt") as f:
            wordsList = f.read().splitlines()
            secretWord = choice(wordsList).lower()
        return secretWord

    def read_player_input(self):
        self.inputChar = input("\nType a letter: ")

    def guess_letter(self):
        if (
            self.inputChar in self.secret_word
            and self.inputChar not in self.correct_letters
        ):
            self.correct_letters.append(self.inputChar)
            return True
        elif (
            self.inputChar not in self.secret_word
            and self.inputChar not in self.missed_letters
        ):
            self.missed_letters.append(self.inputChar)
            self.error += 1

            return False
        else:
            print("\nYou've already tried this letter.")
            return False

    def print_game_board(self):
        encoded_word = ""
        for letter in self.secret_word:
            if letter not in self.correct_letters:
                encoded_word += "_"
            else:
                encoded_word += letter

        if self.error <= self.attempts:
            print(status[self.error])

            print(encoded_word)

        print(f"\nCorrect letters: {' '.join(self.correct_letters)}")

        print(f"\nWrong letters: {' '.join(self.missed_letters)}")

    def game_continue(self):
        if set(self.correct_letters) == set(self.secret_word):
            print("\nYou win!")
            return False
        elif self.error >= self.attempts:
            print(status[self.error])
            print(f"The secret word is {self.secret_word}")
            return False
        else:
            return True


def main():
    hangman = Hangman()

    while hangman.game_continue():
        hangman.print_game_board()
        hangman.read_player_input()
        hangman.guess_letter()


if __name__ == "__main__":
    main()
