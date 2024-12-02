'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the nth prime number?

'''
import time

def calişma_suresi(func, *args):
    baslangic_zamani=time.time()

    func(*args)

    bitis_zamani=time.time()

    return bitis_zamani-baslangic_zamani

def is_prime2(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # Daha verimli bir asal kontrolü
        if num % i == 0:
            return False
    return True


def is_prime(num):
    j=num
    if j==2:
        #return print("asal")
        return True

    while j!=2:
        j-=1
        if num%j==0:
            return False
            #return print("asal değil")
    
    if j==2:
        #return print("asal")
        return True


def find(num):
    k=1
    prime=[2]
    for i in range(3,500000,+2):
        if is_prime(i) :
            prime.append(i)
            k+=1
        
        if k==num:
            break
    answer=prime[k-1]
    print(answer)
        

#find(10001)
print(f"Çalişma süresi: {calişma_suresi(find, 10001)} saniye")
