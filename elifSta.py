
#05-24-2020
caps = 100
gowns = 200

print(gowns < caps)#this will check our if condition
print(gowns == caps)#this will check the elif condtion
print(not(gowns < caps))#this will check our elif condition

if (gowns< caps):
    print(f"We have {100} less caps than gowns")
elif (gowns == caps):
    print("We have %d  gowns and caps." %(200))
else:
    print("We have {} more gowns than caps." .format(100))


