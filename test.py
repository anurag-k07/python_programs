'''str=input("Enter string:")
rev=""
for i in str:
    rev=i+rev
print("Reversed string:",rev)
if rev==str:
    print(str,"is palindrome")
else:print(str,"is not palindrome")'''
'''d={}
n=int(input("Enter no. of students:"))
for i in range(n):
    rno=int(input("Enter roll no. :"))
    name=input("Enter name:")
    marks=int(input("Enter marks:"))
    d[rno]={"Name":name,"Marks":marks}
print(d)
print("Students with above 75 marks:-")
for j in d:
    if d[j]["Marks"]>75:
        print(d[j]["Name"])'''
while k>=10 and k<20:
    print(k)
    k+=1