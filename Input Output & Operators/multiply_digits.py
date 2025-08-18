# 56. Multiply all digits of a number.

num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10      # last digit nikalo
    product *= digit      # product me multiply karo
    num = num // 10       # last digit hatao

print("Multiplication of all digits:", product)
