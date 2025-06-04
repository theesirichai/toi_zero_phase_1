month = int(input("เดือน : "))
day = int(input("วัน : "))

if (month == 12 and day >= 21) or month == 1 or month == 2 or (month == 3 and day < 21):
    season = "winter"
elif (month == 3 and day >= 21) or month == 4 or month == 5 or (month == 6 and day < 21):
    season = "spring"
elif (month == 6 and day >= 21) or month == 7 or month == 8 or (month == 9 and day < 21):
    season = "summer"
elif (month == 9 and day >= 21) or month == 10 or month == 11 or (month == 12 and day < 21):
    season = "fall"
else:
    season = "unknown"

print(season)