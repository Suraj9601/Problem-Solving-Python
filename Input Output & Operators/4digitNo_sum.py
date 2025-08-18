# 54. Input a 4-digit number and print the sum of all digits.

num = int(input("Enter the number upto 4 digits : "))
f_digit = num // 1000
s_digit = (num // 100) % 10
t_digit = (num // 10) % 10
l_digit = num % 10

sum = f_digit + s_digit + t_digit + l_digit

print("Sum of all Digits : ", sum)
