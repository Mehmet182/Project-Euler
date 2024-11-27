def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  
    return True    

def Summationofprimes(num):
    result=2
    for i in range(3,num,2):
        if is_prime(i):
            result+=i

    return result

print(Summationofprimes(2000000))