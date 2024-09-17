budget = float(input())
n_statisticians = int(input())
price_eqipment_per_stat = float(input())

price_decor = 0.10*budget

if n_statisticians > 150:
    price_eqipment_per_stat -= (price_eqipment_per_stat*0.10)

price_stat = price_eqipment_per_stat * n_statisticians

cost = price_stat + price_decor



if budget < (cost):
    print("Not enough money!")
    print(f"Wingard needs {(cost - budget):.2f} leva more. ")
elif budget >= (cost):
    print('Action!')
    print(f"Wingard starts filming with {(budget-cost):.2f} leva left.")







