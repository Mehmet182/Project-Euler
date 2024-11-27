'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.

'''

def palindrom(num):
    mynumber=num
    reversenumber=0

    while num !=0:
        temp=num % 10
        reversenumber=reversenumber*10 + temp
        num//=10
        #print(num)
        #print(reversenumber)

    if mynumber==reversenumber:
        #print("palindrom")
        return True
    else:
        #print("not polindrom")
        return False


def çarpanbulma():
    enbuyuk=1
    for i in range(99,1,-1):
        for j in range(i,1,-1):
            sayi=i*j
            if palindrom(sayi):
                if enbuyuk<sayi:
                    enbuyuk=sayi


def carpanbulma1(num):
    enbuyuk=num
    for i in range(1000):
        for j in range(i,1000):
            sayi=i*j
            if palindrom(sayi):
                if enbuyuk<sayi:
                    enbuyuk=sayi
                    eniyiİ=i
                    eniyiJ=j

    #return eniyiİ,eniyiJ,enbuyuk
    print("en iyi ve çarim değerleri = {} {}".format( eniyiİ,eniyiJ))
    print("en büyük palindrom = {}".format(enbuyuk))


print(carpanbulma1(1))

