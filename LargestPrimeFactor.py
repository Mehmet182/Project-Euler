'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
'''

def Largestprime(number):
    largestprime=1
    for i in range(2,number+1):
        if number%i==0:
            while number%i==0:
                number=number//i

            largestprime=i

    return largestprime



#print(Largestprime(7))
answer=Largestprime(600851475143)
print(answer)
