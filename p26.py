#menu based python program to do following operations
#to find factorial of a natural no.
#to print the first N fibonacci series
#to find the sum of first N natural nos.
def fact(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact
def fibonacci(y):
    a,b=0,1
    for i in range(y):
        a,b=b,a+b
    return b
N=int(input("how many terms?:"))
print(fibonacci(N))