#to find factorial of a no.
'''num=int(input("Enter a no. :"))
j=1
a=1
while (a<=num):
    j=j*a
    a+=1
print(j)'''

#multiplication from 1 to 10 of a user input no.
'''n=int(input('Enter the no. :'))
for i in range(1,11):
    r=n*i
    print(n,'x',i,'=',r)'''

'''#nested loop
t=int(input('Enter how many times u want to print :'))
for i in range(t):
    for j in range(i+1):
        print(t,end=' ')
    print()'''
'''L=[10,"FUN",40,"FEW",50,"FULL"]
L1=[]
for i in L:
    if type(i)==int:
        i=i*i
    elif type(i)==str:
        i=i.lower()
    L1.append(i)
print(L1)'''
'''d={}
for i in range(5):
    state=input("Enter state:")
    capital=input("Enter capital:")
    d[state]=capital
print(d)
search=input("Enter the state:")
if search in d:
    print(search,"is found in the dictionary with capital",d[search])
else:print("State not found in dictionary")'''
for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
            break