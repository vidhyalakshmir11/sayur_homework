#defining function for owner to add new item in to the  menu
def owner():
    item = input ("Enter the item to add :")
    price = int(input("Price of that item :"))
    itemDict[item] = price #add item as key and price as value
    print("It's added into the MENU list : ")
    print("MENU :")
    for key, value in itemDict.items():#print the key and value of item dictionary 
        print("*",key, value)
    
#defining function for customer to buy and calculate bill
def customer():
    print("Menu:")
    for key, value in itemDict.items():
        print("*",key, value)
    order = input("What do you want ? ")
    while True:
        if order in itemDict:  # check if ordered item is in menu 
            count = int(input("How many ? "))
            bill = itemDict[order] * count #calculate bill from itemName (value) using dictionaryName[key] 
            order = input("Do you anything else sir? ")
            if order.lower() == "nothing"  or order.lower() == "no" :
                return Bill(bill) #call bill function
        else: #  if ordered item is not in menu
            print("No such product available Sir !")
            order = input("Do you want anything else ? ")
            if order.lower() == "nothing"  or order.lower() == "no" :
                return 

#defining function for calculate total bill include tax and tips
def Bill(bill):
    # initialize the tax and tip amount
    Tax= 20  
    Tip= 20
    Discount = 0 # initialize discount variable as 0
    Bill_amount = Tax+Tip+bill # calculate bill with tax and tip amount
    if Bill_amount  > 1000 : #if total bill is greater than 1000 , then give an discount
        Discount= (30/100)*bill
        return print(f"Congratulations! \n Your bill  is {bill} , crossed above 1000 and you got discount Sir! and the bill is :{Discount}")
    return print("Your bill along with tax and tips :", Bill_amount) 

#initialize the menu with some items as dictionary
itemDict={"tea":15, "cappuccino":25, "coffee":20, "pizza":50}
while True:
    while True:
        ask= input (" Are you Customer/Owner ? ") # ask for if it is customer to buy or owner to add item into menu
        if ask.lower() =="customer": 
            customer()
            break
        elif ask.lower() =="owner":
            owner()
            break
        else :  # if the input is not realted to conditions -show invalid 
            print("Invalid input,Sir!")

    ask = input("Do you want to stop? (Yes/No) ")
    if ask.lower() == "yes":
        break
    elif ask.lower() =="no" :
        continue
    else :
        print("Invalid Answer Sir!")
