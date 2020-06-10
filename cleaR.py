#06-10-2020
#use input command

name = input('Please enter you name: ')
favColor = input('%s,please enter your favorite color: '%(name))
print('%s\'s favorite color is %s.' %(name,favColor))

#use the input function twice to prompt users to enter two integers
#called in1 and in2

#use the int()function to cast the inouts into integers and
#store the results back into in1 and in2

in1 = input('Please enter a integer: ')
in2 = input('Please enter a second integer: ')
in1 = int(in1)
in2 = int(in2)

average =(in1 + in2) /2
print('The average is %.2f' %(average))

in1 = input('Please enter a number from 1 to 10:')
in2 = input('Enter another number from 10 to 20:')
in1 = int(in1)
in2 = int(in2)

average =(in1 + in2) / 2
print('The averge is %.2f.' %(average))




