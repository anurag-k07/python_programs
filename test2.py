'''s='anurageio'
s.lower()

lst=[]
v=['a','e','i','o','u']
for i in s:
    if (i in v) and (i not in lst):
        lst.append(i)
print(lst)'''
s=input("Enter string:")
d={}
s.lower()
for i in s:
    if i not in d:
        d[i]=s.count(i)
    else:pass
print(d)

