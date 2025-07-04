#Program to convert feet into inches & vice versa by using menu interface
print("""\t\t\tMENU
      \t\t1.Feet to inches
      \t\t2.Inches to feet""")#\t= One tab space
choice=int(input("Enter Your Choice(1-2): "))
if(choice==1):
    feet=float(input("Enter the value of feet: "))
    inch=feet*12
    print("The value of",feet,"feet in inches is",inch)
elif(choice==2):
    inch=float(input("Enter the value of inch: "))
    feet=inch/12
    print("The value of",inch,"inch in feet is",feet)
else:print("The choice you have given is not available.......Please give a valid choice")