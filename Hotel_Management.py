menu={
    
    "Pizza":700,
    "Burger":300,
    "Fries":200,
    "Coffee":100,
    "Pasta":250,
    "Salad":200,
    
}

print("WELCOME TO OUR RESTURANT!!")
print("Pizza : 700Rs \nBurger: 300Rs \nFries: 200Rs \nCoffee: 100Rs \nPasta: 250Rs \nSalad: 200Rs")

order_total=0
item_1=input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} is added to your order")
else:
    print(f"Order item {item_1} is not available yet ")
        
another_order=input("Do you want to add another item? (Yes/No) ")
if another_order=="Yes":
    item_2=input("Enter the name of Second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"item {item_2} is added to your order ")
    else:
        print("Order item is not available! ")
print(f"Total amount of item is {order_total} to pay")     

        
            

    


