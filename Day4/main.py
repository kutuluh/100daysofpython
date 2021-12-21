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



