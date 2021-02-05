# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# number_one = 7
# number_two = 9
# number_three = 19
# number_four = 17
# if(number_four > number_three):
#     print("this is greater")
# else:
#     print("this is smaller")
# phrase = "anything"
# print(phrase.replace("any","many"))
# user_input = input('how are you today')
#
# print(user_input)
#__________________________build a simple calculator_______________________
# first_number = input("What is your first number: ")
# second_number = input("What is your second number: ")
# sum = float(first_number) + float(second_number)
# print(sum)
#-----------------------------lists-----------------------
# pokemon_id = [0,1,2,3,4]
# pokemon = ["magikarp", "pikachu", "squirtle", "charmander", "bulbasaur"]
# pokemon.extend(pokemon_id)
# print(pokemon[0:10])
#---------------------Tuples is a type of data structure-----------------------------------------------
#examples = (6, 8)
#print(examples[1])
#--------------------------------------functions-----------------------------------------------------------------
# def print2():
#     print("something")
# print2()
# print2()
# print2()
#-------------------------if statements----------------------------------------
# num = 3
# numTwo = 1
# if(numTwo > num) :
#     print("5 greater than 1")
# elif(num > numTwo) :
#     print("1 greater than 3")
#some random assignment translation from java to python
# constant = 10
# print("welcome to wtv")
# #print("please enter a 6 digit number")
#
# user_input = int(input("please enter a 6 digit number"))
# print("generating your number")
#
# lastDigit = int(user_input % constant)
# fifthDigit = int((user_input / constant) % constant)
# fourthDigit = int((user_input / 100) % constant)
# thirdDigit = int((user_input / 1000) % constant)
# secondDigit = int((user_input / 10000) % constant)
# firstDigit = int((user_input / 100000) % constant)
#
# secondDigit = secondDigit % 2
# thirdDigit += 1
# fourthDigit = ((thirdDigit) % 3)
#
# encryptedNumber = ((((((((((lastDigit * constant) + secondDigit) * constant) + thirdDigit) * constant) + fifthDigit) *
#                       constant) + fourthDigit) * constant) + firstDigit)
# print("Your number is: " + str(encryptedNumber))
#--------------------------------------dictionaries--key value pairs------------------------------------
# monthConversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
# }
# ------------------------------while loop----------------------
# i = 1
# while i < 20:
#         print(i)
#         i += i
# ---------------------guessing game------------------
# word = "dog"
# user_input = ""
# print("Guess the 3 letter word: ")
# while user_input != word:
#         user_input = input("")
#         if user_input != word:
#                 print("wrong answer try again :")
#         elif user_input == word:
#                 print("You got the right word")
# -----------------for loops--------------------
# for letter in "abcdefg":
#         print(letter)
# samples = ["bulbasaur", "charmander", "squirtle"]
# for sample in samples:
#         print(sample)
# print a right triangle
# rows = int(input("how many rows would you like the right triangle to be?"))
# for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#                 print('*', end =  '  ')
#         print()
# -----------------Practice---------------
#
# i = 0
# while i <= 10:
#         print(i)
#         i += 1
# for num in range(-10, 0):
#         print(num)
# 2D lists & loops
# number_grid = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9],
#         [0]
# ]
# for row in number_grid:
#         for column in row:
#                 print(column)
# ------------------------try except--------------------
# try:
#         division = 10 / 0
#         number = int(input("Enter a number: "))
#         print(number)
# except ZeroDivisionError as err:
#         print(err)
# except ValueError:
#         print("Invalid input")
# ------------Reading files--------------open(file name, w = write r = read a = append r+ = read and write) always close the file after
# employees_file = open("employees.txt", "r")
# for employee in employees_file.readlines():
#         print(employee)
#
# employees_file.close()
# -----------------------------writing files
# employees_file = open("employees.txt", "a")
# employees_file.write("\nsample")
# # for employee in employees_file.readlines():
# #         employees_file.write("hello " + employee)
# employees_file.close()
# --------------------------Modules and pip----------------
# import sample_module
# conversion = sample_module.roll_dice(6)
# print(conversion)
# -------------classes------------
# from Student import Student
# student = Student("kevin", 21, "male", 3.57, False)
# print(student.__str__())
# ----------------Inheritance-------------
