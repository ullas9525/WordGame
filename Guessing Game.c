#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include<string.h>
int position(char *guess, const char *word)
{
    int correct_position = 0;
    for(int i = 0;i < 4;i++)
    {
        if(guess[i] == word[i])
        {
            correct_position += 1;
        }
    }
    return correct_position;
}
int letter(char *guess,const char *word)
{
    int correct_letter = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (guess[i] == word[j]) {
                correct_letter+= 1;
                break;
            }
        }
    }

    return correct_letter;
}
int main() {
    const char *words_list[] = {
  "ABLE", "ACID", "AUNT",
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
  "ZERO", "ZINC", "ZONE"
};
    int numWords = 206;
    srand(time(NULL));
    int randomIndex = rand() % numWords;
    int copy = 0,correct_letter = 0,correct_position = 0;
    char *word = words_list[randomIndex];
    char guess[10];
    printf("\t\t Welcome to Word Guessing Game!!\n");
    printf("Rules:-\n");
    printf("1. You have 10 Chances to guess the word.\n");
    printf("2. Word should have 4 unique letters(letter should not repeat).\n");
    printf("3. A word should have specific meaning.\n");
    printf("I think you have read all the above rules.\n");
    printf("Let's begin the Game.\n");
    int attempts = 10;
    int guessed = 0;
    while(attempts > 0)
    {
        printf("\nYou have %d chances left",attempts);
        printf("\nEnter your Guess: ");
        scanf("%s",&guess);
        strupr(guess);
        if(strlen(guess) != 4)
        {
            printf("Read the rules again!!\n");
            printf("try again with different word!!\n");
            continue;
        }
        for(int i = 0;i < 4;i++)
        {
            for(int j = i + 1;j < 4;j++)
            {
                if(guess[i] == guess[j])
                {
                    copy = copy + 1;
                    printf("Read the rules again!!\n");
                    printf("try again with different word!!\n");
                    break;
                }
            }
        }
        if(copy>0)
        {
            copy = 0;
            continue;
        }
        correct_position = position(guess,word);
        correct_letter = letter(guess,word);
        printf("correct letters: %d, correct position: %d",correct_letter,correct_position);
        attempts -= 1;
        if(correct_position == 4)
        {
            printf("\nCongratulations!!\nYou have guessed the correct word!!");
            guessed = 1;
            break;
        }
    }
if(guessed == 0)
{
    printf("\nYou have ran out of attempts.\nThe correct word was: %s",word);
}
    return 0;
}
