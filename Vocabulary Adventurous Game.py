import time
import random
import sys
#variable
streaks1 = 0
streaks2 = 0
streaks3 = 0
streaks4 = 0

level1 = 1
level2 = 1
level3 = 1
level4 = 1


generated_number1 = set()
generated_number2 = set()
generated_number3 = set()
generated_number4 = set()
total = 40

def unique(total,generated_numbers1):
    if(len(generated_numbers1) == total):
        generated_numbers1.clear()
    while True:
        n1 = random.randint(0,total)
        if n1 not in generated_numbers1:
            generated_numbers1.add(n1)
            return n1

message = """
------------------------------------------------------------------------------------------------------------------------------------------------------------
\t\t\t\t\t\t\t🔤 Welcome to the Vocabulary Adventurous Game!

In this game, you'll embark on an exciting journey to expand your vocabulary by guessing words based on given clues.

Here's how to play:

1. Objective:

Your goal is to correctly guess the word that corresponds to the clue provided at each level.

2. Levels:

The game is divided into four distinct levels, each increasing in difficulty:

a. Easy: Clues are straightforward, and the words are common. This level is designed to warm you up.
b. Intermediate: Clues become a bit more challenging, requiring you to think a little deeper.
c. Professional: Expect more complex clues and less common words. This level is for players with a strong vocabulary.
d. Hard: The ultimate test! Clues are cryptic, and the words are rare or have multiple layers of meaning.

3. Gameplay Mechanics:

Clue Presentation: At the start of each level, you'll be given a clue related to a specific word.
Unlimited Attempts: You have unlimited tries to guess the correct word for each level. Don’t worry about making mistakes—take your time to think it through!
Advancing Levels: Once you successfully guess the word at your current level, you automatically progress to the next level.
Feedback: After each guess, you will receive immediate feedback. If your guess is incorrect, keep trying until you find the right word.
Lifelines: At the first level, you will start with only one lifeline. As you clear each level, your lifelines will increase, giving you additional support as you continue your journey.
Note: Tenses also matters
Note: Give more importance to the single quoted word in the clue.

4. Streaks:
This variable keeps track of the number of consecutive times you have successfully completed the entire game.
Each time you complete the final level (i.e., after the Hard level), your streak count increases by 1.
If you give up during any level (by pressing '2'), your streak resets to 0.
Keep pushing your limits and try to beat your high streak!
5. Tips for Success:

Think about the clue carefully and consider multiple meanings or associations.
Use your vocabulary knowledge and intuition to deduce the correct word.
Don't be afraid to use your lifelines when you need a little extra help.
Stay positive and have fun! This game is designed to challenge
you and help you learn new words along the way.
Enjoy the process of learning new words and challenging yourself as the game progresses.
------------------------------------------------------------------------------------------------------------------------------------------------------------
            """
def game(level,mode,streaks,defi1,len1,lifeline,word1,n):
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nLevel: ⚔️ ",level,"\t\t\t\t\t\t\tMode: 🔹"+mode,"\t\t\t\t\t\t\tStreaks: 🔥",streaks)
        print("\nClue: "+ defi1)
        print("Word has",len1,"letters")
        print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------")
        dash = ["* "]*len1 # dashes
        while(True):
            print("\nMy Word: ","".join(dash))
            print("\nLifeline: ",lifeline)
            guess = input("\nEnter your Word: ").lower()
            if(len(guess) == 1):
                if(guess == "1"):
                    lifeline-= 1
                    if(lifeline == -1):
                        print("You have already used all lifelines!!")
                        lifeline = 0
                    else:
                        word_letters = []
                        nospacedash = [x.strip() for x in dash]
                        for c in word1:
                            if c not in nospacedash:
                                word_letters.append(c)
                        if word_letters:
                            random_letter = random.choice(word_letters)
                            for i,ch in enumerate(word1):
                                if ch == random_letter:
                                    dash[i] = random_letter
                elif(guess == "2"):
                    print("You gave up!!")
                    print("The word was: ",word1)
                    streaks = 0
                    break
                elif(guess == "?"):
                    print("Exit from the mode and get the information about the game!!")
                elif(guess == "q"):
                    print("You quit the game!!")
                    while(True):
                        n = input("\nEnter the Mode you want to play: ")
                        if(n == "e" or n == "i" or n == "P" or n == "h"):#h
                            break
                        else:
                            print("You have entered wrong mode!!")
                            print("Please enter the correct mode!!")
                    break
                else:
                    print("My word has only", len1 ,"letters,so Try again with different word!!")
            elif(len(guess) != len1):
                print("My word has only", len1 ,"letters,so Try again with different word!!")
            else:
                if(guess != word1):
                    print("Well tried but it's not my word")
                else:
                    print("Congralutations!!, you guessed the correct word")
                    level += 1
                    streaks += 1
                    break
        return level, mode,lifeline,streaks,n
