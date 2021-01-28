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
samples = ["bulbasaur", "charmander", "squirtle"]
for sample in samples:
        print(sample)