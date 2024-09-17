budget = float(input())
n_videocards = int(input())
n_processors = int(input())
n_rams = int(input())

total_price_videocard = 250*n_videocards
total_price_processor = n_processors * (0.35 * total_price_videocard)
total_ram_price = n_rams * (0.10*total_price_videocard)

total_sum = total_price_videocard + total_price_processor + total_ram_price

if n_videocards > n_processors:
    total_sum -= (0.15*total_sum)


if total_sum <= budget:
    print(f"You have {(budget-total_sum):.2f} leva left!")
elif total_sum >= budget:
    print(f"Not enough money! You need {(total_sum-budget):.2f} leva more!")


