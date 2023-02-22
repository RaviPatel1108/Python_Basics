custName = "Marry Smith"
itemDesc = ["shirt", "jeans", "glasses", "watch"]
itemNumber = 5
price = 500
tax = 25.78
quantity = 2
outOfStock = False

if itemNumber < len(itemDesc):
    if outOfStock:
        print("selected item is unavailable")
    else:
        message = custName + " wants to purchase " + str(quantity) + " " + itemDesc[0]
        if quantity > 1:
            print(message + "s")
        else:
            print(message)
        print("total cost with tax is:", quantity * (price + tax))
else:
    message = "Not selected correct item code"
    print(message)

