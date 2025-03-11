# Word Guessing Game

## Introduction
The **Word Guessing Game** is an interactive two-player challenge that tests your vocabulary, deduction, and strategic thinking. One player secretly enters a four-letter word (from a predefined list), and the other player tries to guess it letter by letter within a limited number of attempts.

## Objectives
- **Enhance Vocabulary:** Engage with a curated list of words to strengthen your vocabulary.
- **Test Deductive Skills:** Use feedback from each guess to deduce the secret word.
- **Foster Competitive Fun:** Enjoy a friendly challenge with a friend in a turn-based setting.
- **Improve Logical Thinking:** Analyze the hints provided (correct letters and positions) to narrow down possibilities.
- **Track Progress:** Build and maintain streaks as you continuously improve your guessing skills.

## How to Play
1. **Word Entry:**  
   - **Player 1** enters a secret four-letter word (each letter must be unique and the word must be in the predefined list).
2. **Guessing:**  
   - **Player 2** has 10 chances to guess the secret word.
3. **Feedback:**  
   - After each guess, the game displays:
     - **Correct Letters:** Total number of letters that are present in the word.
     - **Correct Position:** Number of letters in the correct position.
4. **Game End:**  
   - The game ends when the correct word is guessed or when all attempts are used.
   - Enter **'Q'** at any time to exit the game.

## Rules
- The secret word must have exactly **4 letters**.
- All letters in the word must be **unique** (no repeats).
- The word must be chosen from the provided word list.
- You have **10 attempts** per round to guess the word.
- Type **'Q'** to quit the game at any time.

## Installation
### Requirements
- **Python 3** (Tested on Windows since the game uses `msvcrt` for keyboard input)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/WordGuessingGame.git
