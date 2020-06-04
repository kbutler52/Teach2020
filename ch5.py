
#06-03-2020
#practice using input

#Write a program that uses the input() function to prompt the user to entr an
#integer
#into a variable called num1.
#next,prompt the user to enter another integer and store the input
#into another variable called num2.
#use the print() function to display the message.

num1 = input("Enter an integer:")
num2 = input("Enter another integer:")
print('You have entered %s and %s.' %(num1,num2))

num3= input('Please enter a number from 1 to 5: ')
num4 = input('Please enter another number from 6 to 10: ')
print('You have enter %s and %s.' %(num3, num4))

num5 = input('Enter integer: ')
num6 = input('Enter a second integer: ')
print('You have entered %s and %s.' %(num5,num6))

#06-04-2020
#practice eamples from chapter 5 question 8

#use the input () function twice

in1 = input('Please enter an integer:  ')
in2 = input('Sorry to bother you , but can you please enter another integer:  ')
in1 = int(in1)
in2 = int(in2)
average = (in1 +in2) / 2
print('The average is %.2f' %(average))

#06-04-2020
#practice
#write a program that prompts the user to enter her name.
#The program then prompts the uer to enter her favorvite number.

name = input('Please enter your name:  ')
favNum = input('Hi %s, What is your favorite number?: ' %(name))
print('%s\'s favorite number is %s.' %(name,favNum))



