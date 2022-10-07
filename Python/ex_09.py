#Q9

bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
cart={}
def viewBakeryItems():
    print("Item \t Price\n")
    for i in bakery_items:
        print(i,"\t", "Rs:",bakery_items[i])
    print("\n")
        
def addItem():
    item=int(input("""Please select item to be added:
                1. Bread
                2. Butter
                3. Jam
                4. Cheese
                5. Croissant\n"""))
    for i in bakery_items:
        res = int(list(bakery_items.keys()).index(i))+1
        if item==res:
            cart[i]=1
            break
    
def viewCart():
    print("Items in Cart:")
    print("Item \t Quantity\n")
    for i in cart:
        print (i,"\t",cart[i])
def updateCart():
    new_item=input("Enter the Item to be updated: ")
    qty=int(input("\nEnter the quantity: "))
    cart[new_item]=qty
def removeItems():
    item=input("Enter the item to be removed:")
    del cart[item]
def checkoutItems():
    cost=0
    for i in cart.keys():
        cost=cost+cart[i]*bakery_items[i]
    print("Total Amount: Rs:", cost)

i=True
while(i==True):
    print(""" Menu
            1. View the bakery items
            2. Add the item into the cart
            3. View the cart
            4. Update item in the cart
            5. Remove item from the cart
            6. Checkout and generate bill
            """)
    choice=int(input("Enter a number: "))
    print("\n")
    if choice==1:
        viewBakeryItems()
    elif choice==2:
        addItem()
    elif choice==3:
        viewCart()
    elif choice==4:
        updateCart()
    elif choice==5:
        removeItems()
    elif choice==6:
        checkoutItems()
        i=False
    else:
        print("Invalid number! Please try again.")



