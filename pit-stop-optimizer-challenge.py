# Pit Stop Timing Optimizer 
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew."


# Collect inputs
totalRaceTime = (float(input('Total race time in seconds: ')))
numPitStops = int(input('Number of pit stops: '))
avgPitStops = float(input('Enter the avarage pit stop duration in seconds: '))


# Calculate total pit time
totalPitTime = numPitStops * avgPitStops
pitPercentage = (totalPitTime / totalRaceTime) * 100

# Print results
print("\n--- Pit Stop Summary ---")
print(f"Total pit stop time: {totalPitTime} seconds")
print(f"Percentage of race in pits: {pitPercentage}%")

# Optional feedback
if pitPercentage > 5:
    print("You need a new pit crew. ")
