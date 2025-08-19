# 59. Convert rupees to dollars (take conversion rate as input).
rupees = float(input("Enter the amount in rupees : "))
rate = float(input("Enter the current rate to convert : ")) # rate = 0.011498

doller = rupees * rate

print(rupees, "Rupees : ", doller, "Dollers.")
