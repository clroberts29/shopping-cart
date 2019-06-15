# shopping_cart.py

#from pprint import pprint

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

# Capture user inputs
receipt_list = []

id_list = [p["id"] for p in products]
# print(id_list)


user_input = "String"


while user_input != "DONE":
    
    user_input = (input("Please input a product identifier, or type 'DONE' if there are no more items."))
    
    if user_input == "DONE":
        print("THANK YOU! Your items have been registered.")
        print(receipt_list)
    else:
        print("Not done yet")
        try:
            user_input = int(user_input)
            print("trying...")
        except ValueError:
            print("Error (1)! Invalid entry. Try again.")

        print(type(user_input))

        if user_input in id_list:
            receipt_list.append(user_input)
            print(receipt_list)
        else:
            print("Error (2)! Invalid number. Try again.")
    

#print(user_item_list[])

# Validate user inputs are legitimate

# Create a "done" option

# Print the receipt including...
    
    # Name of the store
print("------------")
print("Charlie's Python Emporium -- Pythons and More!")
print("------------")
    # A grocery store phone number and/or website URL and/or address of choice
print("Phone Number: 1-800-GET-ITEM")
print("Website: www.CsPythonEmp.com")
print("1 West 4th Street")
print("New York, NY")
print("10001")

    # The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
currentDT = datetime.datetime.now()
print ("Checkout time: " + currentDT.strftime("%Y-%m-%d %H:%M"))
print("------------")