print("\t\t\t\t\t\t\t🔤 Welcome to Vocabulary Adventures Game\n")
print("\n loading game....", flush=True)
time.sleep(3)
sys.stdout.write('\033[F')  # Move cursor up one line.
sys.stdout.write('\033[K')  # Clear to the end of line.
print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t📜 Rules:-")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("1. Guess the word 🎯 by the given clue🔍.")
time.sleep(2)
print("2. You have 1 💡 lifeline each reveals one letter of word.")
time.sleep(2)
print("3. Enter 1 to use 💡 lifeline.")
time.sleep(2)
print("4. Enter 2 to 😩 give up.")
time.sleep(2)
print("5. Enter ? to get the information about the game 📝.")
time.sleep(2)
print("6. Word should not contain any special characters.")
time.sleep(2)
print("7. You have 4 Modes.")
time.sleep(2)
print("  ✌️ Easy.\n  🤨 Intermediate.\n  👔 Professional.\n  💪 Hard.")
time.sleep(3)
print("\n   Enter e for Easy.\n   Enter i for Intermediate.\n   Enter p for Professional.\n   Enter h for Hard.")
time.sleep(3)
print("I think you have read all the Rules!!\n\n")
time.sleep(2)
while(True):
    n = input("\nEnter the Mode you want to play: ")
    if(n == "e" or n == "i" or n == "P" or n == "h"):
        break
    else:
        print("You have entered wrong mode!!")
        print("Please enter the correct mode!!")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\t🎉 Let's start the game!!")

