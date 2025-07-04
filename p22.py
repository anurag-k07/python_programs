items={}
item_count=0
while True:
    print("""\t\t**MENU**
    1.Add items and quantity
    2.Remove item
    3.Update quantity
    4.Print all items and its quantity
    5.Exit""")
    ch=int(input("Enter your choice(1-4)"))
    match ch:
        case 1:
            item_n=input("Enter item name")
            item_c=int(input("Enter item quantity"))
            items[item_n]=item_c
            item_count+=1
        case 2:
            item_n=input("Enter item name")
            del items[item_n]

        case 3:
            item_n=input("Enter item name")
            item_cup=int(input("Enter updated item quantity"))
            items[item_n]=item_cup

        case 4:
            for i,j in items.items():
                print(i,": ",j)
        
        case 5:
            break

        case _:
            print("Invaid input")