trip_price = float(input())
n_puzzles = int(input())
n_dolls = int(input())
n_bears = int(input())
n_minions = int(input())
n_trucks = int(input())

price_puzzle = 2.60
price_dolls = 3
price_bear = 4.10
price_minions = 8.20
price_trucks = 2

total_price_articules = (n_puzzles*price_puzzle) + (n_dolls*price_dolls) + (n_bears*price_bear) + (n_minions*price_minions) + (n_trucks * price_trucks)

if (n_trucks+n_minions+n_puzzles+n_dolls+n_bears) >= 50:
    total_price_articules -= (total_price_articules*0.25)

# total price = total price - ( total price * 0.25 ) 25% disc of the whole price for more than 50 articules

rent = (total_price_articules*0.1)

if ( total_price_articules - rent) >= trip_price:
    print(f"Yes! {((total_price_articules - rent - trip_price)):.2f} lv left.")
else:
    print(f"Not enough money! {(trip_price - (total_price_articules - rent)):.2f}lv needed.")

