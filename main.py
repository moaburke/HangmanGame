"""
Hangman Game

Author: Moa Burke
Date: 26 Sept 2024
Description: This program implements a classic Hangman game where the player guesses letters to reveal a randomly selected word.
The player has limited number of incorrect guesses (lives) before losing the game. The game provides visual feedback through stages of the hangman,
displays the correctly guessed letters, tracks incorrect guesses and keeps track of the player's total wind and losses.
Additionally, it validated user input for both letter guesses and continuation of the game after each round.

Version: 1.1

Changelog:
- v1.1: Added tracking for total wins/losses, visual display of game outcome, and input validation for letter guesses and game continuation.
- v1.0: Initial release with basic gameplay functionality.
"""

import random # Import random module for selecting a random word
from hangman_art import stages, logo, win, lose # Import visual elements for the hangman game, including stages and logos for display
from hangman_words import word_list, alphabet # Import the predefined list of words for the game and the alphabet for validating user input


"""
Prompts the user to decide whether to play the game again.

This function repeatedly asks the user for input until a valid response ('y' for yes or 'n' for no) is received. 
The user's input is converted to lowercase to ensure case-insensitivity.

Returns:
    bool: Returns True if the user chooses not to play again (by typing 'n'),
    and false if the user wants to continue playing (by typing 'y'). 
"""
def prompt_exit_game():
    valid_input = False # Initialize a flag to track if the input is valid
    choice = "" # Initialize the choice variable

    # Continue looping until a valid input is received
    while not valid_input:
        choice = input("\nDo you want to play again? Type 'y' for Yes or 'n' to exit the game. ").lower() # Ask for user input
        if choice == 'y' or choice == 'n': # Check is the input is valid
            valid_input = True # Set flag to true to exit the loop
        else:
            print("Invalid input. Please try again.")  # Inform the user that the input is invalid

    return choice != 'y' # Return true to exit if the user does not want to play again


"""
Displays the result of the round in the game

Parameters:
    result (str): A string indicating the outcome of the round. Either "win" or "lose"
    
The function prints the user's total score, including the number of wins and losses,
reveals the correct word, and displays an appropriate message based on whether the
user won or lost the round.
"""
def end_of_round(result):
    print(f"Your total score:\nWins: {wins}\nLosses: {losses}") # Display the user's total score, including the number of wins and losses
    print(f"\n------------------------- The word was {chosen_word.upper()} -------------------------")  # Inform user of the outcome adn reveal the correct word
    #Check the result of the round; if the user won, display the winning message
    if result == "win":
        print(win[0]) # Print the winning message
    else:
        print(lose[0]) # Print the losing message


exit_game = False # Initialize the flag to control the game's continuation or exit
wins = 0 # Initialize the counter for the number of wins
losses = 0 # Initialize the counter for the number of losses

print(logo[0]) # Welcome message

# Main game loop that continues until the user decides to exit
while not exit_game:
    lives = 6 # Initialize the number of lives for the player

    # Randomly select a word from the word list
    chosen_word = random.choice(word_list)

    # Initialize placeholders for guessed letters
    placeholder = ''
    guessed_letters = [] # List to keep track of guessed letters
    correct_letters = [] # List to keep track of correct letters

    #Fill the placeholder with underscores for each letter in the generated word
    for letter in chosen_word:
        placeholder += "_"

    print(f"\nWord to guess: {placeholder}") # Display the initial placeholder

    game_over = False #Initialize the flag to manage game state; set to False to allow for ongoing play

    # Inner loop for the actual game logic
    while not game_over:
        print(f"Lives left: {lives}/6") # Display remaining lives

        valid_guess = False #Initialize a flag to track whether the user's guess is valid

        #Continue looping until a valid guess is made
        while not valid_guess:
            guess = input("Please guess a letter: ").lower() #Prompt the user to input a letter and convert it to lowercase

            if guess not in alphabet: # Check if the guessed letter is not in the predefined alphabet
                print("Oops! That doesn't seem to be a valid letter. Give it another shot!") # Inform the user that the guess is invalid
                valid_guess = False # Set flag to false
            elif guess in guessed_letters: # Check if the guess has already been made
                print(f"You have already guessed {guess.upper()}. Try again!") # Inform the user
                valid_guess = False  # Set flag to false
            else: # If the guessed letter is valid
                valid_guess = True # Set the flag to true to exit the loop

        display = '' # Initialize the display for the current state of the word

        # Build the display string based on the user's guess
        for letter in chosen_word:
            if letter == guess: # If the guessed letter is correct
                correct_letters += letter # Add the letter to correct_letters list
                display += letter #Reveal the letter in the display
            elif letter in correct_letters: # If the letter has been guessed correctly before
                display += letter # Keep the letter visible
            else:
                display += "_" # Hide the letter with an underscore


        guessed_letters += guess # Add the guess to guessed_letters list
        #If the guess is incorrect
        if guess not in chosen_word:
            print(f"Sorry, {guess.upper()} is not in the word.") # Inform user of wrong guess
            lives -= 1 #decrease the number of lives

        # Create a string of guessed letters for display
        guessed_letter_print = ', '.join(letter.upper() for letter in guessed_letters)

        # Print the current display of the word and the guessed letters
        print(f"\nWord to guess: {display}")
        print(f"Guessed letters: {guessed_letter_print}")

        # Display the current stage of the hangman
        print(stages[lives])

        # Check for game over conditions
        if lives == 0: # If the user has run out of lives
            losses += 1 # Increment the losses counter
            end_of_round("lose") # Call the function to handle the end of the round for a loss
            game_over = True # End the round
            exit_game = prompt_exit_game() # Ask the user if they want to exit the game


        if "_" not in display: # If there are no underscores left, the user has won
            wins += 1 # Increment the wins counter
            end_of_round("win") # Call the function to handle the end of the round for a loss
            game_over = True # End the round
            exit_game = prompt_exit_game() # Ask the user if they want to exit the game


print("\nThank you for playing. Goodbye!") # Thank user for playing