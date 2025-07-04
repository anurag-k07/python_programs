n=eval(input('Enter the no. to multiplicate:'))
o=eval(input('Enter the no. of multiples you want:'))
print('Multiples of',n)
print('-'*15)
for i in range(1,o+1):
    m=n*i
    print(n,'x',i,'=',m)