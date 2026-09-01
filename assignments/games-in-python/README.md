
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a complete Hangman game where players guess letters to reveal a hidden word before running out of attempts. You'll practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Word Selection and Display

#### Description
Create the core game setup that randomly selects a word and displays it as underscores that reveal letters as they are guessed correctly.

#### Requirements
Completed program should:

- Define a list of at least 10 words to choose from
- Randomly select one word from the list at the start of each game
- Display the word as underscores (e.g., `_ _ _ _`)
- Update and display the word as correct letters are guessed
- Example: After guessing 'a' in the word "python", display `_ _ _ _ _ _` and after guessing 'p', display `p _ _ _ _ _`


### 🛠️ Guess Tracking and Game State

#### Description
Implement the logic to track guesses, manage remaining attempts, and keep track of letters already guessed.

#### Requirements
Completed program should:

- Track incorrect guesses and decrement remaining attempts
- Prevent duplicate guesses (inform player if they already guessed a letter)
- Display the list of guessed letters
- Display the number of remaining attempts
- Example: "Guessed letters: a, e, i | Attempts remaining: 5"


### 🛠️ Game End Conditions

#### Description
Implement the win and lose conditions, and handle game flow from start to finish.

#### Requirements
Completed program should:

- End the game when the player guesses all letters correctly (win)
- End the game when attempts run out (lose)
- Display appropriate win/lose messages with the hidden word revealed
- Ask if the player wants to play again
- Example win message: "Congratulations! You guessed the word: python"
- Example lose message: "Game over! The word was: python"
