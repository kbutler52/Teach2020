
#05-30-2020
#Chapter4
#Question 1
name1 = 'Jamie'
print(name1)
namer = 'Aaron'.upper()
print(namer)
message = ('The names are %s and %s.' %(name1, namer))
print(message)

lang1 =('Python')
lang2 = ('Java')
lang3 = ('C#')
print('The most popular programming languages are %s, %s and %s.' %(lang1,lang3,lang2))
message1 =('The most popular programming languages are %s, %s, and %s.'%(lang1,lang2,lang3))
message2 = ('The most popular programming languages are %s,%s and %s.' %(lang1,lang3,lang2))
print(message1)
print(message2)
num= 12
message = ('%d' %(num))
print(message)

message = ('%4d' %(num))
print(message)

decnum = 1.72498329745
messagez = ('%5.3f' %(decnum))
print(messagez)

messagez = ('%7.2f' %(decnum))
print(messagez)

p, q =111,13
result = p/q
print(result)


messagex='My name is {} and I am {} years old.' .format('Jamie',31)
print(messagex)

student1 = 'Aaron'
student2 = 'Beck'
student3 = 'Carol'
messageb =('My best friends are {}, {} and {}.' .format(student1,student2,student3))
print(messageb)

x,y=12,7
quotient = x/y
result = quotient
print (f"The results of 12 divided by 7 is {result}, correct to 4 decimal places")
numberq= 2.7123
numberq = int(numberq)#this is casting a numberq into an integer.
print(numberq)

#how do you convert the number 2.12431 into a string?
numberz = str(2.12431)
print(numberz)

userInput = str('12')
userInput = int(userInput)
print(userInput)

myList = [1,2,3,4,5,6]

testScores =[10,11,12,13]
print(testScores[3])
print(testScores[-1])


























