import random
def guessword(guess,word):
    correct_letters = 0
    correct_position = 0
    for i in range (4):
        if (guess[i] == word[i]):
            correct_position += 1
        if (guess[i] in word):
            correct_letters += 1
    return correct_letters,correct_position
words_list = [ "ABLE", "ACID", "AUNT",
  "BAKE", "BANK", "BASE", "BEAR", "BIKE", "BORE", "BOWL", "BUNK",
  "CAKE", "CALM", "CARD", "CARE", "CAST", "CLAP", "CLIP", "CODE", "COIL", "COLD", "COST", "CUBE",
  "DARE", "DARK", "DATE", "DEAL", "DICE", "DIRT", "DISH", "DOVE", "DUSK", "DUST",
  "EARN", "EASY", "ECHO", "EDIT", "EPIC", "EXAM",
  "FACE", "FAKE", "FAST", "FEAR", "FILE", "FILM", "FIRE", "FIST", "FIVE", "FLAG", "FOLD", "FORK", "FORT", "FOUL", "FOUR", "FROG", "FUEL",
  "GAIN", "GAME", "GEAR", "GIFT", "GLOW", "GOAT", "GOLF", "GROW",
  "HAIR", "HAND", "HARD", "HEAT", "HERB", "HINT", "HOLE", "HOME", "HOST", "HURT",
  "ICON", "IDEA", "IDLE", "IDOL", "INCH", "INFO", "ITEM", "IRON",
  "JAIL", "JOKE", "JUMP",
  "KIND", "KING", "KITE",
  "LADY", "LAMB", "LAND", "LAST", "LEAF", "LEFT", "LINE", "LINK", "LOCK", "LONG", "LOST", "LOUD", "LOVE", "LUCK",
  "MAIL", "MAIN", "MALE", "MARK", "MASK", "MATE", "MEAL", "MICE", "MILK", "MINT", "MORE", "MOVE",
  "NAIL", "NAME", "NEAR", "NEAT", "NEST", "NICE", "NOSE", "NOTE",
  "OPEN", "ORAL", "ORES", "OVAL", "OVEN",
  "PACE", "PAIR", "PALM", "PARK", "PART", "PAST", "PINK", "PLAY", "PORT", "POUR", "PURE",
  "QUIT", "QUIZ",
  "RACE", "RAIN", "REAL", "REST", "RICH", "RISK", "ROCK", "ROPE",
  "SAFE", "SALT", "SAND", "SCAN", "SEAL", "SEAT", "SEND", "SHIP", "SHOCK", "SILK", "SKIP", "SLOT", "SOAP", "SOIL", "SORT", "SPOT", "STAR", "STOP", "SUIT", "SURE",
  "TAIL", "TAPE", "TAXI", "TEAM", "TEAR", "TERM", "TILE", "TIME", "TIRE", "TOUR", "TRAP", "TRIP", "TRUE", "TUBE", "TURN",
  "UNIT", "USER",
  "VERB", "VISA", "VOTE",
  "WAIT", "WANT", "WAVE", "WEAK", "WEAR", "WEST", "WIDE", "WIND", "WINE", "WISH", "WOLF", "WORD", "WORM", "WRAP",
  "YOGA",
  "ZERO", "ZINC", "ZONE"]
while(True):
    print("\t\t\nWelcome to the Word Guessing Game!!")
    print("\nRules:-")
    print("\t1. You have 10 chances to guess.")
    print("\t2. Word has 4 unique letters(letter should not repeat).")
    print("\t3. A word should have a specific meaning.")
    print("\nI think you have read all the rules above")
    print("\nLet's begin the game:-")
    word = random.choice(words_list)
    attempts = 10
    guessed = 0
    while(attempts>0):
        print("\nYou have", attempts, "chances left.")
        guess = input("\nEnter your Guess: ").upper()
        if(len(set(guess)) != 4 or len(guess) != 4):
            print("Read the above rules again!!")
            print("Try again with different word!!\n")
            continue
        correct_letters,correct_position = guessword(guess,word)
        print("correct letters:",correct_letters,", correct position:", correct_position)
        if(correct_position == 4):
            print("Congratulations!!\nYou have guessed the correct word !")
            guessed = 1
            break
        attempts -= 1
    if(guessed == 0):
        print("\nYou have ran out of attempts.\nThe correct word was " + word)
