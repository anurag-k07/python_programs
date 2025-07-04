#Python program to calculate and display frequency of each item in a list using a CountFrequency() which accepts list as argument
print("Python program to calculate and display frequency of each item in a list using a CountFrequency() which accepts list as argument")
def CountFrequency():
    lst=eval(input("Enter the items in[]:"))
    frequency={}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    for i in frequency:
        print(i,":",frequency[i])
CountFrequency()