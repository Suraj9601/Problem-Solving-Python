# 66. Calculate total bill with tax (price + tax%).
price = float(input("Enter the price : "))
tax = float(input("Enter the Tax in % : "))
tax = tax * price / 100
bill = price + tax
print("Price : ", price)
print("Tax : ", tax, "%")
print("Total bill : ", bill)
