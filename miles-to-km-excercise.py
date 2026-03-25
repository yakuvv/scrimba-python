name = input("What is your name? ")
distance = float(input("Distance in km? "))
distance_mi = float(distance) / 1.609


print(f"Hello, {name.title()}! your distance {distance} km is equivalent to {round(distance_mi, 2)} miles.")
