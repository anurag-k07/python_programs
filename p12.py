#Python program to print ascending order of 3 nos.
n1=float(input("Enter the 1st no. :"))
n2=float(input("Enter the 2nd no. :"))
n3=float(input("Enter the 3rd no. :"))
if n1>n2 and n2>n3:
    print(n3,"<",n2,"<",n1)
elif n1>n3 and n3>n2:
    print(n2,"<",n3,"<",n1)
elif n2>n1 and n1>n3:
    print(n3,"<",n1,"<",n2)
elif n2>n3 and n3>n1:
    print(n1,"<",n3,"<",n2)
elif n3>n1 and n1>n2:
    print(n2,"<",n1,"<",n3)
elif n3>n2 and n2>n1:
    print(n1,"<",n2,"<",n3)
else:print("Either any two nos. or all 3 nos. are equal")