'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.

'''

#sqrt krekök
import math

def SpecilPythagoreantriplet(n):
    found=False

    for a in range(1,n//2+1):
        if a==n//2:
            return False
        for b in range(a+1,(n//2)+1):
            c=(a**2)+(b**2)
            c=math.sqrt(c)
            if a+b+c==n:
                found=True
                print("multiplied numbers={},{},{}".format(a,b,c))
                print(a*b*c)
    
    if not found:
        print("Pythagorean triple not found")
    
    #if toplam==1:
    #    print("error")

SpecilPythagoreantriplet(120)