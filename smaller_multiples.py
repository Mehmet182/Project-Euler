'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

'''


def is_prime(num):
    i=num
    if i==2:
        #return print("asal")
        return True

    while i!=2:
        i-=1
        if num%i==0:
  
            return False
            #return print("asal değil")
    
    if i==2:
        #return print("asal")
        return True

       
def smaller_multiples(num):
    result=1
    for i in range(num,1,-1):
        num2=i

        if num2%2==0:
            while num2%2==0:
                num2=num2//2
                if num2==1:
                    result*=2
    
        elif num2%3==0:
            while num2%3==0:
                num2=num2//3
                if num2==1:
                    result*=3


        if is_prime(i) and i!=2 and i!=3:
            result*=i
            #print("smaller_mutiples_for={}".format(result))

    
    print("smaller_mutiples={}".format(result))

smaller_multiples()