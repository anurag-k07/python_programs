'''ch='y'
while ch=='y':
    s=input("Enter a string:")
    rev=""
    for i in s:
        rev=i+rev
    print("Reversed string is",rev)
    if rev==s:
        print(s,"is a palindrome")
    else:print(s,"is not a plalindrome")
    ch=input("Do u want to restart?(y/n)")'''