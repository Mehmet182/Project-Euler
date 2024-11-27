'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 10 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

'''

def karebul(num):
    result=0
    sum=0
    for i in range(num+1):
        result=result+i*i
        sum=sum+i
    sum=sum**2
    answer=sum-result
    print("sum of the squares ={}".format(result))
    print("square of the sumtoplamlarin karesi= {} ".format(sum))
    print("karelerin toplami ile toplamlarin karesi arasindaki fark= {}".format(answer))

karebul(10)