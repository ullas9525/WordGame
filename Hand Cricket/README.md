# Hand Cricket Game

## Introduction
The **Hand Cricket Game** is an interactive simulation of the popular street game "hand cricket." In this game, the outcome of the toss is decided by an odd-even choice, and the match unfolds with batting and bowling innings based on numbers selected between 1 and 6. Enjoy a fun, competitive game where your input and a bit of luck determine the winner!

## Objectives
- **Experience Virtual Cricket:** Enjoy a digital version of the classic hand cricket game right from your terminal.
- **Test Strategy and Luck:** Decide whether to bat or bowl based on the toss outcome and try to beat the computer.
- **Improve Decision-Making:** Learn to make strategic choices under pressure and manage game flow.
- **Engage in Interactive Play:** Experience a simple yet fun cricket match with real-time scoring and dynamic gameplay.

## How to Play
1. **Toss:**
   - The game begins with a toss. Choose between **odd** or **even**.
   - You will then enter a number (1-6), and the computer will randomly choose its own number.
   - The sum of both numbers determines the toss result. If the parity (odd/even) of the sum matches your choice, you win the toss; otherwise, the computer wins.

2. **Batting or Bowling Decision:**
   - If you win the toss, you choose whether to **bat** or **bowl**.
   - If the computer wins, it randomly selects to bat or bowl, and you will take the opposite role.

3. **Innings:**
   - **Batting:**
     - The batting side (user or computer) enters a number between 1 and 6.
     - The opposing side simultaneously chooses a random number.
     - If the numbers differ, the batting side scores runs (the chosen number or the computer's number, depending on the inning).
     - If the numbers match, the batsman is declared **OUT**, ending that innings.
   - **Target Setting:**
     - Once the batting side is out, the opposing side's target is set as the batting side’s score plus one run.
   - **Chasing:**
     - The chasing side then tries to reach the target by repeating the process until they either achieve the target or get out.

4. **Winning the Game:**
   - The game compares scores after both innings.
   - The winner is announced along with the winning margin (runs or otherwise).

## Rules
- **Toss:**
  - Choose **odd** or **even**.
  - Enter a valid number between 1 and 6 for the toss.
- **Batting/Bowling:**
  - When batting, your runs add to the score if the numbers do not match.
  - If both numbers are the same, the batsman is declared OUT.
- **Input Validation:**
  - Only numbers between 1 and 6 are accepted.
  - Invalid inputs prompt you to try again.

## Installation
### Requirements
- **Python 3** installed on your system.

### Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/HandCricketGame.git
