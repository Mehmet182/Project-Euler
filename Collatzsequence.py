'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under the given limit, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above limit.

'''

def CollatzeQueence(num,toplam):

    while num!=1:
    
        if num%2==0:
            toplam+=1
            num=num//2

        else:
            toplam+=1
            num=3*num+1
    
    return toplam



def find(num):
    en_buyuk=0
    for i in range(2,num):
        toplam=0
        k=CollatzeQueence(i,toplam)
        if k > en_buyuk:
            en_buyuk=k
            sonuc=i
            #print("en uzun olani ={}".format(i))

    return sonuc


print(find(1000000))