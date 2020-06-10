#06-10-2020

#chapter 5(continued)
#question 11
# write a program that prompts the user to enter 5 numbers,
#separting the numbers with commas. Calcuate the sum of the
#5 numbers and display the numbers entered and the sum the
#to the user
userInput = input('Please enter 5 numbers,separated by commas: ')
inputList = userInput.split(',')
print('\nyou entered %s,%s,%s,%s,%s.' %(inputList[0],inputList[1],inputList[2],inputList[3],inputList[4]))
print('The sum is %d.' %(int(inputList[0]) + int(inputList[1]) + int(inputList[2])+int(inputList[3]) + int(inputList[4])))

