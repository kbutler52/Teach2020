#05-15-2020
def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x==0):
             answer=checkIfPrime(13)
            return False
        return True


