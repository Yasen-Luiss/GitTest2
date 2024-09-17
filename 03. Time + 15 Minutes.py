hour = int(input())
mins = int(input())

new_mins = mins + 15

if (new_mins-60) >= 0:
    hour += 1
    new_mins -= 60

if hour > 23:
    hour = 00

if new_mins < 10:
    print(f"{hour}:0{new_mins}")
else:
    print(f"{hour}:{new_mins}")
