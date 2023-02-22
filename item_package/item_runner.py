from item_package.item_module import Item

item1 = Item()
item2 = Item()

item1.descr = "Tea"
item2.descr = "Coffee"
item1.quantity = 4
item1.price = 100
item2.quantity = 7
item2.price = 200

# item1.descr = item2.descr

print("Price:", item1.price)
print("Price:", item2.price)

item1.calculate_discounted_price()
item2.calculate_discounted_price()







