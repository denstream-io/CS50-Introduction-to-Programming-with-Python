
time = input("Time: ")
minutes = "00"
if ":" in time:
    hour, am_pm = time.split(" ")
    hour, minutes = hour.split(":")
    print(hour, minutes, am_pm) # 9 00 AM
else:
    hour, am_pm = time.split(" ")
    print(hour, am_pm)

if am_pm == "AM":
    if hour == "12":
        print("00" + ":" + minutes)
    else:
        print(hour.zfill(2) + ":" + minutes)
elif am_pm == "PM":
    if hour == "12":
        print(hour.zfill(2) + ":" + minutes)
    else:
        print(str(int(hour) + 12) + ":" + minutes)