#05-30-2020
i =0
while i<11:
    print(f" we have {i} pears.")
    i=i+1

kites = 20
for i in range(0,kites):
    print("We have %d kites." %(i))

apples = 25
pears = 20
print(apples < pears)
print(not(apples< pears))
print(apples %2 ==0)
print(not(apples %2 ==0))
print(pears %2 ==0)
print(not(pears %2 ==0))

if(apples < pears):
    print("apples is greater")
elif (not(apples < pears)):
    print("pears are greater")
elif (apples %2 ==0):
    print("Apples are even")
elif(not(apples %2 ==0)):
    print("apples are odd")
elif(pears %2 ==0):
    print("Pears are even")
elif(not(pears %2 ==0)):
    print("Pears are not even")



