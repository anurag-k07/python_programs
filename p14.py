print("Python program to check whether a no. is palindrome or not")
n=int(input("Enter the no. :"))
temp=n
rev=0
while temp > 0:
    rem=temp % 10
    rev=(rev* 10)+rem
    temp=temp//10
if n==rev:
   print('The no.',n,'is Palindrome')
else:
    print('The no.',n,'is Not Palindrome')