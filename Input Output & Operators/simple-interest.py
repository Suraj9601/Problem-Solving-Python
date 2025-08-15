# 37. Input principal, rate and time; calculate simple interest.

P = float(input("Enter amount : "))
R = int(input("Enter rate in % : "))
T = int(input("Enter the time period in year : "))
SI = P * R * T / 100
print("Simple Interest : ",SI)