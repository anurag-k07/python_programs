print('''Python program to input the value of x and n and print the sum of following series:
      1)1+x+x**2+x**3+x**n
      2)1-x+x**2-x**3+x**4+x**n
      3)x+x**2/2+x**3/3+x**n/n''')
ch=int(input("Enter your choice(1-3):"))
if ch==1 or ch==2 or ch==3:
    x=int(input("Enter the value of x:"))
    n=int(input("Enter the exponential value n:"))
if ch==1:
    sum=0
    for i in range (1,n+1):
        sum+=x**i
    sum+=1
    print(sum)
elif ch==2:
    sum=1 
    sign=-1 
    for i in range(1,n+1):
        term=sign*(x**i)
        sum+=term
        sign*=-1
    print("The sum of the series is:", sum)
elif ch==3:
    sum=0
    for i in range(1,n+1) :
        term=x**i/i
        sum+=term
    print("Sum=",sum)
else:print("Please enter a valid choice")