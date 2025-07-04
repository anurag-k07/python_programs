#Design a menu to find (i)Largest among 3 nos. (ii)No. is +ve or-ve (iii)Arithmetic operations by using menu interface
print("""\t**MENU**
1.Largest among 3 nos.
2.No. is +ve or-ve
3.Arithmetic operations by using menu interface""")
choice=int(input("\nEnter Your Choice(1-3)"))
#(i)Largest among 3 nos.
if(choice==1):
    n1=float(input("Enter the 1st no. :"))
    n2=float(input("Enter the 2nd no. :"))
    n3=float(input("Enter the 3rd no. :"))
    if(n1>n2 and n1>n3):
        print("Biggest among 3 nos. =",n1)
    elif(n2>n1 and n2>n3):
        print("Biggest among 3 nos. =",n2)
    else:print("Biggest among 3 nos. =",n3)
    #(ii)No. is +ve or-ve
elif(choice==2):
    n=float(input("Enter the no. :"))
    if n>0:print("The no.",n,"is +ve")
    elif n<0:print("The no.",n,"is -ve")
    else:print("The no. is neither +ve nor -ve")
    #(iii)Arithmetic operations by using menu interface
elif(choice==3):
    print("""\t*MENU*
    1.Addition of two nos.
    2.Subtraction of two nos.
    3.Division of two nos.
    4.Multiplication of two nos.""")
    c=int(input("\nEnter Your Choice(1-4)"))
    no1=float(input("Enter the 1st no. :"))
    no2=float(input("Enter the 2nd no. :"))
   #Addition
    if c==1:
        add=no1+no2
        print(no1,"+",no2,"=",add)
    #Subtraction
    elif c==2:
        sub=no1-no2
        print(no1,"-",no2,"=",sub)
    #Division
    elif c==3:
        div=no1/no2
        print(no1,"/",no2,"=",div)
    #Multiplication
    elif c==4:
        mul=no1*no2
        print(no1,"*",no2,"=",mul)
    else:print("Please give a valid choice...")
else:print("Please give a valid choice...")