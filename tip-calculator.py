print("Welcome to the tip calculator.")

total = float(input("What what the total bill? $ "))
percent = float(input("What percentage of the tip would you like to give? 10, 12, or 15? "))
total_after_tip = percent / 100 * total + total
amount_of_people = int(input("How many people are splitting the bill? "))
total_after_split = total_after_tip / amount_of_people

print(f"Each person should pay: ${round(total_after_split,2)}")
