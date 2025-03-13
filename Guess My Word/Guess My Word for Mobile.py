import random
import os
import time
import sys

# Setting delays for better user experience
delay1 = 2
delay2 = 3

# Initializing Streak counter
streaks = 0
words_list = []
try:
    terminal_width = os.get_terminal_size().columns
except OSError:
    terminal_width = 80

# Function to check the guessed letters and positions
def guessword(guess,word): 
    correct_letters = 0
    correct_position = 0
    for i in range (4): # Loop through each letterin the guessed word
        if (guess[i] == word[i]): # Check if letter is in the correct position
            correct_position += 1
        if (guess[i] in word): #Ceck if letter exists anywhere in the word
            correct_letters += 1
    return correct_letters,correct_position

# Reading the words from the file and storing them in a list
with open("Words.txt","r") as file: 
    for line in file:
        words_list.append(line.strip())
def guessmyword(word,guessed,streaks): # Main Function handling the game logic
    attempts = 10 # Number of attempts allowed
    while(attempts >0):
        print("\nChances left: 🎲",attempts)
        guess = input("\nEnter your Guess: ").upper()
        if(guess == "Q"): #check if the user wants to exit the game
            print("You have exited the game!!🏳️")
            break
        # Check if the guessed word is valid
        if(len(set(guess)) != 4 or len(guess) != 4):
            print("Read the above rules again!! 📚 ")
            print("Try again with different word!!🔤\n")
            continue
        # Get the correct letters and positions
        correct_letters,correct_position = guessword(guess,word)
        print("correct letters:",correct_letters,", correct position:", correct_position)
        if(correct_position == 4): # Check if the user has guessed the correct word
            print("Congratulations🎉!!\nYou have guessed the correct word !\n")
            streaks += 1 # Increment the streak count
            guessed = 1
            return guessed,guess,streaks
        attempts -= 1 # Decrement the attempts count
    return guessed,guess,streaks # Return the values after attempts are exhausted

# infinite loop to play the game
while(True): 
    print("-"*40) 
    print("\n🔤 \033[36mWelcome to the Word Guessing Game!!\033[0m\n".center(terminal_width))
    print("\n loading game....", flush=True)
    time.sleep(3)
    sys.stdout.write('\033[F')  # Move cursor up one line.
    sys.stdout.write('\033[K')  # Clear to the end of line.
    print("-"*40)

    # Printing the rules of the game
    print("\t📜 \033[31mRules:-\033[0m".center(terminal_width)) 
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

    # Selecting a random word from the list
    word = random.choice(words_list)

    # Dsiplay Streaks
    print("Streaks: 🔥",streaks) 
    guessed = 0 # reset the guessed flag

    # Call the function to start the game
    guessed,guess,streaks = guessmyword(word,guessed,streaks)

    # If user quits, display correct word and exit the game
    if(guess == "Q"):
        print("The correct word was " + word)
        break

    # If attempts run out, show correct word and reset streaks
    elif(guessed == 0):
        print("\nYou have ran out of attempts🏳️.\nThe correct word was " + word,"\n")
        streaks = 0
