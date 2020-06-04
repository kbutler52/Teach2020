#Question 15, 16, 17,18 in workbook
# Assign the numbers 10,11,13,and 13 to a list called testscores.
#print the numbers at the index 3 and -1

testscores = [10,11,12,13]
print(testscores[3])
print(testscores[-1])

#Determine the output of the following program without running code
#Q16
myList = [1,2,3,4,5,6,7,8,9,10]
myList1 = myList
myList2 = myList[3:6]
myList3 = myList[:5]
myList4 = myList[2:]
myList5 = myList[1:7:2]
myList6 = myList[ : :3]

print(myList)
print(myList1)
print(myList3)
print(myList4)
print(myList5)
print(myList6)

#Assign the values 11,12,13,14,15,16,17,18,19,20 to a list called q17.
#use a slice to select the numbers 13 to 18 from q17 and assign them to a new list called slice A
#use another slice to select the numbers 13,16, and 19 from q17 and assign them to a lsit called sliceB
#use print () function to print sliceA and sliceB


q17 = [11,12,13,14,15,16,17,18,19,20]
sliceA= q17[2:8]
sliceB = q17[2: :3]
print(sliceA)
print(sliceB)

#quetion18
#create a list called emptyList with no inital values.
#Add the nubmers 12,5,9 and 11 to emptyList and use the
#print () function to print the list

emptyList=[]
emptyList.append(12)
emptyList.append(5)
emptyList.append(9)
emptyList.append(11)
print(emptyList)

#question 19
#Assign the nubmers 1,2,3,4 and 5 to a list called q19.
#next change the third number to 10 and use the print() function to print the list.

q19= [1,2,3,4,5]
q19[2]=10
print(q19)

#question20
#Assign the letters A,B,C,D and E to a list called q20.
#remove A and C from the list and print the list
#hint it's easier to remove c from the list first..

q20 = ['A','B','C','D','E']
del q20[2]
del q20[0]
print(q20)

#06-03-2020
#question 21
#Assign the strings 'Sun', 'Mon', 'Tue', 'Wed', 'Thurs','Fri'and 'Sat' to
#a tuple called daysOfWeek.
#assign the third element in daysOfWeek to a variable called myDay
#and print the value of myDay.

daysOfWeek = ['Sun','Mon','Tue','Wed','Thur','Fri','Sat']
myDay=daysOfWeek[2]
print(myDay)

#question22
#what is wrong with the following dictionary?
nameAgeDict = {'John':12, 'Matthew':15, 'Aaron':13,'John':14, 'Melvin':10}
print(nameAgeDict)
#answer John is used in the dictionary Twice.

#question 23
#Determine the output of the following program without running the code.

dict1 = {'Aaron':11, 'Betty':5, 0: 'Zero', 3.9: 'Three'}
print(dict1['Aaron'])
print(dict1[0])
#rint(dict1[3:9])
dict1['Aaron'] = 12
print(dict1)

del dict1['Betty']
print(dict1)
#the above did not work like the book said it
#should, talk to William about this one on Saturday 6-6-2020





