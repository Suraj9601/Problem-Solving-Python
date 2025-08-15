# 38. Calculate compound interest (no formula). 

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest (%): "))
T = int(input("Enter Time in years: "))

amount = P
for _ in range(T):
    amount += amount * (R / 100)

CI = amount - P
print("Compound Interest =", round(CI, 2))
print("Final Amount =", round(amount, 2))
