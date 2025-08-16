# 42. Input marks in 5 subjects and calculate percentage.
print("Enter the for each subject : ")
ds = int(input("1) Data Structure : "))
os = int(input("2) Operating System :"))
oop = int(input("3) Object Oriented Programming : "))
de = int(input("4) Digital Electronics : "))
m = int(input("5) Mathematics : "))

percentage = (ds + os + oop + de + m) / 5

print("Percentage : ", percentage)
