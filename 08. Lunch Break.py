import math

serial = str(input())
lenght_ep = int(input())
lenght_break = int(input())

time_lunch = lenght_break/8
time_leisure = lenght_break/4
time_left_watch = lenght_break - (time_lunch+time_leisure)

if time_left_watch >= lenght_ep:
    print(f"You have enough time to watch {serial} and left with {math.ceil((time_left_watch-lenght_ep))} minutes free time.")
elif time_left_watch <= lenght_ep:
    print(f"You don't have enough time to watch {serial}, you need {math.ceil(lenght_ep-time_left_watch)} more minutes.")