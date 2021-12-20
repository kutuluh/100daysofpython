# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆#  
# #Write your code below this line 👇#  
# if (number % 2) == 0:
# print("This is an even number.".format(number))
# else:
# print("This is an odd number.".format(number))


#ex2
 
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))if height >= 120:
#print("You Can Ride the rollercoaster!")
#age = int(input("What is your age? "))
#if age <= 12:
#    print("Please pay $5.")
#elif 12 < age < 18:
#    print("please pay $7. ")
#else:  
#    print("Please pay $12. ")else:
#print("Sorry you have to grow taller before you can ride.")

## 🚨 Don't change the code below 👇
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
## 🚨 Don't change the code above 👆
#
##Write your code below this line 👇
#  
#bmi = int(weight) / float(height) ** 2
#bmi_to_round = float(bmi)
#bmi_as_int = round(bmi_to_round)
#if bmi_to_round < 18.5:
#  print("Your BMI is " + str(bmi_as_int) + "  You are underweight.")
# 
#elif 18.5 < bmi_to_round < 25:
#    print("Your BMI is " + str(bmi_as_int) + " You have a normal weight.")
#
#elif 25 < bmi_to_round < 30:
#    print("Your BMI is " + str(bmi_as_int) + " You are Slightly overweight.")
#    
#elif 30 < bmi_to_round < 35:
#    print("Your BMI is " + str(bmi_as_int) + " You are obese.")
#
#else:
# print("Your BMI is " + str(bmi_as_int) + " You are clinically obese.")



##ex3
## 🚨 Don't change the code below 👇
#year = int(input("Which year do you want to check? "))
## 🚨 Don't change the code above 👆
#
##Write your code below this line 👇
#
#if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("Leap Year.")
#     else:
#         print("Leap year.")
#else:
#    print("Not leap year.")         


# 
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height >= 120:
#  print("You Can Ride the rollercoaster!")
#  age = int(input("What is your age? "))
#  if age <= 12:
#    bill = 5
#    print("Child tickets are $5.")
#  elif 12 < age < 18:
#    bill = 7
#    print("Youth tickets are $7. ")
#  else:  
#    bill = 12
#    print("Adult tickets are $12. ")
#  wants_photo = input("Do you want a photo taken? Y or N. ")
#  if wants_photo == "Y" or wants_photo == "y":
#      bill +=3
#  print(f"Your final bill is ${bill}")
#else:
#  print("Sorry you have to grow taller before you can ride.")



## 🚨 Don't change the code below 👇
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
## 🚨 Don't change the code above 👆
#
##Write your code below this line 👇
#if size == "S":
#  bill = 15
#  if add_pepperoni == "Y":
#     bill +=2
#  if extra_cheese == "Y":
#     bill +=1
#     print(f"Your final bill is: ${bill}.")
#  else:
#     print(f"Your final bill is: ${bill}.")  
#
#elif size == "M":
#  bill = 20
#  if add_pepperoni == "Y":
#     bill +=3
#  if extra_cheese == "Y":
#     bill +=1
#     print(f"Your final bill is: ${bill}.")
#  else:
#     print(f"Your final bill is: ${bill}.")   
#
#elif size == "L":
#  bill = 25
#  if add_pepperoni == "Y":
#     bill +=3
#  if extra_cheese == "Y":
#     bill +=1
#     print(f"Your final bill is: ${bill}.")
#  else:
#      print(f"Your final bill is: ${bill}.")


#
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height >= 120:
#  print("You Can Ride the rollercoaster!")
#  age = int(input("What is your age? "))
#  if age <= 12:
#    bill = 5
#    print("Child tickets are $5.")
#  elif 12 < age < 18:
#    bill = 7
#    print("Youth tickets are $7. ")
#  elif  45 <= age <= 55:
#      bill = 0
#      print("Everything is going to be ok. Have a free ride on us!") 
#  
#  else:  
#    bill = 12
#    print("Adult tickets are $12. ")
#  wants_photo = input("Do you want a photo taken? Y or N. ")
#  if wants_photo == "Y" or wants_photo == "y":
#      bill +=3
#  print(f"Your final bill is ${bill}")
#else:
#  print("Sorry you have to grow taller before you can ride.")

## 🚨 Don't change the code below 👇
#print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
## 🚨 Don't change the code above 👆
#
##Write your code below this line 👇
#lower_name1 = name1.lower()
#lower_name2 = name2.lower()
#names = lower_name1+lower_name2
#T = int(names.count("t"))
#R = int(names.count("r"))
#U = int(names.count("u"))
#E = int(names.count("e"))
#L = int(names.count("l"))
#O = int(names.count("o"))
#V = int(names.count("v"))
#E3 = int(names.count("e"))
#true = str(T+R+U+E)
#love = str(L+O+V+E)
#result = true+love
#addr = int(result)
#
#if (addr < 10) or (addr > 90):
#  print(f"Your score is {addr}, you go together like coke and mentos.")
#elif  (40 < addr) and (addr < 50):
#       print(f"Your score is {addr},  you are alright together")
#else:
#    print(f"Your score is {addr}.")


#print('''
#*******************************************************************************
#          |                   |                  |                     |
# _________|________________.=""_;=.______________|_____________________|_______
#|                   |  ,-"_,=""     `"=.|                  |
#|___________________|__"=._o`"-._        `"=.______________|___________________
#          |                `"=._o`"=._      _`"=._                     |
# _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
#|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
#|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
# _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
#|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
#|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
#____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
#/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
#____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
#/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
#____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
#/______/______/______/______/______/______/______/______/______/______/_____ /
#*******************************************************************************
#''')
#print("Welcome to Treasure Island.")
#print("Your mission is to find the treasure.") 
#
##https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#
##Write your code below this line 👇
#lor = input("You're at a crossroad. Where do you want to go?... Type left or right")
#if lor == "left":
#    sow = input("'You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across.'")
#    if sow == "wait":
#        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
#        if door == "red":
#            print("Burned")
#        elif door == "blue":
#            print("Eaten")    
#        elif door == "yellow":
#            print("You found the treasure! You Win!")  
#        else:
#            print("You enter a room of beasts. Game Over.")      
#
#    else:
#        print("You get attacked by an angry trout. Game Over.")    
#else:
#    print("You fell into a hole. Game Over.")
#           