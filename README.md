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
