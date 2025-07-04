num=int(input("Enter the no. :"))
if num<=1:print(num,"is not prime no.")
else:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime no.")
            break
    else:print(num,"is prime no.")