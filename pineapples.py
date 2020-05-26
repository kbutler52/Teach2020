#05-25-2020
#Test Objectives
#review material from Test printing, conditional statements, loops- done
#Create a variable names pineapple , set it to 10
pineapple = 10#create a variable name pineapples and set it to 10
print(f"I have {10} pineapples")
print("I have %d pineapples." %(10))
print("I have {} pineapples." .format(10))
#if I have more than 20 pineapples
pineapples = 30
if(pineapples > 20):
    print(" I have more than %d pinapples." %(20))
#if I have a even number os pineapples
pineapples = 20
print(pineapples %2==0)# divides pinapples by 2 to see if the remainder is 0 also checks our if condition
print(not(pineapples %2==0))#divides pinapples by 2 to see if the remainder is 0 checks our else condition
if(pineapples %2 ==0):
    print("I have a even number of pineapples")
else:
    print("I have a odd number of pineapples")
#if I have a odd number of pineapples
pineapples = 21
print(pineapples %2 ==0)#divides pineapples by 2 to see if the reminder is 0- also checks the if statement
print(not(pineapples %2 ==0))
if (pineapples %2 ==0):
    print("We have a even number of pineapples")
else:
    print("We have a odd number of pineapples")

#create a looping statement that prints how many pineapples you have reduce the number by 2 repeat until pineapples
#are less than 6 ( flexible)

pineapples = 20
while (pineapples > 0):#stop condition
    print(f" I have {pineapples} pineapples")
    pineapples = pineapples - 2#iteration/step

# was not able to get for loop to work
pineapples = 50
for i in range(5,5,2):
    print("I have {} pineapples." .format(i))
   # pineapples = pineapples - 1

#use input() to store how many cherries you have into variable- Print how many cherries you
howMany=int(input("How many Cherries do you have?"))#stores the number of Cherries
print("I have" + str(howMany))





