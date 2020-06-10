#06-03-2020
#Chapter 5- Question1

#Determine the output of the following program without running the code:

a = 10
b = 4
print(a, "-", b, "=", a-b)

#question2
#rewrite the print() statement in question 1 to display
#same output using the % operator

a = 10
b =4

print("%d - %d = %d" %(a,b,a-b))

#question 3
#Rewrite the print() statement in question 1 to display the
#the same output using the format() method.

a = 10
b = 4
print("{} - {} = {}"  .format(a,b,a-b))

#question 4
#Determine the output of the following program without
#running the code.

print('''Date:\nJan 11, 2019
Time:\n1.28pm
venue: \nConvention center
Number of Pax:\n30''')


#question 5
#rint('This is a single quotation (') mark and this is a double qutation(") mark.')
#The code above will result in a sytax error. make the necessary amendment
#to correct it so that we get the following output:
# This is a single quatation(') mark and this is a double quotation (') mark.
print('This is a single qutation( \') mark and this is a double qutation( \") mark.')



#question 7
#Write a program that uses the input() function to prompt the user to enter an integer
#into a variable called num1.
#next, prompt the user to enter another integer and store the input into another
#variable called num2.
# Use the print() function to display the following message:
#You entered * and ^

num1 = input('Please enter an integer:')
num2 = input('Please enter another integer:')
print('You entered %s and %s' %(num1,num2))

#06-04-2020
#question 8

#Use the input() function twice to prompt users to enter two integers and store the
#input into two variables called in1 and in2.

#use the int() function to cast the inputs into integers and store the results
#back into int1 an int2

# Caluclate the average of the two numbers and assign the result to a variable
#called average. The average is found by adding the two numbers and dividing
#the result by 2
#Use print function to display the message
# The average is *






in1= input('Enter a integer: ')
in2 = input('Enter a second integer: ')

in1 = int(in1)
in2 = int(in2)

average = (in1 + in2) /2
print('The average is %.2f' %(average))

#question 9
#write a program that prompts the user to enter his/her name.
#The program then prompts the user to enter his/her favorite number
#using the prompt below:
#Hi Kyla, what is your favorite number?:
#Finally, the program displays the message
#Kyla's favorite number is

name = input('What is your name?: ')
favNum = input('Hi %s, What is your favorite Number?: '  %(name))
print('%s\'s favorite number is %s.' %(name, favNum))





