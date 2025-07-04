print("""\t\t*MENU*
      \t1.MULTIPLES OF 2 TILL 100
        2.MULTIPLES OF 3 TILL 100
        3.MULTIPLES OF 5 TILL 100
        4.MULTIPLES OF 7 TILL 100
        5.MULTIPLES OF 9 TILL 100""")
choice=int(input("Enter Your Choice(1-5):"))
if(choice==1):
    for m2 in range(2,101,2):
        print(m2,end=" ")
elif(choice==2):
    for m3 in range(3,101,3):
        print(m3,end=" ")
elif(choice==3):
    for m3 in range(5,101,5):
        print(m3,end=" ")
elif(choice==4):
    for m4 in range(7,101,7):
        print(m4,end=" ")
elif(choice==5):
    for m5 in range(9,101,9):
        print(m5,end=" ")
else:print("The choice you have given is not available")