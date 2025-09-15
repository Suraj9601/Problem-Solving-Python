# 68. Input total seconds and print as HH:MM:SS.
sec = int(input("Enter total seconds : "))

hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60

print(f"Time = {hours:02d}:{minutes:02d}:{seconds:02d}")
