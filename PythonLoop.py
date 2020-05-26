#05-25-2020
#Homework#3
#write a program that loops from 0 to 10
# In each loop print the number and if that number is even or odd
books = 11
print(books %2 ==0)#divides books by 2, and see if the remainder is 0, it also checks our if condition
print(not(books %2 ==0))#checks to see if the remainder of books by 2 is NOT 0, it also checks our elif condtion

if (books %2 ==0):
        print(f"{books} is even")
elif (not(books %2 ==0)):
    print(f"{books} is odd")


