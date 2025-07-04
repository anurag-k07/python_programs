#write a function using text file to print the content of the text file in the reverse format
def rev_textfile():
    file_input=open('test.txt','r')
    file=file_input.read()
    rev=file[::-1]
    print(rev)
rev_textfile()