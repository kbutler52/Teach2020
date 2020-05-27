
#05-27-2020
#this is a post test follow up from yesterday's test with william
#Create a variable named pineapples. set pindapples to 10

pineapples = 10
print("I have %d pineapples." %(10))
print("I have {} pineapples." .format(pineapples))
print(f"I have {10} pineapples.")

#create an conditional statement that:
#print:"I have more than 20 pineapples." If you have more than 20 pineapples.
#print: I have an even mumber of pineapples." If you have an even number of pineapples.
#print: I have an odd number of pineapples." If you have an odd number of pineapples.

print(pineapples > 20)
print(pineapples %2 ==0)
print(not(pineapples %2 ==0))

if(pineapples > 20):
    print("I have more than 20 pineapples")
elif(pineapples %2==0):
    print("I have an even number of pineapples.")
else:
    print("I have a odd number of pineapples")




