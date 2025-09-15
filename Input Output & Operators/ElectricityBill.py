# 67. Calculate electricity bill (units × rate).
units = int(input("Enter the meter units of electricity : "))
rate = float(input("Enter the rate for unit : "))
bill = units * rate
print("Total units : ", units)
print("Rate : ", rate)
print(f"Total Electricity Bill : {bill} Rs")
