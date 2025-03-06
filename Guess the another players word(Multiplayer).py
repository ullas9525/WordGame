import random
import msvcrt
import os
import time
import sys
delay1 = 2
delay2 = 3
streaks = 0
def key_interrupt(delay):
    start_time = time.time()
    while time.time() - start_time < delay:
        if msvcrt.kbhit():
            msvcrt.getch()  # Consume the key press
            break
        time.sleep(0.1)
    return 0
try:
    terminal_width = os.get_terminal_size().columns
except OSError:
    terminal_width = 80

def guessword(guess,word):
    correct_letters = 0
    correct_position = 0
    for i in range (4):
        if (guess[i] == word[i]):
            correct_position += 1
        if (guess[i] in word):
            correct_letters += 1
    return correct_letters,correct_position

def guessmyword(word,guessed,streaks):
    attempts = 10
    while(attempts >0):
        print("Chances left: 🎲",attempts)
        print("Streaks: 🔥",streaks)
        guess = input("\nEnter your Guess: ").upper()
        if(guess == "Q"):
            print("You have exited the game!!🏳️")
            break
        if(len(set(guess)) != 4 or len(guess) != 4):
            print("Read the above rules again!! 📚 ")
            print("Try again with different word!!🔤\n")
            continue
        correct_letters,correct_position = guessword(guess,word)
        print("correct letters:",correct_letters,", correct position:", correct_position)
        if(correct_position == 4):
            print("Congratulations🎉!!\nYou have guessed the correct word !")
            guessed = 1
            streaks += 1
            return guessed,guess,streaks
        attempts -= 1
    return guessed,guess,streaks
while(True):
    print("🔤 \033[36mWelcome to the Word Guessing Game!!\033[0m\n".center(terminal_width))
    print("\n loading game....", flush=True)
    key_interrupt(delay2)
    sys.stdout.write('\033[F')  # Move cursor up one line.
    sys.stdout.write('\033[K')  # Clear to the end of line.
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("📜 \033[31mRules:-\033[0m".center(terminal_width))
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("1. You have 10 chances🎲 to guess🎯.")
    key_interrupt(delay1)
    print("2. Word has 4 unique letters(letter should not repeat).")
    key_interrupt(delay1)
    print("3. A word should have a specific meaning.")
    key_interrupt(delay1)
    print("4.Enter q to exit the game.")
    key_interrupt(delay1)
    print("\nI think you have read all the rules above")
    key_interrupt(delay1)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Let's begin the game:-")
    print("Enter a Word to guess for another player:",flush = True)
    word = input().upper()
    sys.stdout.write('\033[F')  # Move cursor up one line.
    sys.stdout.write('\033[K')  # Clear to the end of line.
    if(len(word) != 4 or len(set(word)) != 4):
        print("Enter the Correct Word")
        sys.stdout.write('\033[F')  # Move cursor up one line.
        sys.stdout.write('\033[K')  # Clear to the end of line.
    else:
        sys.stdout.write('\033[F')  # Move cursor up one line.
        sys.stdout.write('\033[K')  # Clear to the end of line.
    guessed = 0
    guessed,guess,streaks = guessmyword(word,guessed,streaks)
    if(guess == "Q"):
        print("The correct word was " + word)
        break
    elif(guessed == 0):
        print("\nYou have ran out of attempts🏳️.\nThe correct word was " + word)
        streaks = 0