'''s=input("Enter a string:")
v='a','e','i','o','u','A','E','I','O','U'
vowel=0
lower=0
upper=0
for i in s:
    if i in v:
        vowel+=1
for lo in range(97,122+1):
    for j in s:
        if j in chr(lo):
            lower+=1
for up in range(65,90+1):
    for k in s:
        if k in chr(up):
            upper+=1
print("No. of vowels=",vowel)
print("No. of lower case characters=",lower)
print("No. of upper case characters=",upper)'''
X=eval(input("."))
n=eval(input(":"))
a=1
for i in range(n):
    a*=X
print(a)