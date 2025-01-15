#  Detils of order 
print("Welcome Python Restaurant   ")
menu = {
     
     'Pasta' : 50,
     'Burger' : 70,
     'Coffe' : 80,
     'salad' : 60,
     'Pizza' : 100,
}
print(menu)
# greet
print("Pasta : 50\nBurger : 70\nCofee : 80\nsalad : 60\nPizza : 100")
order_total = 0
# input of order of the customer 

intem = input("Enter the Name of items of the customer = ")

if intem in menu:
     order_total += menu[intem]
     print(f"your item {intem} has been added to the order ")
     
else:
     print(f"please This {intem} item is not Avialble for me resturnat")
     
another_order  = input("please Do you want another order item ? (YES/NO) =  ")
     #  print(another_order)
if another_order == "Yes":
     item2 = input("Enter the name of second iteme orderd = ")
     if item2 in menu:
          order_total += menu[item2]
          print(f"item has {item2} been to added to order " )
     
     else:
          print(f"item has{item2} not avilable ")
          
print(f"Total amount of  items to pay is = {order_total}")   