while(True):
    if(n == "e"):
        clue1 = {
            "sharp" : "Having a 'fine edge' or point that can cut.",
            "kitchen" : "A room or area where food is 'prepared and cooked'.",
            "fast" : "Moving quickly or able to move 'quickly'.",
            "water" : "A clear, 'tasteless' liquid essential for most forms of life.",
            "brave" : "Showing courage and 'facing danger', fear, or difficulty without hesitation.",
            "slow" : "Taking 'longer' than expected or desired.",
            "sour" : "Having an acidic, tangy, or 'sharp flavour'.",
            "bag" : "A container for 'carrying things'.",
            "fix" : "To 'repair' or mend something.",
            "blank" : "'Empty' or without content.",
            "dew" : "'Tiny drops of water' on surfaces in the morning.",
            "gloves" : "A covering for the 'hands'.",
            "craft" : "An activity involving skill in making things by 'hand'.",
            "cab" : " A 'taxi' or a car for hire.",
            "frog" : "A small amphibian with smooth skin, often found 'near water'",
            "torch" : "A device that produces 'light'.",
            "road" : " A pathway or 'route' for vehicles and pedestrians.",
            "train" : "A mode of transportation that runs on 'tracks'.",
            "guitar" : "A 'six stringed' instrument used in many songs.",
            "piano" : "A musical instrument with 'black and white keys'.",
            "chair" : "Something you pull out for 'sit on' at a dinning table.",
            "table" : "furniture were people 'place thing, eat, or work'.",
            "keyboard" : "A 'set of keys' on a computer or typewriter.",
            "dark" : "Having little or 'no light'.",
            "heart" : "A muscular organ that 'pumps blood' through the body.",
            "brain" : "The organ that controls 'thought, memory, and emotion'.",
            "smile" : "A 'facial expression' showing happiness or pleasure.",
            "triangle" : "A plane figure with 'three sides and three angles'.",
            "cry" : "To shed 'tears' due to pain, sadness, or strong emotion.",
            "candle" : "A stick of wax with a wick that 'emits light' when burned.",
            "soil" : "The upper layer of earth in which 'plants grow'.",
            "flower" : "The 'reproductive part' of a plant.",
            "market" : "A place where goods are 'bought and sold'.",
            "money" : "A 'medium of exchange' for goods and services.",
            "kingdom" : "A country, state, or territory ruled by a 'king or queen'.",
            "pond": "A small body of 'still water', often found in gardens or parks.",
            "ship": "A large vessel designed for 'water transportation', carrying goods or passengers.",
            "grow": "To 'increase in size', number, or mature over time.",
            "bold": "Showing a 'willingness to take risks'; confident and courageous.",
            "pen" : "A writing instrument that uses 'ink' to leave marks on paper or another surface.",
            "game": "An activity or sport with rules that involves 'competition and fun'.",
        }
        n1 = unique(total,generated_number1)
        lifeline = 3
        mode = "EASY"
        defi1 = list(clue1.values())[n1]   # clue 1
        word1 = list(clue1.keys())[n1] #word 1
        len1 = len(list(clue1.keys())[n1]) #len of word 1

        #main
        level1,mode,lifeline,streaks1,n = game(level1,mode,streaks1,defi1,len1,lifeline,word1,n)
    elif(n == "i"):
        clue2 = {
            "bowling" : "A sport in which players 'roll a ball' to knock down pins.",
            "flowchart" : "A diagram showing a 'process or steps'.",
            "mighty" : "Having 'great strength', influence, or force.",
            "playground" : "An 'outdoor area' provided for children to play.",
            "laugh" : "To make sounds with the voice that show 'happiness'.",
            "cafe" : "A small establishment where you can 'enjoy coffee' and light snacks.",
            "background" : "The area 'behind the main object' or focus.",
            "magnetic" : "Exhibiting the 'properties of a magnet'; capable of attracting ferrous materials.",
            "organic" : "Relating to or 'derived from living matter'; not synthetic.",
            "chapter" : "A division or 'section in a book' or period of history.",
            "jackpot" : "A 'large cash prize' in a game or lottery.",
            "equation" : "A mathematical statement that asserts the 'equality of two expressions'.",
            "hospital" : "An building providing 'medical and surgical treatment' and nursing care.",
            "light" : " Electromagnetic radiation which is 'visible to the human eye'.",
            "diamond" : "The 'hardest nature' substance often used in jewelery.",
            "chalk" : "A white soft earthy limestone used for 'writing or drawing'.",
            "sprint" : "To run at 'full speed over a short distance'.",
            "pencil" : "A writing tool made of 'wood with graphite center'.",
            "journey": "To travel from 'one place to another', often on an adventurous trip.",
            "watch": "A device used to 'tell time', usually worn on the bristor hung on wall.",
            "calm": "'Peaceful', without excitement.",
            "honest": "Truthful and sincere.",
            "discover": "To find or 'learn something' for the first time which is already invented.",
            "absent": "'Not present' or available; missing from a place or event.",
            "luck": "The success or failure brought 'by chance' rather than effort.",
            "rope": "A long, flexible material used for 'tieing, pulling lifting objects'.",
            "dare": "To have the courage to do something challenging or risky.",
            "antique" : "A collectible object with 'high value' due to its age and quality.",
            "blanket" : "A large piece of cloth used for keeping warm, especially on a 'bed'.",
            "failure" : "'Lack of success' in achieving a goal or objective.",
            "farming" : "The practice of 'cultivating the land' and raising animals for food and other products.",
            "history" : "The study of 'past events', particularly in human affairs.",
            "picture" : "A 'visual representation' of a person, object, or scene.",
            "another" : "One more; an additional one.",
            "victory" : "An act of 'defeating an enemy' or opponent in a battle, game, or other competition.",
            "outside" : "The 'external side' or surface of something.",
            "fashion" : "A 'popular trend' in clothing, accessories, or behavior.",
            "music" : "The art created by 'organising sound rythm' and melodies.",
            "players" : "A 'person' who takes part in a game or sports.",
            "voltage" : "The 'measure' of electrical potential difference between two points in a circuit.",
            "mobile" : "A portable device that allows for 'communication' or access to information.",
}
        lifeline = 3
        n2 = unique(total,generated_number2)
        defi2 = list(clue2.values())[n2]   #clue 2
        word2 = list(clue2.keys())[n2] #word 2
        len2 = len(list(clue2.keys())[n2])
        mode = "INTERMEDIATE"
        level2,mode,lifeline,streaks2,n = game(level2,mode,streaks2,defi2,len2,lifeline,word2,n)
    elif(n == "P"):
        clue3 = {
                "capture" : "To seize or acquire something by force or strategy.",
                "liberty" : "The state of being free within society from oppressive restrictions.",
                "predict": "To say what will happen in the future.",
                "campfire" : "A fire built outdoors for warmth, cooking, or social gatherings.",
                "harmonic" : "In wave Physics, any periodic signal can be decomposed into a series of sinusoidal components at different frequencies using fourier analysis.",
                "dynamic" : "Characterized by constant change, activity, or progress.",
                "elastic" : "The object which returns to original shape after deforming.",
                "network" : "A group or system of interconnected people or things.",
                "algorithm" : "A well defined, step by step procedure or set of rules designed to perform a specific task or solve a particular problem.",
                "product": "An article or substance that is manufactured or refined for sale.",
                "software" : "The programs and other operating information used by a computer.",
                "consult" : "To seek expert advice or offer professional guidance.",
                "mentors" : "An experienced and trusted adviser.",
                "merchant" : "A person or company involved in wholesale trade.",
                "profits" : "A financial gain, especially the difference between the amount earned and the amount spent.",
                "savings" : "Money saved or kept aside for future use.",
                "formula" : "Concise, symbolic way to represent a relationship or rule betweeen different quantities.",
                "profile" : "A summary of qualifications, experience, or characteristics, often used for professional networking.",
                "organise" : "To arrange systematically in order.",
                "signal": "A transmitted electrical impulse representing data or information.",
                "dynamics": "The branch of mechanics concerned with the forces and motion of bodies.",
                "spectrum": "A range of different frequencies or wavelengths, such as in light or sound.",
                "amplitude": "The maximum extent of a vibration or oscillation, measured from the position of equilibrium.",
                "exports" : "Goods or services sold to a foreign country.",
                "verdicts" : "A decision on a disputed issue in a civil or criminal case.",
                "penalty" : "A punishment imposed for breaking a law, rule, or contract.",
                "printer" : "A device that produces physical copies of text or images.",
                "laser" : "A device that emits a narrow, intense beam of light.",
                "plastic" : "A synthetic material made from polymers, widely used in all over world.",
                "justice" : "The quality of being fair and reasonable; the administration of the law.",
                "gambler" : "A person who bets money on an uncertain outcome.",
                "skydive" : "To jump from an aircraft and descend by parachute; also used as a theme or activity in extreme sports games.",
                "upgrade" : "To improve or enhance the quality or functionality of a product or service.",
                "fighter" : "A person or character who engages in combat or warfare.",
                "reloads" : "To fill a weapon with ammunitions again.",
                "storage" : "The act of keeping or storing goods or data safely.",
                "retails" : "Sells goods or services directly to consumers.",
                "rematch" : "To compete against an opponent again, often after a previous contest.",
                "refunds" : "Money returned to a customer, typically after a return or cancellation.",
                "customer" : "A person or organization that buys goods or services from a store or business.",
                "replays" : "Recorded sessions of gameplay that can be watched again, often used for review or sharing highlights.",
            }
        lifeline = 3
        n3 = unique(total,generated_number3)
        mode = "PROFESSIONAL"
        defi3 = list(clue3.values())[n3]   #clue 3
        word3 = list(clue3.keys())[n3] #word 3
        len3 = len(list(clue3.keys())[n3])
        level3,mode,lifeline,streaks3,n = game(level3,mode,streaks3,defi3,len3,lifeline,word3,n)
    elif(n == "h"):
        clue4 = {
                "supernova" : "A powerful and luminous explosion marking the end of a star's life cycle.",
                "invadar" : "A person or group that enters a country or territory",
                "loading" : "The process of preparing software or data for use.",
                "unlocks" : "To open, release, or enables access to a feature or content in a game that was previously restricted or hidden.",
                "graphics" : "Visual elements or designs produced by computers, essential in digital media and design.",
                "imports" : "Goods or services brought into a country from abroad for sale or use.",
                "advisor" : "A person who provides expert guidance.",
                "respawn" : "To reappear in a game after being killed.",
                "improve" : "To make or become better in quality or condition.",
                "employs" : "To give work to (someone) and pay them for it.",
                "details" : "Specific pieces of information or particulars.",
                "teamwork" : "The combined action of a group of people, especially when effective and efficient.",
                "backups" : "Extra copies of data made to guard against data loss.",
                "updates" : "The latest information or news.",
                "investor" : "A person or organization that puts money into financial schemes.",
                "clients" : "A person or organization using the services of a professional person or company.",
                "routine" : "A sequence of actions regularly followed; a fixed program.",
                "cluster" : "A group of similar things or occurring closely together.",
                "convert" : "To change or make something into another form.",
                "journal" : "A daily record of news and events of a personal nature.",
                "confirm" : "To verify or validate details or decisions in a professional setting.",
                "purchase" : "The 'act of buying goods' or services.",
                "granted" : "Given or approved, as in permissions or requests in a professional setting.",
                "caption" : "A title or brief explanation appended to an article, illustration, or poster.",
                "seminar" : "A meeting or training session on a specific topic, typically for professional development.",
                "duration" : "The length of time something lasts; important for project planning and deadlines.",
                "busying" : "Keeping oneself occupied with a particular activity.",
                "informed" : "Being provided with details or facts about something.",
                "ratings" : "An evaluation of performance or quality, as in feedback or reviews.",
                "publish" : "To make information available to the public.",
                "mindset" : "A particular way of thinking or a mental attitude that shapes behavior.",
                "focused" : "Concentrated on a particular task or goal.",
                "complex" : "Consisting of many interconnected parts; often used to describe multifaceted projects.",
                "optical" : "Relating to sight, especially in relation to the physical properties of light.",
                "deposit" : "Money placed into a bank account or fund; a financial contribution.",
                "justify" : "To show or prove to be right or reasonable.",
                "lawyer" : "A professional who practices law and represents clients in legal matters.",
                "funding" : "Money provided for a project or venture.",
                "outcome" : "The result or effect of an action or event.",
                "reactor" : "A device used to contain and control nuclear reactions.",
                "bipolar" : "Having two extremes or poles; often used in contexts ranging from mood disorders to systems with dual aspects."
        }
        n4 = unique(total,generated_number4)
        lifeline = 3
        mode = "HARD"
        defi4 = list(clue4.values())[n4]   #clue 4
        word4 = list(clue4.keys())[n4] #word 4
        len4 = len(list(clue4.keys())[n4])
        level4,mode,lifeline,streaks4,n = game(level4,mode,streaks4,defi4,len4,lifeline,word4,n)
    elif(n == "?"):
        print(message)
        break