import math

world_record_sec = float(input())
distance_m = float(input())
swim_1m_sec= float(input())

time_newrecord = distance_m*swim_1m_sec

w_resistance_delay = math.floor((distance_m / 15)) * 12.5

time_Ivan = time_newrecord + w_resistance_delay

if time_Ivan < world_record_sec:
    print(f"Yes, he succeeded! The new world record is {(time_Ivan):.2f} seconds.")
else:
    print(f"No, he failed! He was {(time_Ivan-world_record_sec):.2f} seconds slower.")

print("Time of Ivan in mins:",time_Ivan//60)