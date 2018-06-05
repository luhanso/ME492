# Lucas Hanson - Week 3 Day 4 - Assignment 2

Hours = int(input("Please enter the number of hours: "))
RPH = int(input("Please enter the rate per hour: "))

if Hours > 40:
    OT = Hours-40
    OTRPH = 1.5*RPH
    GrossPay = 40*RPH+OT*OTRPH
elif Hours <= 40:
    GrossPay = Hours*RPH

print('Your calculated gross pay is: $',GrossPay)
