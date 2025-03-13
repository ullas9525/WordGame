import random
import os
import time
import sys
delay1 = 2
delay2 = 3
streaks = 0
words_list = []
try:
    terminal_width = os.get_terminal_size().columns
except OSError:
    terminal_width = 80

def guessword(guess,word): # Function to check the guessed letters and positions
    correct_letters = 0
    correct_position = 0
    for i in range (4):
        if (guess[i] == word[i]):
            correct_position += 1
        if (guess[i] in word):
            correct_letters += 1
    return correct_letters,correct_position
with open("Words.txt","r") as file: # Reading the words from the file
    for line in file:
        words_list.append(line.strip())
def guessmyword(word,guessed,streaks): # Main Function
    attempts = 10
    while(attempts >0):
        print("\nChances left: 🎲",attempts)
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
            print("Congratulations🎉!!\nYou have guessed the correct word !\n")
            streaks += 1
            guessed = 1
            return guessed,guess,streaks
        attempts -= 1
    return guessed,guess,streaks
while(True): # infinite loop to play the game
    print("-"*40) 
    print("\n🔤 \033[36mWelcome to the Word Guessing Game!!\033[0m\n".center(terminal_width))
    print("\n loading game....", flush=True)
    time.sleep(3)
    sys.stdout.write('\033[F')  # Move cursor up one line.
    sys.stdout.write('\033[K')  # Clear to the end of line.
    print("-"*40)
    print("\t📜 \033[31mRules:-\033[0m".center(terminal_width)) # Printing the rules of the game
    print("-"*40)
    print("1. You have 10 chances🎲 to guess🎯.")
    time.sleep(2)
    print("2. Word has 4 unique letters\n(letter should not repeat).")
    time.sleep(2)
    print("3. A word should have a specific meaning") 
    time.sleep(2)
    print("4. Enter q to exit the game.")
    time.sleep(2)
    print("\nI think you have read the rules above")
    time.sleep(3)
    print("-"*40)
    print("\tLet's begin the game:-\n")
    print("-"*40)
    word = random.choice(words_list)
    print("Streaks: 🔥",streaks) # Streaks point
    guessed = 0
    guessed,guess,streaks = guessmyword(word,guessed,streaks)
    if(guess == "Q"):
        print("The correct word was " + word)
        break
    elif(guessed == 0):
        print("\nYou have ran out of attempts🏳️.\nThe correct word was " + word,"\n")
        streaks = 0
