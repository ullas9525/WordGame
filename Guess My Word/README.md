# Word Guessing Game

## Introduction
The **Word Guessing Game** is an interactive command-line game where the computer randomly selects a secret 4-letter word from a predefined list. You have 10 chances to guess the word correctly. With each guess, you'll receive feedback indicating how many letters are correct and how many are in the correct position. The game also tracks your win streaks to encourage improvement.

## Objectives
- **Enhance Deductive Reasoning:** Use the feedbacks provided to logically deduce the secret word.
- **Improve Vocabulary:** Engage with a curated list of meaningful 4-letter words.
- **Challenge Your Memory and Strategy:** Aim to guess the word within limited attempts and build a winning streak.
- **Enjoy Interactive Gameplay:** Experience a fun, fast-paced game that tests your attention to detail.

## How to Play
1. **Game Start:**  
   When the game begins, the computer randomly selects a secret word from a predefined list.

2. **Guessing:**  
   You are given **10 attempts** to guess the word. Type your guess and press Enter.  
   - Each guess must be a 4-letter word with all unique letters.
   - Enter **'Q'** at any time to exit the game.

3. **Feedback:**  
   After each guess, the game displays:
   - **Correct Letters:** The total number of letters in your guess that are found in the secret word.
   - **Correct Position:** The number of letters that are in the exact position as in the secret word.

4. **Winning and Streaks:**  
   - If you correctly guess the word (i.e., all 4 letters in the correct positions) before running out of attempts, you win the round and your streak increases.
   - If you run out of attempts, the correct word is revealed, and your streak resets.

## Rules
- The secret word is exactly **4 letters**.
- All letters in the word must be **unique** (no repeated letters).
- The word is chosen from a list of meaningful words.
- You have **10 attempts** per round.
- Enter **'Q'** to quit the game at any time.

## Installation
### Requirements
- **Python 3**  
- **Windows OS** (the game uses the `msvcrt` module for keyboard input)

### Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/WordGuessingGame.git
