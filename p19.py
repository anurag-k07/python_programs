students=eval(input("Enter the names of students in tuple format:"))
search_name=input("Enter the name of the student to search:")
if search_name in students:
    pos=students.index(search_name)
    print("The name",search_name,"is found with position",pos)
else:print("The name",search_name,"is not found")
