#Display all prime numbers between 1 to 250
#store the results in a results.txt

# check number is Prime
def isPrime(num):
    for n in range(2,num):
        if num % n == 0:
            return False
    return True

#write the Prime number to a results.txt file
def storeResults(s):
    f = open("results.txt", "w")
    f.write(s[:len(s)-1])
    f.close()



def checkPrime():
    s = ""
    for n in range(1, 251):
        if isPrime(n):
            s = s + str(n) + "\n"

    print("The prime numbers between 1 to 250 :")
    print(s)      
    
    storeResults(s)

checkPrime()                