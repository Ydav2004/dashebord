# rent for students for share per person 

rent = int(input("Enter your hostel/flate rent = "))
food = int(input("Enter your food bill = "))
electicty = int(input("Enter your electitcty bill = "))
chargers_peruntit = int(input("Charges per unit person = "))
person = int(input("Enter The person living unit room/flate rent = "))


total_bill = electicty * chargers_peruntit 
output = (rent+food+total_bill)//person

print("Each person will pay = ",output)