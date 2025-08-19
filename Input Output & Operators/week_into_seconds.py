# 57. Print number of seconds in a week.
week = int(input("Enter the week count : "))
print("Week to seconds Conversion : ")
day = week * 7
hour = day * 24
seconds = hour * 3600
print(week, "Week :", seconds, "seconds.")
