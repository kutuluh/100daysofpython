#   
#   
#   
#   # 🚨 Don't change the code below 👇
#   two_digit_number = input("Type a two digit number: ")
#   # 🚨 Don't change the code above 👆
#   
#   ####################################
#   #Write your code below this line 👇
#   
#   first_digit = two_digit_number[0]  
#   second_digit = two_digit_number[1]
#   
#   result = int(first_digit) + int(second_digit)
#   print(result)

   #    Mathematical operations in python

   #   3+5
#   7-4
#   3*2
#   6/3
#   2**3



#PEMDASLR  order or priority in which operations are carried out 
#  parenthesis
#  exponents
#  multiplication
#  division 
#  addition
#  substraction
#  
#  ()
#  **
#  * /
#  + -

# print(3*3+3/3-3)
# 
# result 7
# 
# 3*3=   9
# 3/3=   1
#  -3=  -3
#        7

#  Ex2
#  
#  # 🚨 Don't change the code below 👇
#  height = input("enter your height in m: ")
#  weight = input("enter your weight in kg: ")
#  # 🚨 Don't change the code above 👆
#  
#  #Write your code below this line 👇
#  
#  bmi = int(weight) / float(height) ** 2
#  bmi_as_int = int(bmi)
#  
#  print(bmi_as_int)

#ex3

#  # 🚨 Don't change the code below 👇
#  age = input("What is your current age?")
#  # 🚨 Don't change the code above 👆
#  
#  #Write your code below this line 👇
#  
#  weeks_in_90years = 52 * 90
#  
#  days_in_90years = 365 * 90
#  
#  months_in_90years = 12 * 90
#  
#  
#  weeks_left = weeks_in_90years -  int(age) * 52 
#  
#  days_left = days_in_90years - int(age) * 365
#   
#  months_left = months_in_90years - int(age) * 12
#  
#  print("you have " + str(days_left) + " days    " + str(weeks_left) + " weeks  " + str(months_left) + " months  ")

#TIPPING CALC

# #If the bill was $150.00, split between 5 people, with 12% tip. 
# #Each person should pay (150.00 / 5) * 1.12 = 33.6
# #Round the result to 2 decimal places.
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))
# 
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# 
# 
# # FAQ: How to round to 2 decimal places?
# 
# # Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
# 
# 
# print(f"Each person should pay: ${final_amount}")

