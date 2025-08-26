# 61. Calculate discounted price (original – discount%).

original_price = float(input("Enter the Original Price : "))
discount_percent = float(input("Enter the discount in % : "))

discount_amount = original_price * discount_percent / 100
discounted_price = original_price - discount_amount

print("Original Price : ", original_price)
print("Discounted Price : ", discounted_price)
