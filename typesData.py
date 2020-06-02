#06-02-2020
#while loop
i=0
while i < 10:
    print(f"We have {i} things")
    i=i+1

a = 0
for q in range (1,10):
    print("We have %d cats." %(q))

    apples = 25
    pears = 20
    print(apples < pears)
    print(not(apples < pears))
    print(apples %2==0)
    print(not(apples %2==0))
    print(pears %2==0)
    print(not(pears %2==0))
if (apples < pears):
    print("We have less pears than apples")
elif(not(apples < pears)):
    print(" We have %d pears." %(20))
elif(apples %2==0):
    print("We have a even number of apples")
elif(not(apples %2==0)):
    print("we have a odd number of apples {}." .format(25))



