def create_file():
    fobj=open("new.txt","w")
    cont=input("Enter the things to add to txt file:")
    fobj.write(cont)
    fobj.close()
def read_file():
    fin=open("new.txt","r")
    s=fin.read()
    print(s)
    fin.close()
create_file()
read_file()