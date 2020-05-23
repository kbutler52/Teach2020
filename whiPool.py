cars = 25
buses = 25

print(cars < buses)#this checks our if loop condition
print(cars == buses)
print(not(cars < buses)) #This check our else loop


#now we start writing our program from using the above

if (cars < buses):
    print(f" We have less cars than buses")
elif(cars == buses):
    print("We equal number of cars and buses")
else:
    print("We have more cars than buses")


