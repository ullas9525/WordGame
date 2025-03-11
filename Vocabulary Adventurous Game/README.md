# Vocabulary Adventurous Game

## Introduction
The **Vocabulary Adventurous Game** is an interactive, text-based game designed to help you expand your vocabulary while having fun. In this game, you'll be given a clue at each level and must guess the corresponding word. The game features multiple difficulty modes—Easy, Intermediate, Professional, and Hard—each with its own set of clues and words. As you progress, you earn streaks and lifelines, making each round more engaging and challenging.

## Objectives
- **Expand Your Vocabulary:** Learn new words through context and clues.
- **Enhance Deductive Skills:** Use clues to logically deduce the correct word.
- **Challenge Yourself:** Tackle four distinct difficulty modes that gradually increase in complexity.
- **Build Streaks:** Successfully complete levels to increase your streak and improve your performance.
- **Utilize Lifelines:** Use lifelines to reveal letters when you’re stuck, adding a strategic element to the game.

## How to Play
1. **Game Setup:**
   - The game starts by displaying a welcome message and a set of rules.
   - You will then be prompted to choose a mode:
     - **e:** Easy
     - **i:** Intermediate
     - **P:** Professional
     - **h:** Hard

2. **Gameplay Mechanics:**
   - At the beginning of each round, a clue related to a specific word is presented.
   - The word's length is shown by displaying Star.
   - You have **unlimited attempts** to guess the word correctly.
   - **Lifelines:**  
     - Enter **`1`** to use a lifeline, which will reveal one random letter of the word.
     - You start with a limited number of lifelines (initially set to 3).
   - **Give Up:**  
     - Enter **`2`** if you wish to give up on the current word. This resets your streak.
   - **Additional Options:**
     - Enter **`?`** to display game information.
     - Enter **`q`** to exit the current mode and choose another.
   - Upon a correct guess, you advance to the next level and your streak increases.

3. **Levels and Modes:**
   - **Easy:** Straightforward clues with common words.
   - **Intermediate:** More challenging clues requiring deeper thought.
   - **Professional:** Complex clues with less common words.
   - **Hard:** Cryptic and multi-layered clues that test your vocabulary limits.

## Rules
- **Word Length:** Each word will have a specific number of letters, shown in the clue.
- **Input Validation:**  
  - Only words with the correct number of letters are accepted.
  - No special characters should be included in the guessed word.
- **Lifeline Usage:**  
  - Lifelines can be used to reveal a letter, but are limited in number.
- **Streaks:**  
  - Your streak increases with every successful level completion.
  - Giving up (inputting `2`) resets your streak to zero.

## Requirements
- **Python 3:** Ensure you have Python 3 installed.
- **Windows OS:** This game uses the `msvcrt` module for handling key interruptions, so it is optimized for Windows.

## Installation and Running the Game
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/VocabularyAdventurousGame.git
