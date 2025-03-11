import random
list1 = ['odd','even']
list2 = ['bat','bowl']
score1 = 0
score2 = 0
bat1 = 0
bat2 = 0
bowl1 = 0
bowl2 = 0
target = 0
while True:
    print("\n\t\tIt's a Toss Time....\n\n\n")
    toss = input("Choose odd or even: ").lower()
    if toss in list1:
       break
    else:
        print("Invalid choice!!,please try again")
while True:
    num1 = int(input("Please Enter a number from 1 to 6:"))
    if(num1 >= 1 and num1 <= 6):
        break
    else:
        print("Invalid number!!,please try again")
num2 = random.randint(1,6)
print("computer Chose:", num2)
sum = num1+num2
if(sum % 2 == 0):
    if(toss == 'even'):
        while True:
            user_choice = input("You Won the toss, Choose to(Bat/Bowl): ").lower()
            if user_choice in list2:
                break
            else:
                print("Invalid Choice!!, Please Try again")
        print("\n\nYou Won the toss, Chose to "+ user_choice)
        if(user_choice ==  'bat'):
            while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat1
                        print("Your Score is ",score1)
                    if(bat1 == bat2):
                        print("You are OUT!!")
                        print("Computer is batting")
                        target = score1 + 1
                        print("Computer's Target is ", target)
                        break
                else:
                   print("Invalid number !!, Please Try again")
            while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl2
                        print("Computer Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("Computer Win!!")
                            break
                    if(bowl1 == bowl2):
                        print("Computer Score = ",score2)
                        print("Computer is OUT!!")
                        print("You win by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")        
        else:
            while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat2
                        print("Computer's Score is ",score1)
                    if(bat1 == bat2):
                        target = score1 + 1
                        print("computer is OUT!!")
                        print("you are batting")
                        print("Your's Target is ",target)
                        break
                else:
                    print("Invalid number !!, Please Try again")
            while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl1
                        print("Your Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("You Win!!")
                            break
                    if(bowl1 == bowl2):
                        print("Your Score = ",score2)
                        print("You are OUT!!")
                        print("Computer Won by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")        
    else:
        computer_choice = random.choice(list2)
        print("Computer Won the toss, Choose to " + computer_choice)
        if(computer_choice == 'bat'):
            while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat2
                        print("Computer's Score is ",score1)
                    if(bat1 == bat2):
                        print("Computer is OUT!!")
                        print("You are batting")
                        target = score1 + 1
                        print("Your's Target is ", target)
                        break
                else:
                   print("Invalid number !!, Please Try again")
            while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl1
                        print("Your Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("You Win!!")
                            break
                    if(bowl1 == bowl2):
                        print("You Score = ",score2)
                        print("Your are OUT!!")
                        print("Computer won by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")
        else:
            while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat1
                        print("Your Score is ",score1)
                    if(bat1 == bat2):
                        print("you are OUT!!")
                        print("Computer is batting")
                        target = score1 + 1
                        print("Your's Target is ", target)
                        break
                else:
                   print("Invalid number !!, Please Try again")
            while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl2
                        print("Computer's Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("Computer Win!!")
                            break
                    if(bowl1 == bowl2):
                        print("Your Score = ",score2)
                        print("You are OUT!!")
                        print("You won by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")                    
else:
    if(toss == 'odd'):
        while True:
            user_choice = input("You Won the toss, Choose to(Bat/Bowl): ").lower()
            if user_choice in list2:
                break
            else:
                print("Invalid Choice!!, Please Try again")
        print("\n\nYou Won the toss, Chose to "+ user_choice)
        if(user_choice ==  'bat'):
           while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat1
                        print("Your Score is ",score1)
                    if(bat1 == bat2):
                        target = score1 + 1
                        print("You are OUT!!")
                        print("Computer is batting")
                        print("Computer's Target is ",target)
                        break
                else:
                   print("Invalid number !!, Please Try again")
           while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl2
                        print("Computer Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("Computer Win!!")
                            break
                    if(bowl1 == bowl2):
                        print("Computer Score = ",score2)
                        print("Computer is OUT!!")
                        print("You win by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")
        else:
            while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat2
                        print("Computer's Score is ",score1)
                    if(bat1 == bat2):
                        target = score1 + 1
                        print("computer is OUT!!")
                        print("you are batting")
                        print("Your's Target is ", target)
                        break
                else:
                    print("Invalid number !!, Please Try again")
            while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl1
                        print("Your Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("You Win!!")
                            break
                    if(bowl1 == bowl2):
                        print("Your Score = ",score2)
                        print("You are OUT!!")
                        print("Computer Won by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")
    else:
        computer_choice = random.choice(list2)
        print("Computer Won the toss, Choose to " + computer_choice)
        if(computer_choice == 'bat'):
            while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat2
                        print("Computer's Score is ",score1)
                    if(bat1 == bat2):
                        print("Computer is OUT!!")
                        print("You are batting")
                        target = score1 + 1
                        print("Your's Target is ", target)
                        break
                else:
                   print("Invalid number !!, Please Try again")
            while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl1
                        print("Your Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("You Win!!")
                            break
                    if(bowl1 == bowl2):
                        print("You Score = ",score2)
                        print("Your are OUT!!")
                        print("Computer won by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")
        else:
            while True:    
                bat1 = int(input("Enter a number from 1 to 6: "))
                if(bat1 >= 1 and bat1 <= 6):
                    bat2 = random.randint(1,6)
                    print("Computer chose =",bat2)
                    if(bat1 != bat2):
                        score1 += bat1
                        print("Your Score is ",score1)
                    if(bat1 == bat2):
                        print("You are  OUT!!")
                        print("Computer is batting")
                        target = score1 + 1
                        print("Computer's Target is ", target)
                        break
                else:
                   print("Invalid number !!, Please Try again")
            while True:
                bowl1 = int(input("Enter a number from 1 to 6:"))
                if(bowl1 >= 1 and bowl1 <= 6):
                    bowl2 = random.randint(1,6)
                    print("Computer chose = ",bowl2)
                    if(bowl1 != bowl2):
                        score2 += bowl2
                        print("computer's Score = ",score2)
                        if(target > score2):
                            print("Total Runs required to Win",target - score2)
                        if(target <= score2):
                            print("Computer Won!!")
                            break
                    if(bowl1 == bowl2):
                        print("Computer's Score = ",score2)
                        print("Computer  is OUT!!")
                        print("You won by ",score1 - score2 ,"runs !!")
                        break
                else:
                    print("Invalid number !!, Please Try again")
