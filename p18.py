a=eval(input("Enter list:"))
print("Reversed list:[",end="")
for i in range(len(a)-1,-1,-1):
    print(a[i],end=",")
print("]",end="")