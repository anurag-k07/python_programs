#Grocery store management
while True:
    print("""\t\t**MENU**
    1.Add items and quantity
    2.Remove item
    3.Update quantity
    4.Print all items and its quantity
    5.Exit""")
    ch=int(input("Enter your choice(1-4)"))
    if ch==1:
        itemsqty={}
        n=int(input("How many items to add?:"))
        for i in range(n):
            item=input("Enter your item:")
            qty=input("Enter its quantity:")
            itemsqty[item]=qty
    if ch==2:
        remitem=input("Which item you need to remove:")
        if remitem in itemsqty:
            itemsqty.remove(remitem,)
        else:
            print(remitem,"not found in items")
    if ch==3:
        entupdqty=input("Which item's quantity to update:")
        if entupdqty in itemsqty:
            updqty=int(input("How much quantity:"))
            itemsqty.update(updqty)
        else:
            print(entupdqty,"not found in items")
        print(itemsqty)
