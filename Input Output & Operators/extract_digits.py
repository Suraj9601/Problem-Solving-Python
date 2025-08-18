# 55. Extract each digit from a 4-digit number and print.
num = int(input("Enter the 4-digit number : "))

f_digit = num // 1000
print("First Digit :", f_digit)

s_digit = (num // 100) % 10
print("Second Digit :", s_digit)

t_digit = (num // 10) % 10
print("Third Digit :", t_digit)

l_digit = num % 10
print("Last Digit :", l_digit)
