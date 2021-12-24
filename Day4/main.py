##Remember to use the random module
##Hint: Remember to import the random module here at the top of the file. 🎲
#import random	 
## 🚨 Don't change the code below 👇
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)
# # 🚨 Don't change the code above 👆 It's only for testing your code.
#	 
##Write the rest of your code below this line 👇
#toss_result = random.randint(0, 1)
#if toss_result == 1:
#    print("Heads")
#else:
#    print("Tails")


#import random
#
## 🚨 Don't change the code below 👇
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)
#
## Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
## 🚨 Don't change the code above 👆
#
##Write your code below this line 👇
#num_items = len(names)
#random_choice = random.randint(0, num_items -1)
#person_who_will_pay = names[random_choice]
#print(person_who_will_pay + " is going to buy the meal today!")


#``
## 🚨 Don't change the code below 👇
#row1 = ["⬜️","⬜️","⬜️"]
#row2 = ["⬜️","⬜️","⬜️"]
#row3 = ["⬜️","⬜️","⬜️"]
#map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
#position = input("Where do you want to put the treasure? ")
## 🚨 Don't change the code above 👆
#
##Write your code below this row 👇
#column = int(position[0]) 
#row = int(position[1])-1
#
#
#s_row = map[row - 1]
#s_row[column -1] = "X"
##Write your code above this row 👆
#
##🚨 Don't change the code below 👇
#print(f"{row1}\n{row2}\n{row3}")


#
#rock = '''
#    _______
#---'   ____)
#      (_____)
#      (_____)
#      (____)
#---.__(___)
#'''
#
#paper = '''
#    _______
#---'   ____)____
#          ______)
#          _______)
#         _______)
#---.__________)
#'''
#
#scissors = '''
#    _______
#---'   ____)____
#          ______)
#       __________)
#      (____)
#---.__(___)
#'''
#
##Write your code below this line 👇
#game_images = [rock, paper, scissors]
#
#user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#print(game_images[user_choice])
#
#computer_choice = random.randint(0, 2)
#print("Computer chose:")
#print(game_images[computer_choice])
#
#if user_choice >= 3 or user_choice < 0: 
#  print("You typed an invalid number, you lose!") 
#elif user_choice == 0 and computer_choice == 2:
#  print("You win!")
#elif computer_choice == 0 and user_choice == 2:
#  print("You lose")
#elif computer_choice > user_choice:
#  print("You lose")
#elif user_choice > computer_choice:
#  print("You win!")
#elif computer_choice == user_choice:
#  print("It's a draw")
#
######## Debugging challenge: #########
##Try running this code and type 5.
##It will give you an IndexError and point to line 32 as the issue.
##But on line 38 we are trying to prevent a crash by detecting
##any numbers great than or equal to 3 or less than 0.
##So what's going on?
##Can you debug the code and fix it?
##Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end


