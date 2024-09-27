## Description
This project implements a classic Hangman game in Python. Players guess letters to reveal a randomly selected word within a limited number of incorrect guesses (lives). The game offers a fun way to improve vocabulary and spelling skills while providing visual feedback through stages of the hangman and tracking wins and losses.

## Features
- **Random Word Selection**: Words are randomly selected from a predefined list.
- **Visual Feedback**: Each incorrect guess is represented visually through hangman stages, enhancing the gameplay experience.
- **Score Tracking**: The game keeps track of the total wins and losses, giving players a summary at the end of each game round.
- **Input Validation**: The game validates user input to ensure that only valid letters are accepted for guesses and that the continuation of the game is handled correctly.
- **Replay Option**: After each game, players can choose to play another round or exit the game.

## How to Play
1. Run the Python program to start the game.
2. You will see underscores representing the letters in the randomly chosen word.
3. Guess letters one at a time. If the letter is in the word, it will be revealed; if not, you will lose a life.
4. Continue guessing until you either reveal the entire word or run out of lives.
5. At the end of each round, your total score (wins and losses) will be displayed, and you will have the option to play again.

## Installation
To run the Hangman game, ensure you have Python installed on your machine. Clone this repository to your local machine using:
```bash
git clone https://github.com/moaburke/hangman-game.git
```

### Navigate to the Project Directory
Once the repository is cloned, navigate to the project directory by running:
```bash
cd hangman-game
```

### Run the Game
To start the game, run the following command:
```bash
python hangman.py
```

This command changes your current directory to the hangman-game folder that contains the game files.

## Changelog
- **v1.1**: Added tracking for total wins/losses, visual display of game outcome, and input validation for letter guesses and game continuation.
- **v1.0**: Initial release with basic gameplay functionality.

## Future Improvements
- Adding a graphical user interface (GUI) for a more engaging experience.
- Expanding the word list to include themed categories (e.g., animals, countries).
- Implementing difficulty levels that change the number of lives available to the player.

## Acknowledgments
- Thanks to the contributors of the word list and hangman art resources.
- Inspired by classic word guessing games.


### Example
```plaintext
 _
| |  Welcome to the
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |          game!
                   |___/


Word to guess: _____
Lives left: 6/6
Please guess a letter: d
Sorry, D is not in the word.

Word to guess: _____
Guessed letters: D

  +---+
  |   |
  O   |
      |
      |
      |
=========

Lives left: 5/6
Please guess a letter: m

Word to guess: m____
Guessed letters: D, M

  +---+
  |   |
  O   |
      |
      |
      |
=========

Lives left: 5/6
Please guess a letter: o

Word to guess: mo___
Guessed letters: D, M, O

  +---+
  |   |
  O   |
      |
      |
      |
=========

Lives left: 5/6
Please guess a letter: 4
Oops! That doesn't seem to be a valid letter. Give it another shot!
Please guess a letter: a
Sorry, A is not in the word.

Word to guess: mo___
Guessed letters: D, M, O, A

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Lives left: 4/6
Please guess a letter: u

Word to guess: mou__
Guessed letters: D, M, O, A, U

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Lives left: 4/6
Please guess a letter: i
Sorry, I is not in the word.

Word to guess: mou__
Guessed letters: D, M, O, A, U, I

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Lives left: 3/6
Please guess a letter: z
Sorry, Z is not in the word.

Word to guess: mou__
Guessed letters: D, M, O, A, U, I, Z

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Lives left: 2/6
Please guess a letter: k
Sorry, K is not in the word.

Word to guess: mou__
Guessed letters: D, M, O, A, U, I, Z, K

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Lives left: 1/6
Please guess a letter: e

Word to guess: mou_e
Guessed letters: D, M, O, A, U, I, Z, K, E

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Lives left: 1/6
Please guess a letter: s

Word to guess: mouse
Guessed letters: D, M, O, A, U, I, Z, K, E, S

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Your total score:
Wins: 1
Losses: 0

------------------------- The word was MOUSE -------------------------


 /$$     /$$                                      /$$           /$$
|  $$   /$$/                                     |__/          | $$
 \  $$ /$$//$$$$$$  /$$   /$$       /$$  /$$  /$$ /$$ /$$$$$$$ | $$
  \  $$$$//$$__  $$| $$  | $$      | $$ | $$ | $$| $$| $$__  $$| $$
   \  $$/| $$  \ $$| $$  | $$      | $$ | $$ | $$| $$| $$  \ $$|__/
    | $$ | $$  | $$| $$  | $$      | $$ | $$ | $$| $$| $$  | $$    
    | $$ |  $$$$$$/|  $$$$$$/      |  $$$$$/$$$$/| $$| $$  | $$ /$$
    |__/  \______/  \______/        \_____/\___/ |__/|__/  |__/|__/


Do you want to play again? Type 'y' for Yes or 'n' to exit the game. 
