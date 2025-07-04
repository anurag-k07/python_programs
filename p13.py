print("Python program to print the 1st n Fibonacci series")
n=int(input("Enter the no. of fibonacci series you want:"))
a,b = 0,1
for i in range(n):
    print(a,end=' ')
    a,b = b,a+b