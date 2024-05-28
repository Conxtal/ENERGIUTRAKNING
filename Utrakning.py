from datetime import datetime, timedelta

#Input
kwh_per_day = float(input("kwH användning: "))
price_per_kwh = float(input("Pris på kWH: "))
start_date = datetime.strptime(input("Start datum (YYYY-MM-DD): "), "%Y-%m-%d")
end_date = datetime.strptime(input("Slut datum (YYYY-MM-DD): "), "%Y-%m-%d")

#Variables
current_date = start_date
total_cost = 0

#Kostnader
while current_date <= end_date:
    daily_cost = kwh_per_day * price_per_kwh
    print(f"{current_date.strftime('%Y-%m-%d')}: {daily_cost:.2f} RIKSDALER")
    total_cost += daily_cost
    current_date += timedelta(days=1)


print(f"\nTotal Kostnad: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}: {total_cost:.2f} SVENSKA RIKSDALER")
