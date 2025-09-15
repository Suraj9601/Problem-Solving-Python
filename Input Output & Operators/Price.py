# 69. Calculate price per unit (total price ÷ quantity).
name = input("Enter the Product name : ")
total_price = float(input("Enter the Total price : "))
quantity = int(input("Enter the quantity of Product : "))
price = total_price / quantity
print(f"Price per {name} : {price:.2f}")
