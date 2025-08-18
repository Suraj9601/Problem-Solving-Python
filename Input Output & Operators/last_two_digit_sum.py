# 52. Find sum of last two digits of a number.

num = int(input("Enter the number : "))
last_2Digits = num % 100

f_digit = last_2Digits // 10
l_digit = last_2Digits % 10

sum = f_digit + l_digit

print("Sum of Last two digits : ", sum)
